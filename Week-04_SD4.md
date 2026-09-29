Prompt：請說明本教學重點內容及你的看法，最後以250字內總結
### Week 4 課堂逐字稿
這份教材主要探討先進的電腦處理器設計，特別聚焦於亂序執行與超純量架構的運作機制。課程核心圍繞四大主題展開：包括允許指令不按順序完成的亂序處理器、處理條件跳躍的預測與推測執行、消除名稱相依性的暫存器命名技術，以及處理記憶體存取順序的記憶體消歧義。透過介紹如重定序緩衝區和發布佇列等硬體結構，教材詳細解析了處理器如何在維持程式正確執行的同時，大幅提升指令的執行並行度與整體效能。

Prompt：請說明本教學重點內容：及你的看法，最後以250字內總結
### Week 4 課堂逐字稿

## slide：1 -2
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0001.jpg" width="49%">
  <img src="./Lecture/SD4/SD4_page-0002.jpg" width="49%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：2
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0002.jpg" width="50%">
</div>

這張簡報投影片的主題為亂序執行（Out-Of-Order, OOO）機制的重點複習（Recap: Out-Of-Order (OOO)），透過比較不同處理器架構與架構代號（如 I4、I2O2、I2O1、IO3、IO2I），分類說明指令在各階段為順序（In-Order, IO）或亂序（Out-Of-Order, OOO）執行，並列出實現該機制所需的硬體組件。
- 本教學重點內容：
  <br>投影片依照處理器流水線（Pipeline）的四大階段：前端（Frontend）、發射（Issue）、寫回（Writeback）與提交（Commit），展示了不同的架構演進與對應技術：
  - 流水線階段的執行順序模式：
    - 前端（Frontend）：所有架構皆保持順序（IO）處理，確保指令依序取出與解碼。
    - 發射（Issue）：早期或簡單架構（如 I4、I2O2、I2O1）採順序（IO）發射；支援動態排程的架構（如 IO3、IO2I）則採用亂序（OOO）發射。
    - 寫回（Writeback）：完全順序執行的架構（I4）採 IO 寫回；引進多管道或亂序執行的架構（I2O2、I2O1、IO3、IO2I）則支援 OOO 寫回。
    - 提交（Commit）：控制狀態更新。若要確保精確例外處理（Precise Interrupts/Exceptions），須採用 IO 提交（如 I4、I2O1、IO2I）；若允許 OOO 提交（如 I2O2、IO3），則控制相對簡化但例外處理較複雜。
  - 核心硬體支援組件：
    - Scoreboard（記分板）：用於追蹤資料依賴性與暫存器狀態，幾乎所有非純流水線架構皆需具備。
    - Issue Queue（發射佇列）：實現亂序發射（OOO Issue）的核心緩衝區。
    - Reorder Buffer, ROB（重排序緩衝區）：將亂序執行的結果重新按照程式原本順序（IO）提交的核心機制。
    - Store Buffer（儲存緩衝區）：確保記憶體寫入操作在正確時間點生效，避免記憶體存取衝突。
- 個人看法與分析：
  <br>這份複習表格精準地捕捉了電腦結構中性能優化與邏輯正確性之間的權衡（Trade-off）：
  - 漸進式的架構演變：從最基礎的 I4（純順序）到 IO2I（亂序發射/寫回，但順序提交），展現了 CPU 如何在提高指令平行度（ILP）的同時，維護程式邏輯的正確性。
  - ROB 的重要性：特別是比較 IO3 與 IO2I，關鍵差異在於 IO2I 引入了 Reorder Buffer (ROB) 與 Store Buffer。雖然兩者皆支援亂序發射與寫回，但 IO2I 能藉由 ROB 實現 In-Order Commit，這對於維護現代計算機的「精確例外（Precise Exceptions）」與記憶體一致性至關重要。
- 總結：
  <br>本頁複習了 CPU 亂序執行（OOO）架構的演進。所有架構前端均為順序（IO）處理，區別在於 Issue、Writeback 與 Commit 是否支援亂序（OOO）。實現動態排程需靠 Scoreboard 與 Issue Queue；而引進 Reorder Buffer (ROB) 與 Store Buffer 則是讓亂序執行的結果能「順序提交（IO Commit）」的關鍵技術。整體而言，這展示了現代 CPU 如何透過 ROB 兼顧高指令平行度（ILP）與精確例外處理的嚴謹設計。

## slide：3
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0003.jpg" width="50%">
</div>

