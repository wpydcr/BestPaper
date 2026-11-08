import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'scripts/reminder.py'


class ReminderTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SOURCE.is_file(), '缺少待实现的 reminder.py')
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.script = self.root / 'skill/scripts/reminder.py'
        self.script.parent.mkdir(parents=True)
        shutil.copyfile(SOURCE, self.script)
        self.prompt = self.root / 'skill/references/runtime/reminder.md'
        self.prompt.parent.mkdir(parents=True)
        self.prompt.write_text('测试提醒：执行已授权的修订。', encoding='utf-8')
        self.cwd = self.root / 'paper'
        self.cwd.mkdir()
        self.env = dict(os.environ, TMP=str(self.root), TEMP=str(self.root), PYTHONIOENCODING='utf-8')
        self.payload = {'session_id': 'session-a', 'cwd': str(self.cwd), 'hook_event_name': 'PostToolBatch'}

    def run_script(self, args=(), payload=None, raw=None):
        result = subprocess.run([sys.executable, str(self.script), *args],
                                input=raw if raw is not None else json.dumps(payload or self.payload),
                                capture_output=True, text=True, encoding='utf-8', env=self.env)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def command(self, name, session='session-a', cwd=None):
        return self.run_script([name, '--session-id', session, '--cwd', str(cwd or self.cwd)])

    def status(self):
        return json.loads(self.command('status').stdout)

    def test_first_hook_confirms_identity_then_default_interval_is_quiet(self):
        result = self.run_script()
        context = json.loads(result.stdout)['hookSpecificOutput']
        self.assertEqual(context['hookEventName'], 'PostToolBatch')
        self.assertIn('session-a', context['additionalContext'])
        self.assertIn(str(self.cwd), context['additionalContext'])
        self.assertIn('1800', context['additionalContext'])
        self.assertEqual(self.run_script().stdout, '')

    def test_due_reads_prompt_from_disk_and_does_not_repeat_early(self):
        self.run_script()
        time.sleep(0.03)
        self.prompt.write_text('独立标记：NOW-READ-42', encoding='utf-8')
        result = self.run_script(['--interval-seconds', '0.01'])
        self.assertEqual(json.loads(result.stdout), {'hookSpecificOutput': {
            'hookEventName': 'PostToolBatch', 'additionalContext': '独立标记：NOW-READ-42'}})
        self.assertEqual(self.run_script().stdout, '')

    def test_session_and_cwd_are_separate(self):
        self.run_script()
        other = self.cwd.parent / 'other-paper'
        other.mkdir()
        self.assertTrue(self.run_script(payload={**self.payload, 'session_id': 'session-b'}).stdout)
        self.assertEqual(self.run_script(payload={**self.payload, 'cwd': str(other)}).stdout, '')
        self.command('arm', cwd=other)
        self.assertFalse(self.status()['active'])
        self.assertEqual(self.run_script().stdout, '')
        self.assertEqual(len(list(self.root.glob('bestpaper-reminder-v1/*.json'))), 3)

    def test_cwd_change_cannot_autostart_another_project(self):
        self.run_script()
        other = self.cwd.parent / 'unrelated-task'
        other.mkdir()
        payload = {**self.payload, 'cwd': str(other)}
        self.assertEqual(self.run_script(payload=payload).stdout, '')
        self.command('disarm')
        self.assertEqual(self.run_script(payload=payload).stdout, '')
        self.assertEqual(len(list(self.root.glob('bestpaper-reminder-v1/*.json'))), 1)

    def test_new_prompt_from_another_cwd_pauses_session_only(self):
        self.run_script()
        other = self.cwd.parent / 'new-project'
        other.mkdir()
        self.run_script(payload={**self.payload, 'session_id': 'session-b'})
        payload = {**self.payload, 'cwd': str(other), 'hook_event_name': 'UserPromptSubmit'}
        result = self.run_script(payload=payload)
        self.assertTrue(result.stdout, '新目录中的用户消息也必须暂停当前会话旧授权')
        self.assertEqual(json.loads(result.stdout)['hookSpecificOutput']['hookEventName'], 'UserPromptSubmit')
        self.assertFalse(self.status()['active'])
        self.assertTrue(json.loads(self.command('status', session='session-b').stdout)['active'])
        self.assertEqual(self.run_script(payload=payload).stdout, '')
        self.assertEqual(self.run_script(payload={**payload, 'hook_event_name': 'PostToolBatch'}).stdout, '')

    def test_session_end_from_another_cwd_pauses_existing_project(self):
        self.run_script()
        other = self.cwd.parent / 'end-location'
        other.mkdir()
        self.run_script(payload={**self.payload, 'session_id': 'session-b'})
        result = self.run_script(payload={**self.payload, 'cwd': str(other), 'hook_event_name': 'SessionEnd'})
        self.assertEqual(result.stdout, '')
        self.assertFalse(self.status()['active'])
        self.assertTrue(json.loads(self.command('status', session='session-b').stdout)['active'])
        self.assertEqual(self.run_script().stdout, '')

    def test_explicit_new_project_arm_replaces_old_grant(self):
        self.run_script()
        other = self.cwd.parent / 'next-paper'
        other.mkdir()
        self.command('arm', cwd=other)
        self.assertFalse(self.status()['active'])
        self.assertTrue(json.loads(self.command('status', cwd=other).stdout)['active'])
        self.command('arm')
        self.assertTrue(self.status()['active'])
        self.assertFalse(json.loads(self.command('status', cwd=other).stdout)['active'])

    def test_pause_message_carries_current_identity_for_rearm(self):
        self.run_script()
        other = self.cwd.parent / 'after-compaction'
        other.mkdir()
        result = self.run_script(payload={**self.payload, 'cwd': str(other), 'hook_event_name': 'UserPromptSubmit'})
        context = json.loads(result.stdout)['hookSpecificOutput']['additionalContext']
        self.assertIn('session-a', context)
        self.assertIn(str(other), context)

    def test_arm_rejects_unexpanded_session_placeholder(self):
        result = self.command('arm', session='${CLAUDE_SESSION_ID}')
        self.assertEqual(result.stdout, '')
        self.assertTrue(result.stderr)
        self.assertFalse((self.root / 'bestpaper-reminder-v1').exists())

    def test_disarm_from_another_cwd_stops_all_current_session_projects(self):
        self.command('arm')
        other = self.cwd.parent / 'disarm-location'
        other.mkdir()
        self.command('arm', session='session-b')
        self.command('disarm', cwd=other)
        self.assertFalse(self.status()['active'])
        self.assertFalse(json.loads(self.command('status', cwd=other).stdout)['active'])
        self.assertEqual(self.run_script().stdout, '')
        self.assertEqual(self.run_script(payload={**self.payload, 'cwd': str(other)}).stdout, '')
        self.assertTrue(json.loads(self.command('status', session='session-b').stdout)['active'])

    def test_subagent_never_creates_state(self):
        self.assertEqual(self.run_script(payload={**self.payload, 'agent_id': 'worker-1'}).stdout, '')
        self.assertFalse((self.root / 'bestpaper-reminder-v1').exists())

    def test_disarm_persists_and_explicit_arm_resumes_without_reset(self):
        self.run_script()
        self.command('disarm')
        self.assertFalse(self.status()['active'])
        self.assertEqual(self.run_script(['--interval-seconds', '0.01']).stdout, '')
        self.command('arm')
        first = self.status()
        self.assertTrue(first['active'])
        self.command('arm')
        self.assertEqual(self.status()['last_reminder_at'], first['last_reminder_at'])
        self.assertEqual(self.run_script().stdout, '')

    def test_user_prompt_pauses_only_active_reminder(self):
        self.run_script()
        payload = {**self.payload, 'hook_event_name': 'UserPromptSubmit'}
        result = self.run_script(payload=payload)
        context = json.loads(result.stdout)['hookSpecificOutput']
        self.assertEqual(context['hookEventName'], 'UserPromptSubmit')
        self.assertIn('arm', context['additionalContext'])
        self.assertFalse(self.status()['active'])
        self.assertEqual(self.run_script(payload=payload).stdout, '')
        self.assertEqual(self.run_script().stdout, '')

    def test_session_end_is_silent_and_stays_disarmed(self):
        self.run_script()
        result = self.run_script(payload={**self.payload, 'hook_event_name': 'SessionEnd'})
        self.assertEqual(result.stdout, '')
        self.assertFalse(self.status()['active'])
        self.assertEqual(self.run_script().stdout, '')

    def test_bad_input_never_blocks_or_arms(self):
        for raw in ['{', '{}', '[]', '{"session_id":"s","cwd":"relative","hook_event_name":"PostToolBatch"}']:
            result = self.run_script(raw=raw)
            self.assertEqual(result.stdout, '')
            self.assertTrue(result.stderr)
        self.assertFalse((self.root / 'bestpaper-reminder-v1').exists())

    def test_corrupt_state_is_not_replaced_or_claimed_active(self):
        self.run_script()
        state = next(self.root.glob('bestpaper-reminder-v1/*.json'))
        state.write_text('{broken', encoding='utf-8')
        result = self.run_script()
        self.assertEqual(result.stdout, '')
        self.assertTrue(result.stderr)
        self.assertEqual(state.read_text(encoding='utf-8'), '{broken')

    def test_stop_continues_after_corrupt_session_state(self):
        for stop in ('disarm', 'UserPromptSubmit', 'SessionEnd'):
            for corrupt_current in (False, True):
                with self.subTest(stop=stop, corrupt_current=corrupt_current):
                    session = f'{stop}-{corrupt_current}'
                    old = self.root / session
                    old.mkdir()
                    files_before = set(self.root.glob('bestpaper-reminder-v1/*.json'))
                    self.command('arm', session=session, cwd=old)
                    self.command('arm', session=session)
                    files = set(self.root.glob('bestpaper-reminder-v1/*.json')) - files_before
                    current = next(p for p in files if json.loads(p.read_text(encoding='utf-8'))['active'])
                    previous = next(p for p in files if p != current)
                    corrupt, valid = (current, previous) if corrupt_current else (previous, current)
                    valid_state = json.loads(valid.read_text(encoding='utf-8'))
                    valid_state['active'] = True
                    valid.write_text(json.dumps(valid_state), encoding='utf-8')
                    corrupt.write_text('{broken', encoding='utf-8')
                    self.command('arm', session=session + '-other')
                    if stop == 'disarm':
                        result = self.command(stop, session=session)
                    else:
                        result = self.run_script(payload={**self.payload, 'session_id': session,
                                                          'hook_event_name': stop})
                    self.assertFalse(json.loads(valid.read_text(encoding='utf-8'))['active'],
                                     '损坏状态不能阻止正常状态停用')
                    self.assertEqual(corrupt.read_text(encoding='utf-8'), '{broken')
                    self.assertEqual(result.stdout, '', '未核实全部状态时不能输出停用成功')
                    self.assertIn(str(corrupt), result.stderr)
                    self.assertIn('停用未全部确认', result.stderr)
                    self.assertTrue(json.loads(self.command('status', session=session + '-other').stdout)['active'])
                    self.assertEqual(self.command('arm', session=session).stdout, '')
                    self.assertEqual(self.run_script(payload={**self.payload, 'session_id': session}).stdout, '')
                    self.assertFalse(json.loads(valid.read_text(encoding='utf-8'))['active'])
                    self.assertEqual(corrupt.read_text(encoding='utf-8'), '{broken')
                    # 坏文件移除后，正常状态也不能恢复投递。
                    corrupt.unlink()
                    result = self.run_script(['--interval-seconds', '0.01'], payload={
                        **self.payload, 'session_id': session, 'cwd': valid_state['cwd']})
                    self.assertEqual(result.stdout, '')

    def test_missing_prompt_does_not_claim_armed_or_delivered(self):
        self.prompt.unlink()
        result = self.run_script()
        self.assertEqual(result.stdout, '')
        self.assertTrue(result.stderr)
        self.assertFalse((self.root / 'bestpaper-reminder-v1').exists())
        self.prompt.write_text('restored', encoding='utf-8')
        self.run_script()
        before = self.status()
        self.prompt.unlink()
        result = self.run_script(['--interval-seconds', '0.01'])
        self.assertEqual(result.stdout, '')
        self.assertTrue(result.stderr)
        self.assertEqual(self.status()['last_reminder_at'], before['last_reminder_at'])


if __name__ == '__main__':
    unittest.main()
