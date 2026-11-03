"""Single declared 180-second author execution; never an automatic retry."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import subprocess
import sys
import time

HERE = (_J_PROGRAM / 'main.py').parent


# Public metadata uses logical locators; actual subprocess/file paths stay resolved.
# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def _record_path(value):
    try:
        return Path(value).resolve().relative_to(_J_ROOT).as_posix()
    except ValueError:
        return '<external-location>'


def _record_command(values):
    result = []
    for value in values:
        option, separator, argument = value.partition('=')
        if separator and option.startswith('-') and Path(argument).is_absolute():
            result.append(option + '=' + _record_path(argument))
        else:
            result.append('python' if value == sys.executable else
                          _record_path(value) if Path(value).is_absolute() else value)
    return result


def save(name, value):
    (((_J_PROGRAM if name in ('main.py', 'readme.md', 'verify.py', 'worker.py') else _J_OUTPUT) / name)).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def main():
    command = [sys.executable, '-B', '-X', 'utf8', str(_J_PROGRAM / 'worker.py')]
    try:
        process = subprocess.run(command, cwd=_J_PROGRAM, timeout=180,
                                 text=True, encoding="utf-8", capture_output=True)
    except subprocess.TimeoutExpired as error:
        (_J_OUTPUT / "failure.json").write_text(
            json.dumps({"status": "timeout", "completed_output": False}) + "\n", encoding="utf-8")
        print(str(error), file=sys.stderr)
        return 124
    if process.stdout:
        print(process.stdout, end="")
    if process.stderr:
        print(process.stderr, end="", file=sys.stderr)
    if process.returncode:
        return process.returncode
    payload = json.loads((_J_OUTPUT / 'result.json').read_text(encoding="utf-8"))
    assert payload['status'] == 'complete' and [r['n'] for r in payload['results']] == [6,7,8,9,10]
    return 0



if __name__ == "__main__":
    raise SystemExit(main())