這張投影片主題為 I4 架構的重點複習（Recap: I4），主要呈現經典的「多執行單元、固定流水線長度（Fixed Length Pipelines）」順序處理器架構設計。
- 本教學重點內容：
  - 流水線架構與執行流程：
    - 前端階段：包含 F（Fetch 取指） $\rightarrow$ D（Decode 解碼） $\rightarrow$ I（Issue 發射） 三個順序運行的階段。
    - 執行單元（Execution Units）：指令在發射（I）階段後，會分流至不同長度的固定執行管道：
      - X 管道（如算術邏輯單元 ALU）：經歷 $X_0 \rightarrow X_1 \rightarrow X_2 \rightarrow X_3$ 四個階段。
      - M 管道（如記憶體存取 Memory/Load-Store）：經歷 $M_0 \rightarrow M_1 \rightarrow M_2 \rightarrow M_3$ 四個階段。
      - Y 管道（如浮點數或複雜運算 FP/Complex）：經歷 $Y_0 \rightarrow Y_1 \rightarrow Y_2 \rightarrow Y_3$ 四個階段。
    - 寫回階段（Writeback）：所有執行管道的長度皆固定為 4 個階段，因此所有指令都會在相同的週期到達 W（Writeback） 階段順序寫回。
  - 暫存器與結構組件的操作時機：
    - ARF（Architectural Register File，架構暫存器檔案）：在 I 階段進行讀取（R），並在 W 階段進行寫入（W）。
    - SB（Scoreboard，記分板）：在 I 階段進行讀取與更新狀態（R/W，檢查資料依賴性與危害），並在 W 階段解除鎖定/清除狀態（W）。
- 個人看法與分析：
  - 「固定長度」的巧妙設計：I4 架構特別將所有執行管道（X、M、Y）統一設計為 4 個階段（$0 \sim 3$）。這種設計能保證先發射（Issue）的指令必定先到達寫回（Writeback）階段，從而在不需要 Reorder Buffer (ROB) 的情況下，天然地實現 In-Order Writeback 與 In-Order Commit。
  - 結構簡潔但效率受限：雖然簡化了精確例外（Precise Exceptions）與記分板（Scoreboard）的控制邏輯，但強迫所有執行單元湊滿相同延遲（Latency），可能會讓短延遲指令（如簡單加法）浪費等待時間，無法充分發揮硬體的最大效能。
- 總結：
  <br>I4 為典型的「順序發射、固定長度管道、順序寫回」處理器架構。指令經 F、D、I 階段後，分流至長度同為 4 階的 X、M、Y 執行管道，最終於 W 階段寫回。架構暫存器（ARF）與記分板（SB）均於 I 階段讀取/更新，並於 W 階段寫回/解鎖。由於所有管道長度固定，指令不會發生寫回順序顛倒（WAW/RAW 衝突少），能以極低代價確保順序提交與精確例外。此設計結構簡潔，但缺乏動態排程彈性。

## slide：4
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0004.jpg" width="50%">
</div>

這張投影片主題為 I2O2 架構的重點複習（Recap: I2O2），展示了「順序發射（In-Order Issue）、變長流水線（Variable Length Pipelines）、亂序寫回（Out-of-Order Writeback）」的處理器架構設計。
- 本教學重點內容：
  - 可變長度執行管道（Variable-Length Pipelines）：
    - 前端階段：保持 F（Fetch 取指） $\rightarrow$ D（Decode 解碼） $\rightarrow$ I（Issue 發射） 順序執行。
    - 不同延遲的執行管道：與 I4 的固定長度不同，I2O2 允許管道長度依指令需求優化：
      - X 管道（簡單運算/ALU）：僅需 1 階（ $X_0$）。
      - M 管道（記憶體存取/Memory）：需要 2 階（ $M_0 \rightarrow M_1$）。
      - Y 管道（複雜/浮點運算 FP）：需要 4 階（ $Y_0 \rightarrow Y_1 \rightarrow Y_2 \rightarrow Y_3$）。
  - 寫回（Writeback）與組件操作：
    - 亂序寫回（OOO Writeback）：後發射但延遲短的指令（例如走 X 管道）會比先發射但延遲長的指令（例如走 Y 管道）更早完成並進入 W 階段，造成寫回順序與程式順序不同。
    - ARF 與 SB 操作時機：
      - ARF（架構暫存器檔案）：於 I 階段讀取（R），完成時於 W 階段直接寫回（W）。
      - SB（Scoreboard，記分板）：於 I 階段讀取與更新（R/W），追蹤暫存器依賴性；於 W 階段清除狀態（W）。
