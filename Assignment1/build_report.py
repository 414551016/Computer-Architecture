from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parent
E=ROOT/'evidence'
OUT=ROOT/'assignment_1_414551016_劉順松.md'
sources=json.loads((E/'conversation_sources.json').read_text())

def read(p): return p.read_text(encoding='utf-8-sig')
def fence(text,lang='text'):
    n=max([len(m.group()) for m in re.finditer(r'`+',text)]+[2])+1
    ticks='`'*max(4,n)
    return f'{ticks}{lang}\n{text.rstrip()}\n{ticks}\n'
def prompt(key): return fence(read(E/f'{key}_prompt.txt'))
def response(key): return fence(read(E/f'{key}_response.md'))
def checker(key): return fence(read(E/key/'checker_stdout.txt'))
def source(key): return f'對話來源：[Gemini 實際對話]({sources[key]})。\n'
def record(key):
    return '**Prompt (verbatim)**\n\n'+prompt(key)+'\n**Full model response**\n\n'+response(key)+'\n'+source(key)

reflections={
'p1_cot':'這個提示要求先追蹤執行，回答因此把錯誤定位到 `None < current_date`，而不只給出修正程式。修正把 `is not None` 放在日期比較之前，該版本通過官方 Task 1 的 4 項檢查；它沒有改變「今天到期不算逾期」的原本語意。',
'p1_step':'Step-back 回答先說明可選日期的型別限制與短路求值，再套用到函式，讓修正有可重用的一般原則。它的實際判斷條件與逐步分析版本相同，也通過 Task 1 的 4 項檢查，因此這次增加的是概念說明，沒有證據顯示功能正確性更高。',
'p1_zero':'在未提供範例與推理框架的情況下，完整規格已使回答使用優先級排名、日期鍵與 `sorted` 產生新的清單，通過官方 Task 2 的 5 項檢查。以二元日期鍵區分有日期與無日期，也讓補充測試中的實際 `date.max` 排在 `None` 前面；這顯示本次清楚的規格已足以得到正確實作。',
'p1_revision':'具體批評逐項檢查優先級、缺日期、穩定排序與不修改輸入，並明確承認它做的是程式檢視、不是已執行測試。初稿與修訂版都通過官方 5 項排序檢查及額外的 `date.max` 案例，因此修訂的收益是移除有效輸入前提下多餘的預設值與日期匯入，不能宣稱它修好了原本不存在的功能錯誤。',
'p1_few':'兩份指定範例引導回答採用一行摘要、`Args:` 與 `Returns:` 的一致結構，並正確說明回傳 0.0 到 1.0 的比例，以及空清單回傳 0.0。官方文件檢查通過，另以 AST 比對確認只有新增 docstring、未更動計算邏輯；但因提示也明確指定了格式，不能把格式一致完全歸因於範例本身。',
}

parts=['''# **Assignment 1:** **Technique Practice and Prompt Diagnosis**

*Name:* 劉順松  
*Student ID:* 414551016

> 閱讀狀態：程式、提示實驗與測試均已完成；本文件的反思與診斷由 Codex 依實際紀錄協助起草，需由本人閱讀確認。三處 Personal connection 已依本人指示採用最後提出的具體經驗版本。

實驗日期：2026-10-18（Asia/Taipei）。生成工具為 Google Gemini，畫面模式標示 **Flash**；介面未揭露精確後端模型版本或溫度，不推測版本。提示詞使用英文，分析使用繁體中文。

原始三題各自使用新對話，只提供作業公開模組與原始問題，未提供團隊規範、工具實作、檢查器或作者意圖；取得三題回覆後才閱讀規範與工具。使用的 PDF／網頁模組與 E3 模組僅排版不同，已確認 Python AST 相同。改寫各用另一個新對話；Self-correction 則保留同一對話的三輪。所有程式區塊均已與瀏覽器擷取內容比對。

---

## **Part 1 — Deliberate Technique Practice (50 pts)**

### Task 1 — Debug get\\_overdue\\_tasks (20 pts)

#### **Chain-of-Thought (10 pts)**
''',record('p1_cot'),'\n**Reflection (2–3 sentences)**\n\n'+reflections['p1_cot'],
'\n\n#### **Step-back (10 pts)**\n\n',record('p1_step'),'\n**Reflection (2–3 sentences)**\n\n'+reflections['p1_step'],
'\n\n---\n\n### Task 2 — Build sort\\_tasks\\_by\\_priority (20 pts)\n\n#### **Zero-shot (10 pts)**\n\n',record('p1_zero'),'\n**Reflection (2–3 sentences)**\n\n'+reflections['p1_zero'],
'\n\n#### **Self-correction (10 pts)**\n\n零樣本回答直接作為本三輪實驗的第一輪，以下重列原文以保留完整流程。\n']
for label,key in [('Turn 1 — Generation prompt and full response','p1_zero'),('Turn 2 — Critique prompt and full response','p1_critique'),('Turn 3 — Revision prompt and full response','p1_revision')]:
    parts += [f'\n**{label}**\n\n',record(key)]
