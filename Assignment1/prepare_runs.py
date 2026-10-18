"""Preserve model outputs and run the unmodified instructor checker in isolated folders."""
from pathlib import Path
import ast
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
MATERIALS = ROOT / 'materials' / 'csic30216-fall26-assignment1'
EVIDENCE = ROOT / 'evidence'

def blocks(name):
    return re.findall(r'```python\s*\n(.*?)```', (EVIDENCE / name).read_text(encoding='utf-8'), re.S)

def run_originals():
    for number in (1, 2, 3):
        dest = EVIDENCE / f'p2_original_{number}'
        dest.mkdir(exist_ok=True)
        for filename in ('task_manager.py', 'check_my_work.py', 'utils.py', 'CONVENTIONS.md'):
            shutil.copy2(MATERIALS / filename, dest / filename)
        # Only the implementation block is needed; optional examples and suggestions
        # remain unedited in the full response evidence.
        code = blocks(f'p2_original_{number}_response.md')[0]
        ast.parse(code)
        (dest / 'my_solutions.py').write_text(code, encoding='utf-8')
        result = subprocess.run([sys.executable, '-X', 'utf8', 'check_my_work.py'], cwd=dest, capture_output=True, text=True, encoding='utf-8')
        (dest / 'checker_stdout.txt').write_text(result.stdout, encoding='utf-8')
        (dest / 'checker_stderr.txt').write_text(result.stderr, encoding='utf-8')
        (dest / 'run.json').write_text(json.dumps({'time_utc':datetime.now(timezone.utc).isoformat(),'command':[sys.executable,'-X','utf8','check_my_work.py'],'exit_code':result.returncode,'checker_sha256':hashlib.sha256((dest/'check_my_work.py').read_bytes()).hexdigest()},indent=2), encoding='utf-8')
        print(f'ORIGINAL PROMPT {number}\n{result.stdout}{result.stderr}')

if __name__ == '__main__':
    run_originals()
