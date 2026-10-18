from pathlib import Path
import json,re
E=Path(__file__).resolve().parent/'evidence'
def fp(s):
    h=2166136261
    for c in s.replace('\r','').strip():
        h=((h^ord(c))*16777619)&0xffffffff
    return f'{h:08x}'
d=json.loads((E/'browser_fingerprints.json').read_text())
for k,v in d['prompt_fingerprints'].items():
    got=fp((E/f'{k}_prompt.txt').read_text(encoding='utf-8'))
    assert got==v,(k,got,v)
for row in d['code_fingerprints']:
    blocks=re.findall(r'```python\s*\n(.*?)```',(E/f'{row["name"]}_response.md').read_text(encoding='utf-8'),re.S)
    got=list(map(fp,blocks))
    assert got==row['codes'],(row['name'],got,row['codes'])
print('PASS: all 12 prompt payloads and all 13 Python blocks match browser-derived fingerprints (outer whitespace normalized).')