parts += ['\n**Reflection (2–3 sentences)**\n\n'+reflections['p1_revision'],
'\n\n---\n\n### Task 3 — Document calculate\\_completion\\_rate (10 pts)\n\n#### Few-shot (10 pts)\n\n',record('p1_few'),'\n**Reflection (2–3 sentences)**\n\n'+reflections['p1_few'],
'''

---

## Part 2 — Prompt Diagnosis and Rewrite (50 pts)

**測試讀法。** 每一題的原始版與改寫版在獨立資料夾執行原封不動的 `python check_my_work.py`。為了隔離問題，資料夾只安裝該題函式，`task_manager.py` 保留老師原始版本；所以完整輸出中其他題目的 SKIP 與 Task 1 已知錯誤，不能算成目前這題的失敗。第二題的頂層匯入錯誤會讓整個 `my_solutions.py` 無法載入，因此它造成多個區塊報 FAIL，根因仍只有該匯入問題。最後另有整合版全部測試。

三題的原始版皆有該題失敗項目，沒有觸發「全部通過時額外重跑兩次」的規則。三題都直接提供了程式，沒有只提問而不寫程式的情況；第二題在提供程式後提出可調整介面的追問，已一併保存。
''']

failure={
1:'缺少團隊規範所造成的介面與資料結構不相容：找不到父任務時回傳 `False` 而不是拋出 `TaskError`，成功時回傳 `True` 而不是原清單，子任務也缺少 `due_date` 與繼承的 `priority`。官方該題結果為 3 PASS、3 FAIL；其中標題正規化的 PASS 是檢查器盲點，補充實驗確認該程式其實沒有正確匹配。',
2:'未取得工具內容就猜測函式介面：原始程式執行 `from utils import format_date`，但老師提供的工具實際是 `due_label(due, today)`，因此發生 `ImportError`，整個解答模組無法載入。模型已明說這是它的假設，所以應描述為「有揭露但未驗證的工具介面猜測」，不能說它宣稱已讀取 `utils.py`。',
3:'把未定義的「urgent」自行縮限為未完成且今天或以前到期，遺漏未來 1～3 天到期的非高優先任務，也遺漏較晚到期或未指定日期的高優先任務。官方該題為 6 PASS、2 FAIL、1 SKIP；排序檢查因集合不正確而跳過，不能把它寫成已驗證排序失敗。',
}
mechanism={
1:'Week 5 的 Context 與 implicit assumptions 說明：模型只能依看到的背景推測專案慣例；原提示詞沒有給它任務錯誤類別、回傳契約與子任務欄位。回覆採用布林成功／失敗值，與已提供模組中的 `mark_complete` 模式相似，但僅憑輸出不能證明它內部一定模仿該函式。改寫把五項規範轉成明確 constraints，修正後該題 6 項全數通過；這是補足資訊後的觀察，並非任意換字就改善的證明。',
2:'Week 6 第 27、32 頁討論 plausible-but-unsupported 輸出與捏造函式介面：常見名稱看似合理，但不能證明私人程式庫真的提供它。這次模型在缺少 context 時以 `format_date` 補空缺，實際匯入失敗提供了外部驗證；改寫透過 grounding 提供真實 `due_label` 邏輯及呼叫規則，四項功能檢查全部通過。原始程式另有大寫優先級及自行產生 "No due date" 的靜態差異，但因模組未載入，不能宣稱原始測試已執行到這兩個分支。',
3:'Week 5 的 Task、Constraints 與 specification-before-generation 適用於此題：原提示詞省略了可以逐項驗證的選取條件與排序規則，模型便自行設定 `due_date <= today`。改寫把條件拆成「未完成 AND（高優先 OR 截止日 <= today+3 天）」並指定跨優先級依日期排序及不修改輸入，九項檢查全數通過。官方檢查器明確納入剛好第 3 天、排除第 4 天的非高優先任務，所以改寫使用這個明確邊界；沒有做多組同義改寫比較，因此不把本次結果稱為已證實的 prompt sensitivity。',
}
personal_connections = {
1: '我曾請 AI 幫忙新增程式功能，卻只描述「要做什麼」，沒有說明原有程式要求的回傳格式；例如，呼叫端需要取得更新後的清單，AI 卻只回傳 `True` 表示成功，導致功能看似完成，接到其他程式時卻無法按預期使用，這與本題缺少團隊規範的情況相似。',
2: '我曾請 AI 使用現有工具協助撰寫程式，卻沒有提供工具檔案的內容；例如，AI 寫出一個名稱看起來合理的日期格式化函式，我照著執行後才發現無法匯入，檢查原始檔案才知道實際函式名稱不同，讓我理解不能把 AI 猜測的介面直接當成已確認的事實。',
3: '我曾請 AI 幫忙安排多項作業的完成順序，只說「先處理緊急的」，卻沒有說明截止日期、重要程度與預估所需時間；例如，AI 把明天到期的小作業排在最前面，卻把幾天後到期但需要較長準備時間的大報告排到後面，讓我發現必須明確說明排序依據，AI 才能更貼近我的需求。',
}
for n in (1,2,3):
    original=f'p2_original_{n}'; rewritten=f'p2_rewrite_{n}'
    parts += [f'\n### **Prompt {n} (15 pts)**\n\n**Failure mode**\n\n{failure[n]}\n\n**Mechanism**\n\n{mechanism[n]}\n\n**Rewritten prompt**\n\n',prompt(rewritten),
    '\n**Evidence — original prompt output**\n\n實際送出的原始提示（含完整模組）：\n\n',prompt(original),'\n完整模型回答：\n\n',response(original),source(original),'\n官方檢查器完整輸出：\n\n',checker(original)]
    if n==1:
        parts += ['\n補充實驗（非官方檢查器；未更改官方測試）：\n\n',fence(read(E/'supplement_original1.txt'))]
    parts += ['\n**Evidence — rewritten prompt output**\n\n',response(rewritten),source(rewritten),'\n官方檢查器完整輸出：\n\n',checker(rewritten),
    f'\n**Personal connection (one sentence)**\n\n{personal_connections[n]}\n\n---\n']

