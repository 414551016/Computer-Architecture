import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'file:///C:/Users/LSS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/marked/lib/marked.esm.js';
const root=path.dirname(fileURLToPath(import.meta.url));
const input=fs.readFileSync(path.join(root,'assignment_1_414551016_劉順松.md'),'utf8');
const tokens=marked.lexer(input);
const code=tokens.filter(t=>t.type==='code');
const headings=tokens.filter(t=>t.type==='heading');
if (!headings.some(h=>h.text.includes('AI Usage Log'))) throw new Error('AI usage heading swallowed by fence');
if (!headings.some(h=>h.text.includes('附錄 B'))) throw new Error('Appendix missing');
const html=`<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><title>Assignment 1 — 劉順松 414551016</title><style>
body{margin:0;background:#f3f5f8;color:#17243a;font:16px/1.75 "Microsoft JhengHei",sans-serif}main{max-width:1050px;margin:32px auto;padding:40px;background:white;border-radius:12px}h1,h2,h3,h4{line-height:1.4;color:#173d65}h2{border-bottom:2px solid #dce6ef;padding-bottom:10px;margin-top:42px}pre{background:#f4f7fa;border:1px solid #dce3ea;border-radius:7px;padding:18px;white-space:pre-wrap;overflow-wrap:anywhere;font:13px/1.6 Consolas,monospace}code{font-family:Consolas,monospace}table{border-collapse:collapse;width:100%;margin:16px 0}th,td{border:1px solid #dbe1e8;padding:10px;text-align:left}th{background:#edf3f8}blockquote{border-left:5px solid #d69520;margin:18px 0;padding:8px 18px;background:#fff8e8}a{color:#16598d}hr{border:0;border-top:1px solid #dce3ea;margin:28px 0}@media(max-width:700px){main{margin:0;padding:18px}body{font-size:15px}}
</style><main>${marked.parse(input)}</main></html>`;
fs.writeFileSync(path.join(root,'evidence','report_preview.html'),html,'utf8');
console.log(JSON.stringify({headings:headings.map(h=>h.text),fencedBlocks:code.length,pendingPersonalConnections:(input.match(/【待本人填寫/g)||[]).length,preview:'evidence/report_preview.html'},null,2));
