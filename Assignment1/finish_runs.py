from pathlib import Path
import ast
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parent
E=ROOT/'evidence'
M=ROOT/'materials/csic30216-fall26-assignment1'

def block(key):
    return re.findall(r'```python\s*\n(.*?)```',(E/f'{key}_response.md').read_text(encoding='utf-8'),re.S)[0]

def replace_fn(src, name, replacement):
    tree=ast.parse(src)
    fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==name)
    lines=src.splitlines(keepends=True)
    new=''.join(lines[:fn.lineno-1])+replacement.rstrip()+'\n'+''.join(lines[fn.end_lineno:])
    ast.parse(new)
    return new

def run_snapshot(name, tm, ms):
    d=ROOT/'completed' if name=='final' else E/name
    d.mkdir(exist_ok=True)
    for f in ('check_my_work.py','utils.py','CONVENTIONS.md'):
        shutil.copy2(M/f,d/f)
    ast.parse(tm); ast.parse(ms)
    (d/'task_manager.py').write_text(tm,encoding='utf-8')
    (d/'my_solutions.py').write_text(ms,encoding='utf-8')
    out=subprocess.run([sys.executable,'-X','utf8','check_my_work.py'],cwd=d,capture_output=True,text=True,encoding='utf-8')
    (d/'checker_stdout.txt').write_text(out.stdout,encoding='utf-8')
    (d/'checker_stderr.txt').write_text(out.stderr,encoding='utf-8')
    (d/'run.json').write_text(json.dumps({'time_utc':datetime.now(timezone.utc).isoformat(),'command':[sys.executable,'-X','utf8','check_my_work.py'],'exit_code':out.returncode,'checker_sha256':hashlib.sha256((d/'check_my_work.py').read_bytes()).hexdigest()},indent=2),encoding='utf-8')
    print(name, re.search(r'\d+ passed,.*',out.stdout).group())
    return out

base=(M/'task_manager.py').read_text(encoding='utf-8')
for n in (1,2,3):
    run_snapshot(f'p2_rewrite_{n}',base,block(f'p2_rewrite_{n}'))
for key in ('p1_cot','p1_step'):
    run_snapshot(key,replace_fn(base,'get_overdue_tasks',block(key)),(M/'my_solutions.py').read_text(encoding='utf-8'))
for key in ('p1_zero','p1_revision'):
    run_snapshot(key,base,block(key))
run_snapshot('p1_few',replace_fn(base,'calculate_completion_rate',block('p1_few')),(M/'my_solutions.py').read_text(encoding='utf-8'))
tm=replace_fn(base,'get_overdue_tasks',block('p1_cot'))
tm=replace_fn(tm,'calculate_completion_rate',block('p1_few'))
ms='\n\n'.join(block(k).rstrip() for k in ('p1_revision','p2_rewrite_1','p2_rewrite_2','p2_rewrite_3'))+'\n'
out=run_snapshot('final',tm,ms)
assert not out.stderr and '[FAIL]' not in out.stdout and '[skip]' not in out.stdout and '[warn]' not in out.stdout
print(out.stdout)