parts += ['''
# **AI Usage Log**

| 工具 | 請求與使用方式 | 人工確認狀態 |
|---|---|---|
| Codex | 協助讀取作業、整理知識地圖、設計提示詞、操作瀏覽器、保存回覆、整合程式、執行官方及補充測試、依證據起草反思與診斷並套用範本。 | 學生提供姓名、學號與材料，明確授權將作業程式及必要規範送至 Gemini；學生亦確認曾經歷三類提示失敗，並指定採用最後提出的三段具體經驗，由 Codex 更新全文；反思與診斷仍需本人閱讀理解。 |
| Google Gemini（介面 Flash 模式） | 執行 12 輪生成：Part 1 共 6 輪（零樣本同時是 self-correction 的第一輪），Part 2 共 6 輪；各實驗對話連結附於對應紀錄。 | 未提供精確後端版本；未偽稱控制溫度或取得模型隱藏推理。 |
| Python 3.12.7 | 本機執行原始官方檢查器、補充單元測試與 AST／證據完整性檢查。 | 程式執行證據已保存；不以模型自評替代實測。 |

沒有代造模型回答或測試結果。原始失敗、模型多提供的建議與範例、批評中的 Markdown 格式問題均保留；程式複製時僅選取實作區塊，不把示範使用程式誤當解答。最終 `task_manager.py` 採用逐步分析修正與 Few-shot docstring，`my_solutions.py` 採用排序修訂版與三題改寫版。三句個人經驗採用本人指定的最後版本，描述回傳格式不符、猜錯日期函式及誤排作業順序；未添加專案名稱、日期或工具版本；尚未上傳 E3。

## 附錄 A：整合驗證

| 驗證項目 | 實測結果 |
|---|---|
| 官方整合檢查 | 33 passed、0 failed、0 warnings、0 not started yet |
| 額外邊界與行為測試 | 8 tests，OK；包含實際新增子任務、日期極大值、穩定排序、工具呼叫、不修改輸入與文件不改邏輯 |
| 逐字提示與程式證據核對 | 12 份提示與 13 個 Python 區塊符合瀏覽器擷取指紋；只忽略區塊首尾空白 |
| 官方檢查器完整性 | 所有實驗資料夾與最終資料夾使用相同原始檢查器 SHA-256 |

通過測試代表已驗證的案例通過，並非滿分保證，也不代表已涵蓋所有可能輸入。例如日期接近 Python 可表示範圍上限時的加法溢位，並不在本次官方需求測試內。

完整整合輸出：

''',fence(read(ROOT/'completed/checker_stdout.txt')),'\n補充測試輸出：\n\n',fence(read(ROOT/'completed/additional_tests.txt')),
'''
## 附錄 B：課程概念依據

- Week 5 `week5-prompt-engineer-1-261005.pdf`：第 34 頁（role/context/task/format/constraints）、第 36–37 頁（模型不知道的背景與慣例）、第 40 頁（implicit assumptions）、第 44–45 頁（specification 與 evaluation）。
- Week 6 `week6-prompt-engineer-2-261012.pdf`：第 27 頁（unsupported／false 的差異）、第 32 頁（不存在的函式介面）、第 34 頁（外部驗證）。
- 本次實作依據 E3 原始範本、`CONVENTIONS.md`、`utils.py` 與未修改的 `check_my_work.py`，並以作業網頁及 PDF 交叉核對要求。
''']
report='\n'.join(parts)
OUT.write_text(report,encoding='utf-8')
# Confirm the template's heading sequence is preserved outside quoted responses.
template=read(ROOT/'materials/csic30216-fall26-assignment1/assignment_1_studentid_name.md')
headings=re.findall(r'^#{1,6} .*$',template,re.M)
for h in headings: assert h in report,repr(h)
for key in sources:
    assert read(E/f'{key}_prompt.txt').rstrip() in report,key
    assert read(E/f'{key}_response.md').rstrip() in report,key
for n in (1,2,3):
    for kind in ('original','rewrite'):
        assert read(E/f'p2_{kind}_{n}'/'checker_stdout.txt').rstrip() in report
reference=hashlib.sha256((ROOT/'materials/csic30216-fall26-assignment1/check_my_work.py').read_bytes()).hexdigest()
for p in ROOT.rglob('check_my_work.py'):
    assert hashlib.sha256(p.read_bytes()).hexdigest()==reference,str(p)
manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and p.suffix in ('.md','.txt','.py','.json') and p.name!='sha256_manifest.json' and '__MACOSX' not in str(p) and '__pycache__' not in str(p)}
(E/'sha256_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Created {OUT.name}: {len(report):,} characters; template headings, all 12 prompts, all responses, and all six Part 2 checker logs verified.')