- 內容看法與分析：
  - 效能提升的代價：I2O2 藉由取消「強迫所有管道等長」的限制，大幅降低了短延遲指令（如簡單算術 $X_0$）的等待時間，提高了執行效能與流水線利用率。
  - 引發 Writeback 衝突與亂序難題：
    - Structural Hazard & WAW Hazard：不同管道長度會導致多條指令可能在同一個週期同時爭搶 W 階段（ Write Port 衝突），或者後發射的指令比先發射的指令先寫回同一個暫存器。因此需仰賴 Scoreboard (SB) 進行嚴格檢查與發射阻擋。
    - 缺少精確例外處理（Lack of Precise Exceptions）：由於沒有 Reorder Buffer (ROB) 來暫存結果並重新排序，指令在 W 階段會直接修改 ARF。若長指令在執行途中發生例外，後續已寫回 ARF 的短指令無法撤銷（Rollback），這是此架構最大的缺陷。
- 總結：
  <br>I2O2 架構採用「順序發射、可變管道長度、亂序寫回」設計。其執行管道長度依功能而異（X管道1階、M管道2階、Y管道4階），使短延遲指令能提早完成，提升執行效率。暫存器 ARF 與記分板 SB 於 I 階段讀取/更新，並於 W 階段直接寫回/解鎖。然而，變長管道導致寫回順序顛倒（OOO Writeback），易產生 Writeback 衝突與 WAW 危害，且因缺乏 Reorder Buffer (ROB) 暫存結果，無法保障精確例外處理（Precise Exceptions）。

## slide：5
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0005.jpg" width="50%">
</div>

這張投影片主題為 過早提交點（Early Commit Point?），透過一段組合語言程式碼的時序圖（Pipeline Timing Diagram），深入探討在沒有 Reorder Buffer (ROB) 的架構下，過早將結果寫回/提交（Early Commit） 所引發的精確例外（Precise Exceptions）問題與流水線停頓（Stall）現象。
- 本教學重點內容：
  - 程式碼執行時序分析：
    - 指令 0（mul x1, x2, x3）：走長延遲管道（Y 管道），經歷 $Y_0 \rightarrow Y_1 \rightarrow Y_2 \rightarrow Y_3$。
    - 指令 1（addi x11, x10, 1）：走短延遲管道（X 管道），在 $X_0$ 執行完畢後立即進入 W 階段寫回。由於它比指令 0 更早完成並修改暫存器，形成了 Early Commit（過早提交）。
    - 指令 2（mul x5, x1, x4）：依賴指令 0 的結果（x1）。因為指令 0 還在 $Y$ 管道中執行，發射（Issue）階段必須卡住停頓（Stall） 3 個週期（I I I），直到資料準備就緒。
    - 指令 3 與 4（mul, addi）：受到前方指令 2 停頓的影響，分別被阻擋在解碼階段（D D D）與取指階段（F F F）。
  - 核心限制：限制了可支援的例外類型（Limits certain types of exceptions）：
    - 在指令 1 已經寫回 W（Commit）之後，如果前面的指令 0 在執行後半段（如 $Y_2$ 或 $Y_3$）突然觸發了硬體算術例外（如溢位）：
      - 指令 1 已經永久修改了架構暫存器 x11，無法回復（Rollback）。
      - 處理器無法將狀態還原到「指令 0 發生例外前」的正確樣子，這打破了精確例外（Precise Exception）的原則。
- 個人看法與分析：
  - 效能與正確性的矛盾（Early Commit 的副作用）：雖然允許短指令提前寫回可以釋放執行單元，但這會讓 CPU 的狀態陷入「未完成前指令，卻已提交後指令」的混亂狀態。
  - 引發全線阻塞（Cascading Stalls）：圖中可以清楚看到，因為 RAW（Data Hazard）資料依賴，長延遲指令（指令 0）會讓後續依賴它的指令（指令 2）卡在 I 階段，並進一步向上游擴散，導致整個前端（Decode、Fetch）完全癱瘓。這凸顯了僅靠 Scoreboard 缺乏動態排程（Issue Queue）與結果暫存（ROB）時的效能瓶頸。
- 總結：
  <br>本頁透過時序圖展示了無 ROB 亂序寫回架構中「過早提交（Early Commit）」的問題。長延遲指令 mul（指令0）仍在執行時，後方短指令 addi（指令1）已完成並寫回暫存器。若此時長指令於後續階段觸發例外，已改變的暫存器狀態無法復原，嚴重破壞精確例外處理（Precise Exceptions）。此外，資料依賴（RAW Hazard）導致後續指令卡在 I 階段，引發連鎖停頓（Stall）使前端癱瘓。這說明了引入 Reorder Buffer (ROB) 實現「順序提交」以維持狀態正確性的必要性。

## slide：6
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0006.jpg" width="50%">
</div>

