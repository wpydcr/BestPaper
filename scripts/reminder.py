"""BestPaper 当前主会话的工具边界提醒，无后台定时进程。"""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import tempfile
import time


PROMPT = Path(__file__).resolve().parent.parent / 'references/runtime/reminder.md'


def emit(event, text):
    print(json.dumps({'hookSpecificOutput': {
        'hookEventName': event, 'additionalContext': text}}, ensure_ascii=False))


def read_prompt():
    text = PROMPT.read_text(encoding='utf-8-sig').strip()
    if not text:
        raise ValueError('提醒正文为空')
    return text


def state_path(session_id, cwd):
    if not isinstance(session_id, str) or not session_id.strip():
        raise ValueError('缺少 session_id')
    if '${' in session_id:
        raise ValueError('session_id 含未展开的占位符')
    if not isinstance(cwd, str) or not cwd.strip() or not os.path.isabs(cwd):
        raise ValueError('缺少绝对 cwd')
    normalized = os.path.normcase(os.path.realpath(cwd))
    prefix = hashlib.sha256(session_id.encode()).hexdigest()
    key = prefix + '-' + hashlib.sha256(normalized.encode()).hexdigest()
    return Path(tempfile.gettempdir()) / 'bestpaper-reminder-v1' / (key + '.json'), normalized


def load(path, session_id, cwd=None):
    if not path.exists():
        return None
    state = json.loads(path.read_text(encoding='utf-8'))
    if (not isinstance(state, dict) or state.get('session_id') != session_id
            or not isinstance(state.get('cwd'), str) or not os.path.isabs(state['cwd'])
            or (cwd is not None and state['cwd'] != cwd) or type(state.get('active')) is not bool
            or type(state.get('last_reminder_at')) not in (int, float)
            or not math.isfinite(state['last_reminder_at']) or state['last_reminder_at'] < 0):
        raise ValueError('提醒状态损坏或身份不符')
    return state


def save(path, state):
    path.parent.mkdir(parents=True, exist_ok=True)
    # 临时文件和目标位于同一目录，替换时不会留下半写入 JSON。
    fd, temporary = tempfile.mkstemp(dir=path.parent, suffix='.tmp')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump(state, stream, ensure_ascii=False)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def pause_session(states, keep=None):
    changed = False
    for path, state in states.items():
        if path != keep and state['active']:
            state['active'] = False
            save(path, state)
            changed = True
    return changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', nargs='?', choices=['hook', 'arm', 'disarm', 'status'], default='hook')
    parser.add_argument('--session-id')
    parser.add_argument('--cwd')
    parser.add_argument('--interval-seconds', type=float, default=1800)
    args = parser.parse_args()
    try:
        if not math.isfinite(args.interval_seconds) or args.interval_seconds <= 0:
            raise ValueError('间隔必须是正数')
        event = None
        session_id, cwd = args.session_id, args.cwd
        if args.command == 'hook':
            payload = json.load(sys.stdin)
            if not isinstance(payload, dict):
                raise ValueError('hook 输入必须为对象')
            if 'agent_id' in payload:
                return
            session_id, cwd = payload.get('session_id'), payload.get('cwd')
            event = payload.get('hook_event_name')
        path, normalized = state_path(session_id, cwd)
        prefix = path.name.split('-')[0] + '-'
        now = time.time()
        if args.command == 'disarm' or event in ('UserPromptSubmit', 'SessionEnd'):
            paths = list(path.parent.glob(prefix + '*.json'))
            if event != 'UserPromptSubmit' and path not in paths:
                paths.append(path)
            changed, failed, current = False, False, None
            # 停用逐文件处理：坏状态不能阻止其他已验证状态撤销授权。
            for item in paths:
                try:
                    state = load(item, session_id, normalized if item == path else None)
                    if state is None:
                        if item != path or event == 'UserPromptSubmit':
                            continue
                        state = {'session_id': session_id, 'cwd': normalized,
                                 'active': False, 'last_reminder_at': now}
                        save(item, state)
                    elif state['active']:
                        state['active'] = False
                        save(item, state)
                        changed = True
                    if item == path:
                        current = state
                except (OSError, ValueError, TypeError) as error:
                    failed = True
                    print(f'BestPaper reminder: 停用未全部确认；{item}；'
                          f'{type(error).__name__}：{error}', file=sys.stderr)
            if failed:
                return
            if args.command == 'disarm':
                print(json.dumps(current, ensure_ascii=False))
            elif event == 'UserPromptSubmit' and changed:
                emit(event, f'新消息已暂停旧论文提醒；当前 session_id={session_id}；cwd={cwd}。'
                     '若仍是同一已授权论文任务请 arm，其他任务保持停用。')
            return
        # 只读取本会话状态；项目改变不能产生新的隐式授权。
        states = {item: load(item, session_id) for item in path.parent.glob(prefix + '*.json')}
        state = states.get(path)
        if state is not None and state['cwd'] != normalized:
            raise ValueError('提醒状态身份不符')
        if args.command == 'status':
            print(json.dumps(state or {'session_id': session_id, 'cwd': normalized,
                                       'active': False, 'last_reminder_at': None}, ensure_ascii=False))
            return
        if args.command == 'arm':
            read_prompt()
            pause_session(states, keep=path)
            if not state or not state['active']:
                state = {'session_id': session_id, 'cwd': normalized, 'active': True, 'last_reminder_at': now}
                save(path, state)
            print(json.dumps(state, ensure_ascii=False))
            return
        if event != 'PostToolBatch':
            if event is None:
                raise ValueError('缺少 hook_event_name')
            return
        if state is None:
            if states:
                return
            read_prompt()
            state = {'session_id': session_id, 'cwd': normalized, 'active': True, 'last_reminder_at': now}
            save(path, state)
            emit(event, f'BestPaper 提醒已启用：session_id={session_id}；cwd={cwd}。'
                 f'每满 {args.interval_seconds:g} 秒，在下一工具批结束时提醒；这不是精确定时器。')
        elif state['active'] and now - state['last_reminder_at'] >= args.interval_seconds:
            text = read_prompt()
            state['last_reminder_at'] = now
            save(path, state)
            emit(event, text)
    except (OSError, ValueError, TypeError) as error:
        # hook 故障只诊断，不阻断用户工具，也不伪报启用或投递成功。
        print(f'BestPaper reminder: {type(error).__name__}；未启用或投递新提醒。', file=sys.stderr)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    main()