這張投影片為課程行政事務宣佈（Course Admin），主要向學生交代當前課程作業與實驗的最新進度與釋出狀況。
- 本教學重點內容：
  - PS1 解答公佈（PS1 solutions are out）：問題集 1（Problem Set 1）的標準解答已經發布，供學生核對與複習。
  - PS2 作業出爐（PS2 is out）：問題集 2（Problem Set 2）已經正式勾選/發布，學生需開始著手撰寫。
  - Lab2 實驗出爐（Lab2 is out）：第二個實驗項目（Lab 2）也已同步釋出，學生需進行相關的硬體實作或模擬實驗。
- 個人看法與分析：
- 總結：
  <br>本頁為課程行政事項宣佈。主要告知學生三項最新動態：第一作業集（PS1）解答已公佈，同時正式釋出第二作業集（PS2）與第二個實驗（Lab2）。這反映出課程正緊密結合理論觀念（Problem Sets）與動手實作（Labs），要求學生在複習前階段觀念（如 OOO 與流水線）之餘，需同時投入新一輪的課後練習與實驗專案。

## slide：7
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0007.jpg" width="50%">
</div>

這張投影片為本堂課的議程/大綱（Agenda），揭示了本章節（或本日課程）的核心主題與後續研討方向。
- 本教學重點內容：
  - 當前聚焦主題（黑色粗體）：
    - 亂序執行處理器（Out-of-Order Processors）：目前正在進行講授的核心內容，著重於如何透過硬體動態排程打破指令發射與執行的順序限制。
  - 後續規劃主題（淡灰色）：
    - 推測執行與分支（Speculation and Branches）：探討分支預測（Branch Prediction）與推測性執行機制，解決控制危害（Control Hazards）。
    - 暫存器重新命名（Register Renaming）：透過實體暫存器將架構暫存器重新對映，以消除 WAW（寫後寫）與 WAR（讀後寫）等偽資料危害（False Data Hazards）。
    - 記憶體消歧義（Memory Disambiguation）：處理 Load 與 Store 指令在亂序執行時對相同記憶體位址的讀寫爭用問題。
- 個人看法與分析：
  - 完整呈現高階 CPU 架構四大核心：這四個主題正是現代高效能微架構（Microarchitecture）不可或缺的四大支柱。光有亂序執行（Out-of-Order）還不夠，必須搭配暫存器重命名消除偽危害、推測執行穿透分支障礙，以及記憶體消歧義確保記憶體存取安全，CPU 才能真正發揮出高平行度（ILP）。
  - 教學階梯式設計：淡灰色的項目設計清楚呈現了課程的邏輯遞進。先帶學生理解 OOO 的基礎概念與限制（如前幾頁所述的流水線與例外問題），再逐步引入更高級的硬體解決方案（如 Register Renaming）。
- 總結：
  <br>本頁為課程議程（Agenda）。目前進度聚焦於「亂序執行處理器（Out-of-Order Processors）」；後續將陸續探討三大進階技術：解決控制危害的「推測執行與分支」、消除偽資料危害的「暫存器重新命名」，以及處理記憶體存取衝突的「記憶體消歧義」。整體課程規劃嚴謹且具系統性，逐步帶領學生掌握現代高階 CPU 設計中提升指令平行度（ILP）與維持系統正確性的核心機制。

## slide：8
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0008.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：9
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0009.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：10
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0010.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：11
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0011.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：12
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0012.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：13
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0013.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：14
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0014.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：15
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0015.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：16
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0016.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：17
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0017.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：18
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0018.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：19
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0019.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：20
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0020.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：21
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0021.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：22
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0022.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：23
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0023.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：24
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0024.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：25
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0025.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：26
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0026.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：27
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0027.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：28
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0028.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：29
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0029.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：30
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0030.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：31
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0031.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：32
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0032.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：33
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0033.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：34
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0034.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：35
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0035.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：36
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0036.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：37
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0037.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：38
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0038.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：39
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0039.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：40
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0040.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：41
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0041.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：42
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0042.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：43
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0043.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：44
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0044.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：45
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0045.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：46
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0046.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：47
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0047.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：48
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0048.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：49
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0049.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：50
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0050.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：51
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0051.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：52
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0052.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：53
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0053.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：54
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0054.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：55
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0055.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：56
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0056.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：57
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0057.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：58
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0058.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：59
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0059.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：60
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0060.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：61
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0061.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：62
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0062.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：63
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0063.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：64
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0064.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：65
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0065.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：66
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0066.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：67
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0067.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：68
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0068.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：69
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0069.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：70
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0070.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：71
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0071.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：72
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0072.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：73
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0073.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：74
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0074.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：75
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0075.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：76
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0076.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：77
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0077.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：78
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0078.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：

## slide：79
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0079.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法與分析：
- 總結：
















