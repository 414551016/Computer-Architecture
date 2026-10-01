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

這張投影片主題為 I2OI 架構（全名：In-order Frontend/Issue, Out-of-order Writeback, In-order Commit）。這是一種透過引入 Reorder Buffer (ROB) 與 Physical Register File (PRF / Future File)，成功解決前幾頁提到的「Early Commit 與精確例外（Precise Exceptions）」難題的關鍵架構。
- 本教學重點內容：
  - 流水線階段與核心運作（Pipeline Flow）：
    - 前端與發射（In-order Frontend/Issue）：F（Fetch） $\rightarrow$ D（Decode） $\rightarrow$ I（Issue） 保持順序執行。
    - 可變長度執行管道：包含 X（1階）、M（2階）、Y（4階）等不同延遲管道。
    - 亂序寫回（Out-of-order Writeback, W）：執行完畢後，指令結果會先寫入 PRF（實體暫存器檔案），同時在 ROB（重排序緩衝區） 中標記為已完成（Finished）。
    - 順序提交（In-order Commit, C）：依據程式原本順序，自 ROB 標頭（Head）順序將結果更新至 ARF（架構暫存器檔案）。
  - 各硬體組件的操作時機與分工：
    - ARF（Architectural Register File）：僅在 C 階段進行寫入（W），代表指令真正安全地退休（Commit）。
    - SB（Scoreboard）：於 I 階段讀取/更新（R/W），於 W 階段解除鎖定（W）。
    - PRF（Physical Register File / Future File）：於 I 階段讀取推測值（R），於 W 階段寫入執行結果（W）。
    - ROB（Reorder Buffer）：於 I 階段分配 Entry（R/W），於 W 階段更新完成狀態（W），於 C 階段讀取並釋放（R/W）。
    - FSB（Finished Store Buffer）：於 W 階段暫存已執行的 Store 資料（W），於 C 階段確定無例外後才真正寫入記憶體（R/W）。
- 個人看法與分析：
  - 成功解決精確例外（Precise Exceptions）：這張圖展現了電腦結構發展上的重要里程碑。藉由分離「寫回暫存結果（Writeback 至 PRF）」與「最終永久生效（Commit 至 ARF）」，就算執行過程是亂序的，也能在發生例外時直接丟棄 PRF 與 ROB 的推測狀態，精確地還原 ARF。
  - 為完全亂序執行（OOO Issue）鋪路：I2OI 雖然發射（Issue）階段仍是順序的（In-order），但它引入的 ROB、PRF 與 Store Buffer 機制，已經構建好了亂序執行所需的最後一道防線（In-order Commit）。後續只需在 I 階段前加上 Issue Queue，即可升級為現代完整的 OOO 處理器（如 IO2I）。
- 總結：
  <br>I2OI 架構結合了「順序發射、亂序寫回、順序提交」。其核心在於引入 ROB 與 PRF：指令於 I 階段分配 ROB 位置；執行完畢於 W 階段先將結果寫入 PRF 並標記 ROB（亂序寫回）；最後於 C 階段按程式原本順序將結果寫入 ARF（順序提交）。FSB 則確保 Store 指令在 Commit 前不修改記憶體。此設計徹底解決了過早提交造成的精確例外問題，為現代高階 CPU 的亂序執行奠定了重要基礎。

## slide：9
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0009.jpg" width="50%">
</div>

這張投影片的主題為 重排序緩衝區（Reorder Buffer, ROB）的硬體結構與運作機制，詳細解構了 ROB 作為環形佇列（Circular Queue）的欄位定義與指標運作方式。
- 本教學重點內容：
  - ROB 的內部欄位定義（Entry Fields）：
    - State（狀態）：記錄該指令目前的生命週期，共有三種狀態：Empty (-- )（空）、Pending (P)（執行中/等待中）、Finished (F)（已完成）。
    - S（Speculative Bit，推測位元）：標示該指令是否屬於推測執行的指令（例如位於尚未確認結果的分支指令之後）。
    - ST（Store Bit，儲存位元）：標示該指令是否為 Store 記憶體寫入指令。
    - V（Valid Bit，有效位元）：標示實體暫存器編號（Preg）是否有效。
    - Preg（Physical Register File Specifier）：儲存該指令所分配到的實體暫存器編號。
  - ROB 的指標與運作流程（Pointers & Lifecycle）：
    - Head of ROB（標頭指標）：指向佇列中最老（Oldest）的指令。Commit 階段（提交）會持續檢查 Head 的狀態，必須等到 Head 指令變為 Finished (F) 時才能進行順序提交。
    - Tail of ROB（標尾指標）：指向佇列最新分配的位置。新指令在解碼/發射階段（D/I）會從 Tail 入列並分配一個 Entry。
    - Out-of-Order Writeback（亂序寫回）：指令可在管道中亂序完成，完成時直接將對應 Entry 的 State 改為 Finished (F)（例如圖中中間已有指令標示為 F）。
    - Speculative Execution（推測執行）：若前方有分支指令尚未確定結果（In flight），後續進入 ROB 的指令其 $S$ 位元會設為 $1$。
- 個人看法與分析：
  - 精緻的 FIFO 設計與邏輯隔離：ROB 透過 FIFO（First-In, First-Out）結構完美解決了「亂序執行、順序提交」的矛盾。圖中清楚展示：就算後方的指令已經早早完成變成 Finished (F)，只要 Head 的指令還處於 Pending (P)，提交階段（Commit）就必須嚴格等待，這保證了精確例外處理（Precise Exceptions）與程式邏輯順序。
  - 支援推測執行（Speculation）與撤銷：$S$ 位元的設計展現了 ROB 強大的例外復原能力。一旦分支預測錯誤，處理器只需將 Tail 壓回至該分支指令的位置，並將標有 $S=1$ 的 Entry 清除（Flush），即可瞬間撤銷所有推測執行的無效變更，不留副作用。
- 總結：
  <br>本頁詳細解構了 Reorder Buffer (ROB) 的硬體結構與運作機制。ROB 採環形佇列設計，包含 State（Empty/Pending/Finished）、Speculative bit (S)、Store bit (ST) 及實體暫存器指標 (Preg) 等欄位。新指令自 Tail 分配入列，執行完畢於 W 階段亂序標記為 Finished；Commit 階段則嚴格等待 Head 變為 Finished 才順序退休並寫回 ARF。透過 S 位元與 FIFO 結構，ROB 成功維護了分支推測失敗時的快速撤銷機制與精確例外處理。

## slide：10
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0010.jpg" width="50%">
</div>

這張投影片的主題為 已完成儲存緩衝區（Finished Store Buffer, FSB），主要探討在亂序執行/順序提交架構中，如何暫存已執行完畢的 Store（記憶體寫入）指令資料，並分析硬體 Entry 數量對系統設計複雜度的影響。
- 本教學重點內容：
  - FSB 的硬體結構欄位：
    - V（Valid Bit）：有效位元，標示該 Entry 是否存放著待寫入的資料。
    - Op（Operation）：操作碼，標示記憶體寫入指令的具體類型。
    - Addr（Address）：目標記憶體實體/虛擬位址。
    - Data（Data）：準備寫入記憶體的數值/資料。
  - 單一 Entry（Single-Entry FSB）與多 Entry 的權衡：
    - 限制單一記憶體指令（Single Memory Instruction in flight）：若系統限制同時只能有一條記憶體指令在執行/等待，FSB 只需要 一個 Entry。
    - 極簡化分配（Single Entry makes allocation trivial）：單一 Entry 讓硬體的配置與控制邏輯變得極為簡單，無需複雜的佇列管理。
    - 多記憶體指令的挑戰（Address Aliasing）：若要支援多條記憶體指令同時在流水線中（More than one memory instruction in flight），就必須處理 Load/Store 位址別名/衝突（Address Aliasing） 問題（即後續 Load 指令可能需要讀取前方尚未正式寫入記憶體的 Store 位址，需引入 Store Forwarding 或 Memory Disambiguation）。
- 個人看法與分析：
  - 保護記憶體狀態與精確例外：Store 指令不能像一般算術指令一樣在 W 階段就直接寫入主記憶體或 Cache，因為一旦寫入就無法撤銷（Rollback）。FSB 扮演了「緩衝池」的角色，讓 Store 指令在 W 階段先將位址與資料算好存入 FSB（寫回），直到 C 階段（Commit）確定沒有任何例外發生後，才真正寫入記憶體。
  - 效能與硬體複雜度的 Trade-off：單一 Entry FSB 雖然實現簡單且避開了複雜的位址別名檢查，但會成為記憶體密集型程式（Memory-intensive programs）的重大效能瓶頸（每次 Store 都會堵塞後續記憶體存取）。這說明了為何進一步學習課程大綱（Agenda）中的 Memory Disambiguation（記憶體消歧義） 是解鎖現代 CPU 記憶體平行度（ILP）的關鍵下一步。
- 總結：
  <br>本頁介紹 Finished Store Buffer (FSB) 的欄位與設計考量。FSB 包含 V、Op、Addr、Data 欄位，用於暫存已完成執行但尚未 Commit 的 Store 資料，確保精確例外。若限制流水線中同時僅能有一條記憶體指令，只需單一 Entry FSB，硬體分配極為簡單；但若要支援多條記憶體指令以提升效能，則必須額外解決 Load/Store 之間的位址別名（Address Aliasing）與衝突問題。這展現了記憶體架構在簡化設計與提升存取平行度之間的取捨。

## slide：11
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0011.jpg" width="50%">
</div>

這張投影片呈現了 I2OI 架構（In-order Frontend/Issue, Out-of-order Writeback, In-order Commit）下，執行同一段指令序列的完整時序圖練習（Pipeline Timing Diagram Exercise）。
- 本教學重點內容：
  - I2OI 架構運算條件回顧：
    - In-order Frontend/Issue：F、D、I 必須依序處理。
    - 管道長度（Latency）：
      - X 管道（如 addi）：1 週期（ $X_0$）。
      - M 管道（如 load/store）：2 週期（ $M_0 \rightarrow M_1$）。
      - Y 管道（如 mul）：4 週期（ $Y_0 \rightarrow Y_1 \rightarrow Y_2 \rightarrow Y_3$）。
    - Reorder Buffer (ROB) & Commit：指令於 W 階段將結果寫入 PRF/ROB，並於 C 階段順序提交至 ARF。
  - 指令序列與依賴關係：
    - 0 mul x1, x2, x3：無相依，走 Y 管道。
    - 1 addi x11, x10, 1：無相依，走 X 管道，可提前完成（OOO Writeback）。
    - 2 mul x5, x1, x4：RAW 依賴指令 0 的 x1，必須在 I 階段等待指令 0 寫回結果（W）後才能發射。
    - 3 mul x7, x5, x6：RAW 依賴指令 2 的 x5，須等待指令 2 完成。
    - 4 addi x12, x11, 1：RAW 依賴指令 1 的 x11。
    - 5 addi x13, x12, 1：RAW 依賴指令 4 的 x12。
    - 6 addi x14, x12, 2：RAW 依賴指令 4 的 x12。
  - 課堂練習目標：
    <br>讓學生在 0 到 19 個 Clock Cycle 的時間軸上，填充每條指令在各週期的流水線狀態（F, D, I, $Y_0 \dots$, W, C），體會 In-order Commit 如何透過 ROB 阻擋過早提交（Commit），從而解決前述的 Early Commit 問題。
- 個人看法與分析：
  - 理論與推演的結合：前幾頁介紹了 I2OI 架構圖與 ROB 欄位，這張投影片則透過具體的時序填空，讓學生動手推演指令在具備 ROB 時的真實運轉過程。
  - 凸顯 ROB 的 Commit 阻塞效應：
    - 指令 1（addi）雖然在週期 4 或 5 就可在 W 階段寫回 PRF，但因為指令 0（mul）仍在執行，指令 1 不能直接 Commit（C 階段被卡住），必須在 ROB 中等待指令 0 先 Commit。
    - 這清晰展示了 In-order Commit 的運作真諦：寫回（Writeback）可以亂序以提升執行效率，但提交（Commit）必須嚴格順序以維護精確例外（Precise Exceptions）。
- 總結：
  <br>本頁為 I2OI 架構的流水線時序圖（Pipeline Timing Diagram）練習。題目給定包含長延遲乘法（mul）與短延遲加法（addi）的指令序列，要求填入 0～19 週期內各指令於 F、D、I、執行管道、W 與 C 階段的狀態。此練習旨在讓學生親自推演：即使短指令可提前於 W 階段亂序寫回 PRF，但受限於 ROB 的 FIFO 順序，仍須等待前方長指令退休後才能於 C 階段提交至 ARF。這具體驗證了 I2OI 架構兼顧執行效率與精確例外的運作細節。

## slide：12
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0012.jpg" width="50%">
</div>

本頁投影片（SD4_page-0012.jpg）呈現了 I2OI（In-order Issue, Out-of-order Writeback, In-order Commit）架構下完整指令運作的時序解答與 Reorder Buffer (ROB) 狀態演變：
- 本教學重點內容：
  - 流水線時序填空解答（Pipeline Timing Diagram）：
    - 指令 0 (mul x1, x2, x3)：週期 0 到 7 完成（ $F \rightarrow D \rightarrow I \rightarrow Y_0 \rightarrow Y_1 \rightarrow Y_2 \rightarrow Y_3 \rightarrow W$），於週期 8 完成 Commit（C）。
    - 指令 1 (addi x11, x10, 1)：雖然在週期 5 就已經完成 Writeback（W），但因為必須遵守 In-order Commit，必須停留在 ROB（標示為 $r$），直到週期 9 才跟隨指令 0 之後完成 Commit（C）。
    - 資料相依性阻塞（RAW Hazard）：
      - 指令 2 (mul x5, x1, x4) 相依於指令 0 的 x1，因此留在 Issue 階段（ $I$）等待，直到週期 7 指令 0 完成 W 寫回後，才於週期 8 進入 $Y_0$ 執行。
      - 指令 4 (addi x12, x11, 1) 相依於指令 1 的 x11，雖然指令 1 在週期 5 就已寫回，但指令 4 受到 Frontend 依序發射（In-order Issue）與 Fetch/Decode 佇列的限制，於週期 10 進入 $X_0$ 執行。
  - ROB 狀態變化追蹤（ROB Life Cycle）：
    - Entry 分配（Allocation）：當指令進入 Decode/Issue 階段時在 ROB 中取得 Entry（如週期 2 的 x1、週期 3 的 x11 與 x5）。
    - 完成標記（Finished / Circle）：當指令執行完畢並在 W 階段寫回結果後，ROB 中的對應欄位會被圈起來（Circle），表示已完成（Finished，例如週期 6 的 x11）。
    - 順序退休與釋放（Commit & Free Entry）：只有位於 ROB 頭部的已完成指令才能 Commit，並在下一個週期釋放（Free）ROB 空間（如週期 8 的 x1 Commit、週期 9 釋放）。
- 個人看法與分析：
  - 圖像化解構 ROB 運作機制：這頁投影片是理解 In-order Commit 最經典且直觀的範例。透過下方 ROB Entry 的生命週期追蹤，學生可以非常清楚地看到「指令寫回（Writeback）」與「指令退休（Commit）」在時間軸上的分離。
  - 亂序執行與精確例外的完美結合：指令 1（addi）早在週期 5 就已運算完畢，但其 ROB Entry 一直被鎖定到週期 9 才釋放。這種「允許 Writeback 亂序以提昇效能、強制 Commit 順序以維持狀態正確性」的設計，正是現代亂序執行 CPU 能同時實現高平行度與精確例外（Precise Exception）的關鍵所在。
- 總結：
  <br>本頁展示了 I2OI 架構下指令執行的完整時序與 ROB 狀態演變。時序圖清楚揭示：短延遲指令（如 addi）雖能提前於 W 階段寫回結果，但受限於 In-order Commit 規則，必須在 ROB 中等待前方長延遲指令（如 mul）退休後才能進行 Commit。ROB 透過 Entry 分配、完成標記與順序釋放，確保了運算亂序執行與狀態精確提交的完美平衡。

## slide：13
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0013.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片（SD4_page-0013.jpg）探討了 當第一條指令（最老指令）發生例外（Exception）時，流水線與 Reorder Buffer (ROB) 的處理流程與狀態演變：
  - 例外發生的情境：
    - 指令 0（mul x1, x2, x3）在執行或寫回階段（W）觸發了例外（例如算術溢位等）。
    - 此時，後續的指令（指令 1 ~ 4）已經在流水線的不同階段執行或等待（例如指令 1 的 addi 已在週期 5 完成 W 寫回，並停留在 ROB 等待提交 $r$）。
  - 精確例外（Precise Exception）的恢復機制：
    - 阻擋非法提交（Block Commit）：當指令 0 在 C 階段被確認發生例外時，系統絕不提交指令 0，同時也不允許後續任何已完成寫回的指令（如指令 1）進行 Commit。
    - 清空流水線（Pipeline Flush /）：圖中右側的斜線 / 表示控制邏輯會立即清空（Flush）流水線中所有位於指令 0 之後的指令（指令 1、2、3、4 等）。
    - 保持架構狀態不被污染（State Protection）：因為所有後續指令的結果都只暫存在 PRF/ROB 中而尚未寫入 ARF，清空流水線並不會破壞 CPU 的架構暫存器狀態（Architectural State）。
    - 轉跳至例外處理程式（Exception Handler）：流水線清空後，程式計數器（PC）重置並跳轉至例外處理常式（底部的 $F \rightarrow D \rightarrow I \dots$）。
- 個人看法與分析：
  - ROB 實現「精確例外」的終極體現：這張投影片完美解答了「為什麼短指令明明算完了（如指令 1 在 W 階段），卻不能直接寫入 ARF/Memory」的根本原因。如果指令 1 提前 Commit 變更了架構狀態，當前方指令 0 發生例外時，系統將無法乾淨地恢復到指令 0 執行前的狀態。
  - 亂序執行與狀態還原的代價：透過 ROB 的 In-order Commit 機制，處理器能以極低代價實現精確例外——只需將未 Commit 的 ROB Entry 標記為無效（Flush）即可，無需進行複雜的回滾（Rollback）計算。
- 總結：
  <br>本頁展示了當第一條指令觸發例外時的流水線處理機制。即使後續指令已完成執行（如指令 1 已到達 W/r 階段），受限於 ROB 的 In-order Commit 規則，這些結果皆未提交至 ARF。當指令 0 確定發生例外時，硬體會直接清空（Flush）流水線中所有後續指令，確保架構狀態不被破壞，隨後轉跳執行例外處理程式，展現了 ROB 維護精確例外（Precise Exceptions）的核心價值。

## slide：14
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0014.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片探討在具備 Reorder Buffer (ROB) 的架構中，當發生分支猜測錯誤（Branch Misprediction）時，系統處理與清空猜測指令（Squash Speculative Instructions）的三種策略機制：
  - Option 1：早期清除（Squash instructions earlier）
    - 運作機制：一旦分支指令在執行階段（ $X_0$）計算出實際結果並發現猜測錯誤時，立刻清空 Issue/Pipeline 中的後續猜測指令。
    - 優缺點：能最早釋放資源並降低猜測錯誤懲罰（Misprediction Penalty），但硬體複雜度極高，需要 ROB 支援多個讀寫埠（Many ports）來隨機存取並清除任意位置的 Entry。
  - Option 2：分支提交時清除（Squash instructions in ROB when Branch commits）
    - 運作機制：分支指令正常走完 Writeback，直到到達 Commit 階段（C）正式退休時，才一次性清空 ROB 中位居其後的所有猜測指令（斜線 /）。
    - 優缺點：簡化了 ROB 的控制邏輯（只需在 Commit 時集體 Flush），但猜測指令會在流水線與 ROB 中佔用資源較長時間。
  - Option 3：猜測指令到達 Commit 時才清除（Squash in Commit stage）
    - 運作機制：允許所有猜測指令繼續執行完畢（ $X_0 \rightarrow W$），逐一到達 Commit 階段時，再由 Commit 邏輯判定其屬於錯誤路徑而予以拋棄（Squash /）。
    - 優缺點：控制最為簡單統一（與 Exception 處理邏輯完全一致），但浪費最多的執行單元能耗與 ROB 空間。
- 個人看法與分析：
  - 設計折衷（Trade-off）的典範：這三種 Option 展現了處理器設計中「效能、功耗與硬體複雜度」的權衡：
    - Option 1 追求極致效能（最低 Pipeline Flush Latency），但付出了巨大的晶片面積與設計複雜度代價。
    - Option 2 提供了極佳的平衡點，是許多實務超純量（Superscalar）亂序執行 CPU 採用的折衷方案。
  - 統一的狀態保護機制：不論選擇哪種 Option，核心原則始終不變——猜測指令在未確定正確前絕不允許 Commit 修改 ARF。這確保了分支預測錯誤時，CPU 能夠無縫還原至正確的分支目標位址（如圖中的 T addi x12, x11, 1）。
- 總結：
  <br>本頁介紹了處理分支預測錯誤（Branch Misprediction）的三種清空（Squash）策略：Option 1 於執行階段立即清除，效能最高但 ROB 埠數多、硬體最複雜；Option 2 於分支指令 Commit 時集體清空 ROB 中的錯誤指令；Option 3 則讓猜測指令執行完後於 Commit 階段逐一拋棄。三者均依賴 ROB 阻止錯誤指令寫入架構狀態（ARF），以維護程式執行的正確性。

## slide：15
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0015.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片（SD4_page-0015.jpg）整理了在具備 Reorder Buffer (ROB) 的微架構中，針對分支指令（Branches）與猜測執行（Speculation）的硬體設計考量與三種撤銷（Squash）時間點：
  - 三種清除猜測指令（Squash Speculative Instructions）與釋放 ROB Entry 的時機點（按複雜度遞減）：
    - 1. As soon as branch resolves（分支結果一確定立即清除）：複雜度最高，但能最快釋放資源與減少效能損失。
    - 2. When branch commits（當分支指令提交時清除）：複雜度居中，在分支到達 Commit 階段時一次性清空 ROB 後續 Entry。
    - 3. When speculative instructions reach commit（當猜測指令到達提交階段時清除）：複雜度最低，讓猜測指令依序走到 Commit 階段才予以拋棄。
  - 多重在途分支（Multiple In-flight Branches）的支援：
    - 基礎設計（Base Design）：一次僅允許一條分支指令在流水線中執行（Only one branch at a time）。若遇到第二條分支指令，必須在 Decode 階段停頓（Stall）。
    - 擴充設計（Extended Design）：可透過增加追蹤位元（More bits / Branch Mask / Branch ID），讓系統能夠同時追蹤與管理多條在途的分支指令，以提升流水線的平行度與吞吐量。
- 個人看法與分析：
  - 設計觀念的系統化歸納：本頁將前一頁（Page 14）的三種 Option 做出了清晰的文字總結與複雜度排序。硬體設計師必須在「追求極致效能（Option 1）」與「控管邏輯複雜度/晶片面積（Option 2/3）」之間做出權衡。
  - 邁向現代超純量（Superscalar） CPU 的關鍵一步：基礎設計只允許單一在途分支會嚴重限制 Instruction-Level Parallelism (ILP)。引入多重分支追蹤機制（如使用 Branch Stack 或 Shadow Registers），是現代高性能處理器（如 RISC-V 亂序核心、Intel Core 系列）不可或缺的核心技術。
- 總結：
  <br>本頁總結了處理分支猜測錯誤的三種時間點策略（分支確定時、分支提交時、猜測指令到達提交時），其硬體控制複雜度依次遞減。同時指出基礎設計僅支援單一在途分支，若要突破效能瓶頸，需透過增加控制位元以支援多條分支同時在流水線中執行，為現代超純量亂序處理器的分支管理提供了完整架構觀念。

## slide：16
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0016.jpg" width="50%">
</div>

本頁投影片介紹了在包含 Store 指令與快取缺快（Store Miss）的情境下，如何透過引入 Retire 階段（R Stage）與 Committed Store Buffer (CSB) 來避免 Commit 階段發生停頓（Avoid Stalling Commit）：
- 本教學重點內容：
  - 傳統架構的問題：Store Miss 導致 Commit 停頓
    - 當 Store 指令（SW）到達 Commit 階段（C）時，必須將資料正式寫入 Cache/Memory。
    - 若此時發生 Store Miss（快取缺快），需要花費許多週期等待記憶體載入資料，導致 SW 必須停留在 Commit 階段（圖中連續多個 C）。
    - 由於 Commit 必須保持順序（In-order Commit），SW 被卡住會直接塞鎖後續所有無相依指令（如 OpB、OpC、OpD）的提交與寫回。
  - 解決方案：引入 Retire 階段（R）與 CSB
    - Committed Store Buffer (CSB)：在 Commit 階段（C）之後增加一個緩衝區 CSB。
    - Retire 階段（R）：當 SW 確定沒有發生任何例外並到達 C 階段時，它就可以立刻完成 Commit（將權限從 ROB 移交並把資料寫入 CSB），將 ROB Entry 釋放出來。
    - 下層非同步寫回（Retire to Memory）：SW 移至 Retire 階段（R），在背景非同步地將 CSB 中的資料寫回快取/記憶體。
    - 結果：後續指令（OpB、OpC、OpD）不再被 Store Miss 阻塞，能順利且連續地在後續週期完成 Commit。
- 個人看法與分析：
  - 解開 Commit 階段的最後一道枷鎖：ROB 的 In-order Commit 機制雖然保證了精確例外，但也讓「長延遲的記憶體寫入操作」成為阻塞整體流水線（Pipeline Stall）的潛在瓶頸。CSB 的設計巧妙地將「解鎖架構暫存器/ROB（Commit）」與「實際寫入物理記憶體（Retire）」解耦（Decouple）。
  - 確保記憶體一致性與安全性：進入 CSB 的 Store 指令已經過 C 階段確認無例外，因此將其放進背景慢慢寫入快取不會破壞精確例外的規則。這也是現代高效能 CPU（如 x86 的 Store Buffer / Write Buffer）普遍採用的關鍵優化技術。
- 總結：
  <br>本頁介紹了利用 Committed Store Buffer (CSB) 與 Retire 階段（R Stage）解決 Store Miss 阻塞提交的機制。當 Store 指令發生快取缺失時，傳統架構會卡住 Commit 階段並阻塞後續所有指令；而引入 CSB 後，Store 指令可在 C 階段直接將資料寫入 CSB 並釋放 ROB，隨後於 R 階段在背景完成快取寫回，從而讓後續指令免於停頓、顯著提升流水線吞吐量。

## slide：17
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0017.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片介紹了 IO3 架構（In-order Frontend, Out-of-order Issue, Out-of-order Writeback, Out-of-order Commit） 下，各主要硬體模組與暫存器結構的讀寫存取權限（R/W Ports）與資料流向：
  - IO3 架構特徵與管道階段：
    - In-order Frontend：Fetch（F）與 Decode（D）階段仍保持順序處理。
    - Out-of-order Issue：指令經過 Decode 後進入 Issue Queue (IQ)，只要操作數（Operands）準備就緒且執行單元空閒，即可亂序發射（Out-of-order Issue） 至執行管道（X、M、Y）。
    - Out-of-order Writeback & Commit：寫回（W）與提交（C）階段皆為亂序執行。
  - 核心模組的讀寫存取權限分析（Bottom Table）：
    - ARF（Architectural Register File）：
      - Issue 階段 (I)：只讀（Read, R），指令發射時從 ARF 讀取來源操作數。
      - Writeback 階段 (W)：只寫（Write, W），指令執行完畢後直接將結果寫回 ARF。
    - SB（Scoreboard）：
      - Issue 階段 (I)：可讀可寫（Read/Write, R/W），發射時查詢暫存器狀態並標記Busy。
      - Writeback 階段 (W)：寫入（Write, W），清除 Busy 標記以解鎖相依指令。
    - IQ（Issue Queue）：
      - Decode/Enqueue 階段：寫入（Write, W），將解碼後的指令填入 IQ。
      - Issue 階段 (I)：可讀可寫（Read/Write, R/W），監控並讀取就緒指令，發射後將 Entry 清空/釋放。
      - Writeback 階段 (W)：寫入/廣播（Write, W），將寫回的 Tag/Data 廣播給 IQ 內等待的其他指令（Wakeup/Forwarding）。
- 個人看法與分析：
  - 無 ROB 架構的極致亂序（與 I2OI 的對比）：
    - 在先前的 I2OI 架構中，雖然 Writeback 是亂序的，但透過 ROB 強制實現了 In-order Commit 以維護精確例外（Precise Exceptions）。
    - IO3 架構取消了 ROB 的順序約束，指令一算完在 W 階段就直接把結果寫進 ARF（即 Commit 亦為亂序）。這種設計雖然硬體控制極度簡化、延遲極低，但無法支援精確例外（Precise Exceptions）與分支猜測恢復。
  - Issue Queue (IQ) 的關鍵角色：
    - IQ 是實現 Out-of-order Issue 的心臟。它需要複雜的 Wakeup（喚醒）與 Select（選擇）邏輯，當 W 階段廣播結果時，IQ 內的指令必須同時比對 Tag，並在下個週期爭奪執行管道。
- 總結：
  <br>本頁介紹了 IO3（In-order Frontend, Out-of-order Issue/Writeback/Commit）架構的硬體佈局與記憶體元件存取模式。此架構引入 Issue Queue (IQ) 來實現指令的亂序發射與執行，並詳細整理了 ARF、Scoreboard (SB) 與 IQ 在發射 (I) 與寫回 (W) 階段的讀寫 (R/W) 關係。雖然 IO3 能最大化指令平行度，但由於結果直接寫回 ARF 且缺乏順序提交機制，無法保證精確例外與猜測執行的安全恢復。

## slide：18
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0018.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片介紹了 Issue Queue (IQ) 的內部硬體結構欄位以及指令發射（Instruction Ready / Issue）的判斷邏輯：
  - Issue Queue (IQ) 的 Entry 結構欄位：
    - Op：操作碼（Opcode），標示指令類型。
    - Imm / S：立即數（Immediate）與猜測位元（Speculative Bit, S）。
    - V / Dest：目標暫存器（Destination Register）與有效位元（Valid Bit）。
    - V / P / Src0 & Src1：來源暫存器（Source Registers）欄位：
      - V（Valid）：該指令是否有對應的來源暫存器。
      - P（Pending）：待產生狀態，標示來源資料是否還在等待前方指令計算產出（1 表示 Waiting，0 表示 Ready）。
  - 指令就緒判斷邏輯（Instruction Ready Logic）：
    - 判斷條件公式：
      <br>Instruction Ready = ( $!V_{\text{src0}}$ || $!P_{\text{src0}}$) &&  ( $!V_{\text{src1}}$ || $!P_{\text{src1}}$) && no structural hazards
    - 邏輯解讀：一條指令若要被認定為就緒（Ready），必須同時滿足：
      - Src0 就緒：不需要 Src0（ $!V_{\text{src0}}$），或者 Src0 已準備完畢不處於等待狀態（ $!P_{\text{src0}}$）。
      - Src1 就緒：不需要 Src1（ $!V_{\text{src1}}$），或者 Src1 已準備完畢不處於等待狀態（ $!P_{\text{src1}}$）。
      - 無結構衝突：對應的執行管道/算術邏輯單元（ALU）目前空閒（No structural hazards）。
    - 效能優化（For High Performance）：
      - 為了追求高效能，發射邏輯需要結合 Bypassing / Forwarding（旁路/前饋） 機制。當前方指令在執行階段（如 $X_0$ 或 $W$）產出結果時，可直接透過 Bypass 網絡廣播給 IQ 內處於 Pending 狀態的指令，使其無需等資料寫入暫存器即可提前解鎖發射。
- 個人看法與分析：
  - 動態排程（Dynamic Scheduling）的核心心臟：Issue Queue 是實現 Out-of-order Issue（亂序發射）最關鍵的組合邏輯單元。透過保留區 Entry 中的 Pending ($P$) 位元，處理器能在硬體層級自動解決 RAW (Read-After-Write) 相依性。
  - 喚醒與選擇（Wakeup and Select）的硬體挑戰：投影片呈現的 Ready 邏輯雖然看起來直觀，但在多發射超純量（Superscalar）處理器中，IQ 每個週期都需要同時比對數十個 Entry 的 Tag 並進行仲裁（Select），這構成了微架構設計中最關鍵的臨界路徑（Critical Path）與晶片面積/功耗來源之一。
- 總結：
  <br>本頁詳細解析了 Issue Queue (IQ) 的硬體結構欄位與動態發射邏輯。IQ 透過 Valid ( $V$) 與 Pending ( $P$) 位元精確追蹤來源操作數的就緒狀態，當指令的操作數皆已就緒且執行單元無結構衝突時即可發射。結合 Bypassing 機制，IQ 能夠將剛產出的資料即時前饋給等待中的指令，從而最大化指令層級平行度（ILP）與亂序執行效能。

## slide：19
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0019.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片展示了在動態排程微架構中，兩種主要的發射佇列（Issue Queue, IQ）佈局組織與組織差異：集中式發射佇列（Centralized Issue Queue） 與 分散式發射佇列（Distributed Issue Queue）。
  - 集中式發射佇列（Centralized Issue Queue）
    - 架構組織：所有解碼後的指令不論類型（如算術邏輯、記憶體存取、乘除法），全部進入同一個共享的 Issue Queue（IQ）。
    - 運送流程：在單一 IQ 中統一進行運算子就緒監控（Wakeup & Select），一旦條件滿足，再發射至各自對應的執行管道（如 $X_0$ 算術管道、 $M_0$ 記憶體管道、 $Y_0$ 乘法管道）。
    - 優缺點：
      - 優點：硬體資源利用率高，不易因為特定類型指令突發而造成單一 Queue 溢位停頓（Stall）。
      - 缺點：IQ 體積龐大，Port 數量多（需要同時連接所有執行單元），搜尋與比對邏輯（Wakeup/Select）的臨界路徑極長，限制了 CPU 時脈頻率。
  - 分散式發射佇列（Distributed Issue Queue）
    - 架構組織：根據指令類型將 Issue Queue 分離為多個獨立的子佇列（例如 IQ A 負責整數/算術管道，IQ B 負責浮點數或乘法管道）。
    - 運送流程：指令在 Decode 階段就被分流（Steer）寄送至指定的 IQ A 或 IQ B，各自獨立監控並發射至對應的管道（如 $X_0/M_0$ 或 $Y_0$）。
    - 優缺點：
      - 優點：每個子 Queue 的 Entry 數與 Port 數大幅減少，喚醒與選擇邏輯顯著簡化，能有效提升時脈頻率（Clock Frequency）與降低功耗。
      - 缺點：負載平衡較差，若連續出現大量相同類型的指令（例如連續整數指令），即使其他 Queue 空閒，對應的子 Queue 仍可能滿載導致 Decode 停頓。
- 個人看法與分析：
  - 微架構權衡的典型案例：集中式與分散式 IQ 的比較，完美體現了「資源利用率」與「硬體延遲/面積」之間的經典 Trade-off。
    - 集中式能最大化利用每一個 Queue Entry，但隨著 Superscalar 發射寬度擴張，其複雜度呈次方級成長。
    - 分散式則透過「分而治之（Divide and Conquer）」成功降低了臨界路徑延遲，因此在當代許多高效能 CPU（例如 Intel 的 Reservation Station 演進、AMD Zen 微架構）中，多採用分散式或半分散式的 Cluster 設計。
- 總結：
  <br>本頁介紹了 Centralized（集中式）與 Distributed（分散式）Issue Queue 的架構設計。集中式 IQ 由所有執行管道共享 Entry，資源利用率高但控制邏輯最為複雜；分散式 IQ 則按指令類型將 Queue 拆分（如 IQ A 與 IQ B），有效簡化了 Wakeup/Select 邏輯與 Port 數量，雖可能產生負載不均問題，卻能顯著優化 CPU 時脈與功耗表現。

## slide：20
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0020.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片（SD4_page-0020.jpg）展示了一個支援動態排程與超純量執行的 Pipeline 微架構範例，並透過一組組譯指令序列說明指令在該架構下的發射與執行時序關係：
  - 流水線結構（Pipeline Architecture）：
    - 前段（Front-end）：包含 F（Fetch, 讀取）、D（Decode, 解碼）、IQ（Issue Queue, 發射佇列）與 I（Issue, 發射）。
    - scoreboard (SB)：於 I（Issue）階段進行記分板狀態更新。
    - 多執行管道（Execution Pipelines）：
      - $X_0$ 管道：單週期的 ALU 算術邏輯執行單元。
      - $M_0 \to M_1$ 管道：雙週期的 Memory 記憶體存取單元。
      - $Y_0 \to Y_1 \to Y_2 \to Y_3$ 管道：四週期的 Multiply 乘法執行單元。
    - 後段（Back-end）：W（Writeback, 寫回）寫入 ARF（Architecture Register File, 架構暫存器檔案）。
  - 範例指令序列（Instruction Trace）：
    - 0 mul  x1, x2, x3 (乘法，走 $Y$ 管道，需要 4 週期)
    - 1 addi x11, x10, 1 (加法，走 $X$ 管道，需要 1 週期)
    - 2 mul  x5, x1, x4 (乘法，相依於指令 0 的 x1，資料相依 RAW Hazard)
    - 3 mul  x7, x5, x6 (乘法，相依於指令 2 的 x5)
    - 4 addi x12, x11, 1 (加法，相依於指令 1 的 x11)
    - 5 addi x13, x12, 1 (加法，相依於指令 4 的 x12)
    - 6 addi x14, x12, 2 (加法，相依於指令 4 的 x12)
- 個人看法與分析：
  - RAW 資料相依性對時序的限制：
    - 指令 0（mul）產出 x1 需要經由 $Y_0 \to Y_1 \to Y_2 \to Y_3$ 長達 4 個週期的延遲。指令 2 需要用到 x1，因此指令 2 雖然早已進入 Issue Queue，但必須在 x1 經由 Bypass 或 Writeback 準備好後才能發射，展現了動態排程中由資料流驅動（Data-driven）的特質。 
  - 獨立指令的 Out-of-Order（亂序）優勢：
    - 指令 1（addi）與指令 0 無資料相依，因此可以在指令 0 執行長延遲乘法時提前發射並完成；同理，後續無相依的 addi 指令序列（如指令 4, 5, 6）也能在乘法鏈卡住時持續推進，充份發揮平行處理的效益。
- 總結：
  <br>本頁展示了具備多條不同延遲執行管道（ALU/Memory/Multiply）的動態排程處理器架構。透過微架構圖與底部的時間軸預留表，用來實測並填寫 Out-of-Order 執行時各指令在 $F, D, I, X/M/Y, W$ 各階段的實際週期分配。

## slide：21
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0021.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片呈現了 IO3 架構（In-order Frontend, Out-of-order Issue/Writeback/Commit）下完整指令執行的時序解答與 Issue Queue (IQ) 狀態演變：
  - 流水線時序解答（Pipeline Timing Diagram）：
    - 指令 0 (mul x1, x2, x3)：週期 0 到 7 完成執行與寫回（ $F \to D \to I \to Y_0 \to Y_1 \to Y_2 \to Y_3 \to W$），在週期 7 完成 $W$ 時即直接更新 ARF（即 Commit 亦為亂序）。
    - 指令 1 (addi x11, x10, 1)：週期 1 到 5 完成（ $F \to D \to I \to X_0 \to W$），於週期 5 在 $W$ 階段直接完成寫回與 Commit，無需等待指令 0 結束。
    - Issue Queue 中的小寫 $i$（Pending / Waiting）：
      - 小寫 $i$ 代表指令已進入 IQ，但因來源操作數尚未就緒（RAW 相依）而處於等待發射狀態。
      - 例如 指令 2 (mul x5, x1, x4) 在週期 4 進入 IQ（以小寫 $i$ 標示），直到週期 7 指令 0 完成 $W$ 並提供 x1 後，才於週期 8 轉為大寫 $I$ 正式發射至 $Y_0$。
  - Issue Queue (IQ) 狀態變化與標記圖解：
    - 欄位結構：記錄 Dest / Src0 / Src1 的狀態。
    - 畫圈（Circle）：圈選代表該暫存器的數值已經存在於 ARF 中（Present in ARF），例如週期 2 的 x2 與 x3。
    - 無圈（No Circle）與 Bypass：當數值是由 Writeback 階段通過 Bypass 網路直接前饋傳遞時，Present bit 被置位但不會畫圈。如圖中註記所示：「Value set present by Instruction 1 in cycle 5, W Stage」（指令 1 於週期 5 在 W 階段將 x11 標記為 Present，解除指令 4 的等待）。
- 個人看法與分析：
  - 更直觀的動態排程視覺化：透過小寫 $i$（在 IQ 內等待）與大寫 $I$（成功發射）的區分，讓學生清晰看到動態排程（Dynamic Scheduling）中「指令佇列等待」與「實際管線發射」的時間落差。
  - 無 ROB 架構的快速執行優勢與隱患：從時序圖可見，指令 1 在週期 5 就已經完全退休並釋放資源，沒有任何流水線停頓（Stall），展現了 IO3 極高的執行吞吐量。然而，若指令 0 在週期 6 或 7 發生例外，由於指令 1 的結果已不可逆地寫入 ARF，將導致系統無法還原至精確例外狀態。
- 總結：
  <br>本頁展示了 IO3 架構下指令執行的完整時序解答與 Issue Queue (IQ) 的 Entry 演變追蹤。時序圖利用小寫 $i$ 標記指令於 IQ 中等待來源操作數的週期，並詳細展示了 Bypass 前饋機制如何於 W 階段解除 IQ 中相依指令的等待狀態，充份演繹了動態排程與亂序執行的運作細節。

## slide：22
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0022.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片（SD4_page-0022.jpg）展示了一個假設情境下的流水線執行時序：假設所有指令皆已預先載入至 Issue Queue（Assume All Instructions in Issue Queue），並對比在前頁（Page 21）常態 Decode 進入條件下的效能差異：
  - 理想化假設（All Instructions in IQ）：
    - 在週期 0 時，假設所有指令（0 至 6）都已經通過 Fetch 與 Decode 階段，並已保存在 Issue Queue 中（如圖中在週期 0~2 時，各指令的 $i$ 狀態）。
    - 由於沒有前段 Fetch/Decode 的發射瓶頸（Bandwidth Limit），每條指令只需要等其來源操作數（Data Hazards）解除即可立即發射（ $I$）。
  - 時序變化分析（Pipeline Timing Diagram）：
    - 指令 0 (mul) & 指令 1 (addi)：無前置 RAW 相依，雙雙在週期 2 正式發射（ $I$）進入 $Y_0$ 與 $X_0$。
    - 指令 4 (addi x12, x11, 1)：由於指令 1 在週期 4 完成 $W$ 階段，指令 4 在週期 4 即可被喚醒並於週期 4 正式發射（ $I$），於週期 5 完成執行。
    - 指令 5 & 6：受惠於指令 4 的提前完成，後續相依指令亦大幅提前發射（週期 7 與 8 完成）。
  - 思考問題：效能是否真的更好？（Better performance than previous?）
    - 答案是：是的（Total Execution Time 縮短）。
    - 在前頁（Page 21）的常態流水線中，最後一條指令（指令 6）要在週期 13 才完成 $W$ 階段；而在本頁「預先在 IQ」的情境下，指令 6 於週期 9 即完成 $W$ 階段，總執行時間縮短了 4 個週期。
- 個人看法與分析：
  - 前段頻寬（Frontend Bottleneck）對動態排程的影響：
    - 本頁範例清楚說明了：即使後段（Issue Queue / Execution Units）具備強大的亂序執行能力，如果前段（Fetch / Decode / Rename）傳送指令的速度太慢（如每週期僅 Decode 1 條指令），後段的 Issue Queue 就會發生「無指令可選（Undersupply）」的飢餓現象。
  - 現代超純量（Superscalar）設計的啟示：
    - 這也是為什麼現代 CPU 普遍採用 Wide Frontend（如 4-way 或 8-way Decode/Rename）以及大型 Instruction Buffer / Decoded Stream Buffer (DSB) 的原因，確保 Issue Queue 隨時有足夠多的指令可供喚醒與亂序發射，以最大化指令層級平行度（ILP）。
- 總結：
  <br>本頁透過「所有指令預先存於 Issue Queue」的理想化情境，展示了解除 Fetch/Decode 前段頻寬限制後的流水線時序。對比常態流程，此方法讓無相依與早解鎖的指令（如 addi 鏈）能大幅提前發射與完成，使整體指令序列完成時間從 13 週期縮短至 9 週期，突顯了強大前段吞吐量對動態排程效能的關鍵決定性。

## slide：23
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0023.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片（SD4_page-0023.jpg）介紹了 IO2I 架構（In-order Frontend, Out-of-order Issue/Writeback, In-order Commit） 下，系統硬體元件的結構組成與各階段的存取權限（R/W Ports）關係：
  - IO2I 架構特徵與管道階段：
    - In-order Frontend：Fetch（F）與 Decode（D）階段保持順序發射。
    - Out-of-order Issue / Writeback：進入 Issue Queue（IQ）後可亂序發射至執行單元（X、M、Y），計算結果亦為亂序寫回（W）至物理暫存器檔案（PRF）。
    - In-order Commit：引入 Reorder Buffer（ROB）與 Future Status Buffer（FSB），確保指令按照原始程式順序（In-order）進行提交（C）至架構暫存器檔案（ARF），以保證精確例外（Precise Exceptions）與猜測執行的正確性。
  - 核心模組存取權限矩陣（Bottom Table）：
    - ARF（Architectural Register File）：
      - Commit 階段 (C)：只寫（Write, W），僅在指令順序提交時更新架構狀態。
    - SB（Scoreboard）：
      - Issue 階段 (I)：可讀可寫（R/W）。
      - Writeback 階段 (W)：寫入（W）。
    - PRF（Physical Register File）：
      - Issue 階段 (I)：只讀（Read, R），發射時讀取物理暫存器內的最新數據。
      - Writeback 階段 (W)：寫入（Write, W），執行完畢後將結果寫回 PRF。
    - ROB（Reorder Buffer）與 FSB（Future Status Buffer）：
      - Decode/Enqueue 階段：可讀可寫（R/W），分配 ROB Entry 並維護指令狀態。
      - Writeback 階段 (W)：寫入（Write, W），更新指令完成標記與結果數據。
      - Commit 階段 (C)：可讀可寫（R/W），確認前方指令順序完成並釋放 Entry。
    - IQ（Issue Queue）：
      - Decode 階段：寫入（Write, W）。
      - Issue 階段 (I)：可讀可寫（R/W）。
- 個人看法與分析：
  - 完整實現現代亂序執行的經典微架構：與前一頁（Page 17）的 IO3 架構相比，IO2I 最大的改良在於加入了 ROB 與 ARF/PRF 的解耦機制。雖然 Issue 與 Writeback 仍維持 Out-of-order 以極大化吞吐量，但由 ROB 強制執行的 In-order Commit 為處理器補足了精確例外與猜測恢復（Speculation Recovery）的核心防線。
  - 暫存器分工明確化：ARF 只在 Commit 階段寫入，代表 ARF 隨時代表「已被百分之百確認（Committed）的正確程式狀態」；而中間過程的動態結果則暫存在 PRF 中，這也是現代亂序 CPU（如 RISC-V 亂序核心、Intel/AMD 近代架構）處理暫存器重命名（Register Renaming）與順序退休的標準做法。
- 總結：
  <br>本頁詳細拆解了 IO2I（In-order Frontend, Out-of-order Issue/Writeback, In-order Commit）架構的硬體佈局與核心組件存取埠。相較於無法保證精確例外的 IO3，IO2I 結合了 Issue Queue (IQ) 的亂序發射能力與 Reorder Buffer (ROB) 的順序提交機制，兼具高效能與系統安全性，為現代亂序處理器的經典微架構範例。

## slide：24
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0024.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片展示了在 IO2I 架構（In-order Frontend, Out-of-order Issue/Writeback, In-order Commit） 下的微架構管道圖與時間軸練習預留表：
  - 流水線結構（Pipeline Architecture）：
    - 前段（Front-end）：保持順序處理，包含 F（Fetch）、D（Decode）、IQ（Issue Queue）與 I（Issue）。
    - Scoreboard (SB)：於 I（Issue）階段進行狀態檢測與更新。   多執行管道（Execution Pipelines）：
      - $X_0$ 管道：單週期的 ALU 算術邏輯執行單元。
      - $M_0 \to M_1$ 管道：雙週期的 Memory 記憶體存取單元。
      - $Y_0 \to Y_1 \to Y_2 \to Y_3$ 管道：四週期的 Multiply 乘法執行單元。
        - 後段（Back-end）：
          - W（Writeback）：亂序將計算結果寫回物理暫存器檔案（PRF），並同時廣播更新 ROB / FSB。
          - C（Commit）：透過 Reorder Buffer (ROB) 與 Future Status Buffer (FSB) 強制執行順序提交（In-order Commit），順序將結果寫入架構暫存器檔案（ARF）。
  - 待推導指令序列（Instruction Trace）：
    - 0 mul  x1, x2, x3 (乘法，4 週期)
    - 1 addi x11, x10, 1 (加法，1 週期)
    - 2 mul  x5, x1, x4 (乘法，RAW 相依於指令 0 的 x1)
    - 3 mul  x7, x5, x6 (乘法，RAW 相依於指令 2 的 x5)
    - 4 addi x12, x11, 1 (加法，RAW 相依於指令 1 的 x11)
    - 5 addi x13, x12, 1 (加法，RAW 相依於指令 4 的 x12)
    - 6 addi x14, x12, 2 (加法，RAW 相依於指令 4 的 x12)
- 個人看法與分析：
  - IO2I 與 IO3 在時序推導上的關鍵差異（In-order Commit 效應）：
    - 在上一單元 IO3 中，指令 1 (addi) 只要在週期 5 完成 Writeback ($W$) 就會立刻完成退休並離開系統（亂序 Commit）。
    - 然而在 IO2I 中，雖然指令 1 在週期 5 就已經完成 $W$ 階段，但因為前面的指令 0 (mul) 需要執行到週期 7 才進入 $W$，指令 1 必須停留在 ROB 中等待指令 0 完成 Commit 後，才能在週期 8 進行 Commit ( $C$)。
  - 確保精確例外與狀態恢復的硬體代價：
    - 此頁練習旨在讓學生深刻體會到 ROB 的 In-order Commit 機制如何阻止早發射、早算完的指令「過早破壞 ARF 架構狀態」。這使得系統隨時具備精確例外能力，但同時也對 ROB 的 Entry 容量提出了更高要求。
- 總結：
  <br>本頁展示了 IO2I 微架構及其對應的指令時間軸推導練習表。相較於 IO3，本頁結構新增了 ROB、FSB 與 PRF/ARF 的雙層暫存器機制，旨在示範指令如何在保持亂序發射與寫回（Out-of-order Issue/Writeback）的效能優勢下，依然透過 ROB 達成順序提交（In-order Commit）以維護精確例外。

## slide：25
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0025.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片展示了在 IO2I 架構（In-order Frontend, Out-of-order Issue/Writeback, In-order Commit） 下指令執行的完整時序解答，並提示讀者觀察與前頁/其他微架構（如 IO3）之間的關鍵差異：
  - 流水線狀態標籤說明：
    - i（小寫 i）：代表指令已完成 Decode，目前保存在 Issue Queue (IQ) 中等待操作數（Pending/Waiting）。
    - I（大寫 I）：代表來源操作數已準備完畢，指令正式從 IQ 發射至執行管道（Issue）。
    - r（小寫 r）：代表指令已完成計算與 Writeback（W 階段），但因為前面尚有未提交（Uncommitted）的指令，必須停留在 Reorder Buffer (ROB) 中等待順序提交（Reorder Buffer Waiting / Ready to Commit）。
  - 指令時序與 In-order Commit 運作分析：
    - 指令 0 (mul x1, x2, x3)：週期 2 發射，週期 7 完成 W，並於週期 8 完成 C（Commit）。
    - 指令 1 (addi x11, x10, 1)：週期 3 發射，週期 5 完成 W。由於指令 0 尚未 Commit，指令 1 於週期 6、7 進入 r 狀態等待，直到週期 8 指令 0 提交後，才於週期 9 完成 C。
    - 指令 2 (mul x5, x1, x4)：等待指令 0 的 x1，週期 8 發射（ $I$），週期 12 完成 W，週期 13 完成 C。
    - 指令 4 ~ 6 (addi 鏈)：指令 4 於週期 6 發射、週期 8 完成 W，但因指令 3 卡住提交，指令 4 在週期 9 ~ 15 持續處於 r 狀態，直到週期 16 才順利 C。
  - 「Difference?（與 IO3 的差異）」思考解析：
    - 執行總週期相同（Latency）：兩者的整體 Writeback（W）完成時間點幾乎一致（例如指令 6 皆在週期 12 完成 W）。
    - 退休時機不同（Commit / Retirement）：
      - 在 IO3 中，指令一完成 W 就立刻寫回 ARF 並離開系統（亂序 Commit）。
      - 在 IO2I 中，指令必須透過 ROB 嚴格遵守 In-order Commit。完成 W 後會進入 r 階段暫存，直到前方所有指令依序完成 Commit 後，才能寫回 ARF。
- 個人看法與分析：
  - r 狀態（Waiting in ROB）的重要性：r 狀態非常直觀地展現了 ROB 如何在「允許亂序執行/寫回」與「維持精確例外（Precise Exceptions）」之間取得平衡。雖然指令 1、4、5、6 早就算好了答案，但它們被「鎖」在 ROB 中，避免了對架構狀態（ARF）的破壞。
  - ROB 阻塞與效能影響：雖然 In-order Commit 保證了精確例外，但如果前方有一條超長延遲的指令（例如 Cache Miss 或長延遲除法/乘法），會導致後續大量算完的指令積壓在 ROB（出現連續的 r），若 ROB 容量不足（Full），就會倒灌導致前段 Decode 停頓（Stall）。
- 總結：
  <br>本頁展示了 IO2I 微架構下指令執行的完整時序與 ROB 狀態變化。透過引入 r 標籤，明確標示了早算完的指令在等待前方指令提交時於 ROB 中停留的時間點。對比 IO3 架構，IO2I 雖然執行階段時間相同，但透過 ROB 強制實現了順序提交（In-order Commit），成功確保了精確例外與猜測執行的安全恢復。

## slide：26
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0026.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片展示了在 亂序執行 2-Wide 超純量（Out-of-order 2-Wide Superscalar with 1 ALU） 環境下的指令執行時序圖：
  - 架構規格特徵（2-Wide Superscalar, 1 ALU）：
    - 2-Wide 前段（2-Wide Frontend）：每週期最多可同時讀取（Fetch）、解碼（Decode）與解鎖發射（Issue）2 條指令（如週期 0 的指令 0 與指令 1 同時進行 $F$）。
    - 單一 ALU 執行單元（1 ALU）：硬體僅配備 1 個 $X_0$ 管道（ALU），因此在同一週期內最多只能有一條加法指令在 $X_0$ 執行（Structural Hazard 結構衝突）。
    - In-order Commit (IO2I 延伸)：透過 Reorder Buffer (ROB) 強制指令依原始程式順序提交。
  - 指令時序與瓶頸分析：
    - 指令 0 (mul) & 指令 1 (addi)：
      - 於週期 0 同時 Fetch ( $F$)，週期 1 同時 Decode ( $D$)。
      - 於週期 2 同時 Issue ( $I$)，分別進入 $Y_0$（乘法器）與 $X_0$（ALU）執行，展現了 2-Wide 超純量並行處理能力。
    - 指令 2 (mul) & 指令 3 (mul)：
      - 於週期 1 同時 Fetch ( $F$)，週期 2 同時 Decode ( $D$) 並進入 Issue Queue ( $i$)。
    - 指令 4、5、6 的結構衝突與發射限制（ALU Bottleneck）：
      - 指令 4 (addi x12, x11, 1)：等待指令 1 於週期 4 完成 $W$，於週期 4 解鎖發射 ( $I$) 並佔用 $X_0$（週期 4）。
      - 指令 5 (addi x13, x12, 1)：雖然與指令 4 一起在週期 2 Fetch、週期 3 Decode，但因相依於指令 4 的 x12，必須等到指令 4 於週期 6 完成 $W$，於週期 5 發射/週期 5 執行。
      - 指令 6 (addi x14, x12, 2)：相依於指令 4 的 x12，在週期 5 結束時 x12 已經準備完畢（可被 Issue Queue 喚醒）。然而因為硬體只有 1 個 ALU ( $X_0$)，且週期 5 已被指令 5 佔用，指令 6 必須順延至週期 6 才能發射 ( $I$) 進入 $X_0$。 
- 個人看法與分析：
  - 前段頻寬提升對整體產出的效益：
    - 對比單發射（1-Wide）的 IO2I（Page 25，最後一條指令於週期 18 完成 Commit），進入 2-Wide Superscalar 後，指令 0 到 3 能更快進入 Issue Queue，整體指令 6 的 Commit 完成時間提前到了週期 17。
  - 結構衝突（Structural Hazard）成為新瓶頸：
    - 本頁範例極佳地說明了「雙發射（2-Wide）」並不等於「效能直接翻倍」。當程式碼中連續出現同類型指令（如連續的 addi 算術指令），若硬體資源（ALU 數量）不足（僅 1 個 ALU），即使 Issue Queue 中有多條指令準備就緒，仍會因爭奪 $X_0$ 執行單元而產生序列化延遲（Structural Hazard）。
- 總結：
  <br>本頁展示了 2-Wide 超純量與單一 ALU 配置下的亂序執行時序解答。透過將 Fetch/Decode 頻寬提升至每週期 2 條指令，加速了指令充實 Issue Queue 的速度；同時也展示了當多條加法指令（指令 4、5、6）競爭唯一 ALU 資源時所發生的結構衝突與順序發射現象，完整傳達了超純量微架構中軟硬體資源搭配的平衡思考。

## slide：27
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0027.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片整理並比較了 亂序執行（Out-of-Order, OOO）處理器微架構演進的全景總表，透過對比各架構在流水線四大階段（Frontend, Issue, Writeback, Commit）的執行特性與所需硬體元件，歸納出不同 OOO 設計的核心差異：
  <br>各微架構特徵解析與演進脈絡
  - 傳統順序執行架構 ( $I_4$)：
    - 特徵：所有階段（Frontend, Issue, Writeback, Commit）皆嚴格遵守順序執行（In-Order）。
    - 缺點：遇到長延遲指令（如記憶體存取或多週期乘法）時，後續無相依的指令會被強制卡住（Stall），降低流水線利用率。
  - 早期亂序寫回架構 ( $I_2O_2$ / $I_2O_1$)：
    - $I_2O_2$：允許 Writeback 與 Commit 亂序，硬體成本低，但無法處理精確例外（Precise Exceptions）與猜測執行。
    - $I_2O_1$：導入 Reorder Buffer (ROB) 與 Store Buffer，將 Commit 鎖回 In-Order，解決了精確例外問題，但 Issue 階段仍為 In-Order，限制了指令動態排程的能力。
  - 現代亂序執行架構 ( $IO_3$ / $IO_2I$)：
    - $IO_3$（In-order Issue Queue, OOO Issue/WB/Commit）：加入 Issue Queue (IQ)，實現真正由數據驅動（Data-driven）的亂序發射與寫回，發揮極高 ILP。然而因亂序 Commit，仍缺乏精確例外保障。
    - $IO_2I$（In-order Frontend, OOO Issue/WB, In-order Commit）：結合了 Issue Queue (IQ) 的亂序發射能力與 Reorder Buffer (ROB) 的順序提交機制。這是現代高效能 CPU（如 RISC-V 亂序核心、Intel/AMD 近代架構）最經典的微架構基石，既能極大化指令並行度，又能維持系統的精確例外與記憶體一致性。
- 個人看法與分析：
  - ROB（Reorder Buffer）是實現「安全亂序」的分水嶺：
    - 從表格可看出，只要 Commit 階段標註為 IO（In-Order） 的架構（如 $I_2O_1$ 與 $IO_2I$），硬體組件必定包含 Reorder Buffer (ROB) 與 Store Buffer。這說明了 ROB 是現代處理器在追求亂序高效能時，用來保障「軟體語意正確性」與「精確例外狀態復原」不可或缺的防線。
  - 軟硬體權衡（Trade-off）總結：
    - $IO_3$ 雖然硬體較簡單（無需 ROB）且完成速度快，但無法處理分支預測失敗或中斷；$IO_2I$ 雖然需要額外的 ROB 與 Store Buffer 成本，但換來了完美的例外處理機制與完整的猜測執行（Speculative Execution）支援，成為現代商用通用處理器的標準選擇。
- 總結：
  <br>本頁投影片作為單元總結，全面梳理了從 $I_4$ 到 $IO_2I$ 各微架構的執行階段特性與硬體組件對應關係。透過這張對照表，可以清楚掌握動態排程（IQ）與順序提交（ROB）如何共同構築現代亂序處理器的核心設計。

## slide：28
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0028.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片展示了 Intel 歷代超純量（Superscalar）處理器的微架構演進發展史（引用自 Hennessy & Patterson 所著《Computer Organization and Design RISC-V Edition》Figure 4.74）：
  - Intel 歷代微處理器規格對照表：
    - 微處理器 (Processor)
    - 時脈 (Clock Rate)
    - 流水線階數 (Pipeline Stages)
    - 發射寬度 (Issue Width)
    - 亂序執行/猜測 (OOO / Speculation)
    - 核心數 (Cores/Chip)
  - 核心微架構發展趨勢與結論：
    - Pentium 4 時代的極限（Frequency Wall & Power Wall）：市場行銷強烈追求更高的時脈速度（Clock Rate），導致設計走向極端深層的流水線（Deeper Pipelines，如 Prescott 達 31 階），但也帶來了高昂的功耗代價（103W）與分支預測失敗時極高的懲罰代價。
    - 後續走向多核心（Multi-core Processors）：在 Pentium 4 遇到「功耗牆（Power Wall）」後，Intel 放棄了盲目拉高時脈與加深流水線的策略，轉而回到 14 階左右的最佳流水線深度（Core 微架構），並開啟了透過增加核心數量（Multi-core）來提升整體算力的世代。
- 個人看法與分析：
  - 單核效能與功耗牆的歷史轉折：
    - Pentium Pro (1997) 是 Intel 導入動態排程與亂序執行（OOO）的里程碑。但到了 Pentium 4 (Prescott)，為了將時脈衝上 3.6 GHz，流水線被切分成 31 階，使得每階邏輯過少、漏電流與功耗暴增，最終迫使晶片設計方向徹底轉變。
  - 理想流水線深度的平衡：
    - 從 2006 年的 Intel Core 開始，流水線階數穩定停留在 14 階左右。這證明了在考量分支預測懲罰、硬體複雜度與熱功耗限制下，14~16 階是亂序超純量處理器在效能與功耗之間的黃金平衡點。
- 總結：
  <br>本頁投影片透過 Intel 處理器近三十年的發展數據，呈現了超純量與亂序執行技術的演進過程。重點展示了 Pentium 4 時代盲目追求極高時脈與超深流水線所帶來的功耗瓶頸，以及後來轉向兼顧單核指令並行度（IPC）與多核心（Multi-core）並行的策略轉變。

## slide：29
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0029.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片展示了 嵌入式行動端核心 ARM Cortex-A53 與 高性能伺服器/桌面端核心 Intel Core i7 920 在微架構規格與設計哲學上的詳細對比（引用自 Hennessy & Patterson 所著《Computer Organization and Design RISC-V Edition》Figure 4.71）：
  - 核心規格與微架構對照表：
    |特性 (Characteristic)  |ARM Cortex-A53  |Intel Core i7 920|
    |--|--|--|
    |目標市場 (Market)  |個人行動裝置 (Personal Mobile Device)   |伺服器、雲端 (Server, Cloud)|
    |熱設計功耗 (TDP)   |100 mW (1 core @ 1 GHz)   |130 W|
    |時脈 (Clock Rate)  |1.5 GHz   |2.66 GHz   |
    |核心數 (Cores/Chip)  |4 核心（可配置）   |4 核心   |
    |浮點運算 (Floating Point)  |支援 (Yes)   |支援 (Yes)   |
    |多發射 (Multiple Issue)|動態多發射 (Dynamic)   |動態多發射 (Dynamic)   |
    |最高 IPC (Peak Inst/Cycle)  |2 條指令 / 週期   |4 條指令 / 週期   |
    |流水線階數 (Pipeline Stages)  |8 階   |14 階   |
    |排程機制 (Pipeline Schedule)  |Static In-order (靜態順序)   |Dynamic Out-of-order with Speculation (動態亂序 + 猜測執行)   |
    |分支預測 (Branch Prediction)  |混合式 (Hybrid)   |雙層 (2-level)   |
    |L1 快取 (1st Level Cache)  |16–64 KiB I-Cache, 16–64 KiB D-Cache   |32 KiB I-Cache, 32 KiB D-Cache   |
    |L2 快取 (2nd Level Cache)  |128–2048 KiB (共享)   |256 KiB (每核獨立)   |
    |L3 快取 (3rd Level Cache)  |視平台而定 (Platform dependent)   |2–8 MiB (共享)   |
- 個人看法與分析：
  - 能耗比優先 vs. 極致效能優先的架構分歧：
    - ARM Cortex-A53 採取 Static In-order 設計，避開了 Issue Queue、Reorder Buffer 與動態重命名等龐大硬體開銷，將功耗控制在僅 100 mW，非常適合對電池續航力極度敏感的行動裝置。
    - Intel Core i7 920 則是經典的 Dynamic Out-of-order ($IO_2I$) 架構，配合 4-Wide 吞吐量與 14 階深流水線，傾全力抽取程式中的指令層級平行度（ILP），但功耗也高達 130 W。
  - 靜態順序 vs. 動態亂序的效能代價：
    - 雖然 Cortex-A53 也是雙發射（2-Wide）處理器，但因為它是 In-order，一旦遭遇記憶體未命中（Cache Miss）或資料相依（RAW Hazard），流水線就會立刻 Stall；反之，Core i7 920 的亂序執行（OOO）與猜測執行能力能有效隱藏延遲，維持更高的實際 IPC。
- 總結：
  <br>本頁投影片透過直觀的對照表，呈現了 ARM Cortex-A53（順序執行、低功耗）與 Intel Core i7（亂序執行、高效能）在架構哲學上的選擇與取捨（Trade-off），完美總結了本單元關於「順序（In-order）」與「亂序（Out-of-order）」執行機制的應用情境。

## slide：30
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0030.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片為本章節的簡報大綱與進度轉換頁（Agenda）。畫面上高亮顯示了即將進入的核心主題：
  - 已完成主題（Grayed Out / Completed Topics）：
    - Out-of-Order Processors：亂序執行處理器架構與時序推導（已說明完畢）。
  - 當前重點主題（Highlighted Topic）：
    - Speculation and Branches（猜測執行與分支處理）：探討處理器如何結合分支預測（Branch Prediction）進行猜測執行，以及在猜測失敗（Misprediction）時如何利用 Reorder Buffer (ROB) 與 Pipeline Flush 安全地還原架構狀態。
  - 後續預告主題（Upcoming Topics）：
    - Register Renaming：暫存器重命名技術，用以消除 WAR（Write-After-Read）與 WAW（Write-After-Write）等假性數據相依（Name Dependencies）。
    - Memory Disambiguation：記憶體位址消歧義技術，用以處理 Load/Store 指令間的記憶體相依性與亂序存取安全。
- 個人看法與分析：
  - 從 Out-of-Order 跨入 Speculation 的必要性：
    - 前面幾頁討論的亂序發射與 In-order Commit 機制（如 $IO_2I$ 架構），其最大的實務價值之一就是為了支援猜測執行（Speculative Execution）。如果沒有 ROB 提供的「暫存且不寫入 ARF」機制，CPU 就無法在分支結果出來前先行執行後續指令。  
  - 學習邏輯的承先啟後：
    - 本頁代表課程從單純的「資料相依（RAW Hazard）與執行單元排程」，正式進階到「控制相依（Control Hazard）與猜測錯誤復原」的硬體設計層面，是現代亂序處理器最核心且複雜的設計環節之一。
- 總結：
  <br>本頁作為大綱索引頁，標示了課程進度正從「亂序處理器架構（Out-of-Order Processors）」轉移至「猜測執行與分支處理（Speculation and Branches）」，為接下來探討分支預測失敗恢復與控制流優化奠定基礎。

## slide：31
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0031.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片（SD4_page-0031.jpg）展示了在 傳統 $I_4$ 管道（In-order Frontend, In-order Issue, In-order Writeback, In-order Commit） 下，當程式遇到條件分支指令（Branch Instruction） 時，無猜測執行（No Speculation）與控制相依（Control Hazard）的時序處理機制：
  - 流水線結構與分支約束（$I_4$ Architecture Constraint）：
    - 下方微架構圖顯示，所有指令必須順序經過 $F \to D \to I \to (X/M/Y) \to W$ 階段。
    - 核心原則："No speculative instructions commit state"（不允許猜測的指令修改架構狀態）。在 $I_4$ 架構中，因為缺乏 Reorder Buffer (ROB) 來暫存猜測結果，分支指令必須確定結果（Taken / Not-Taken）後，後續的正確指令才能被 Issue/Execute。
  - 指令序列與時間軸（Instruction Trace Analysis）：
    - 0 mul  x1, x2, x3：週期 2 發射 ($I$)，週期 7 完成 $W$。
    - 1 addi x4, x5, 1：週期 3 發射 ($I$)，週期 8 完成 $W$。
    - 2 mul  x6, x1, x4：RAW 相依於指令 0（x1）與指令 1（x4），於週期 4~6 在 Issue Queue 等待 (I…I)，週期 7 發射進入 Y0 ，週期 11 完成 W。
    - 3 beq  x6, x0, Target：RAW 相依於指令 2 的 x6。
      - 於週期 3 完成 $F$、週期 4 完成 $D$。
      - 由於需要 x6 的計算結果，beq 於週期 5~10 在管道中等待/停頓 (D…D)。
      - 於週期 11 取得 x6 並發射至 $X_0$ 進行條件判斷，週期 15 完成 $W$。
    - 分支後的指令 4~6 (Sequential Stream) 與 Target (Jump Target)：
      - 控制阻塞（Control Stall）：指令 4 (addi x8, x9, 1) 雖然在週期 4 就已 Fetch ($F$)，但由於 beq（指令 3）結果未知，指令 4 被鎖在 Decode 階段 ($D\dots D$) 長達 4 個週期（週期 8~11），禁止發射。
      - 當週期 11 beq 確定分支成立（Branch Taken）後，流水線清空（Flush）原本預取的前段指令（指令 4、5、6 被標註 -- 廢棄）。
      - 正確的目标指令 T（Target）延後至週期 13 才開始 Fetch (F)，並於週期 14 Decode、週期 15 Issue。
- 個人看法與分析：
  <br>$I_4$ 架構面對 Control Hazard 的極大缺點：
  - 從時間軸可以清楚看到，因為不進行猜測執行（No Speculation），分支指令 beq 為了等待 x6 的算術結果，直接造成流水線停擺了整整 4 個週期。再加上確定 Taken 後清空前段指令的損失，目標指令 T 直到週期 13 才被 Fetch，產生了嚴重的分支懲罰（Branch Penalty）。
  - 引出猜測執行（Speculative Execution）的必要性：
    - 本頁範例是極佳的反面教材，展示了若不使用分支預測（Branch Prediction）與猜測執行（Speculation），高延遲指令（如 mul）接條件分支時會對流水線吞吐量造成多麼嚴重的打擊。這也順理成章地引出下一頁主題：如何透過 ROB 實現猜測執行以消除這類控制阻塞。
- 總結：
  <br>本頁展示了在傳統 $I_4$ 管道下，分支指令因數據相依而阻塞後續指令發射的時序過程。由於缺乏猜測執行機制，流水線必須等待分支結果完全確定後才能排程後續指令，導致嚴重的效能損失。此練習為接下來介紹「動態分支預測」與「基於 ROB 的猜測執行機制」提供了明確的對照基準。 

## slide：32
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0032.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片展示了在 $I_2O_2$ 微架構（In-order Frontend/Issue, Out-of-order Writeback/Commit） 下，面對條件分支指令（Branch Instruction）時的時序推導與控制相依處理：
  - 流水線結構特徵（ $I_2O_2$ Architecture Constraints）：
    - 前端與發射（In-order Frontend & Issue）：指令按順序 Decode 並進入發射隊列。
    - 寫回與提交（Out-of-order Writeback & Commit）：允許亂序寫回（ $W$），且沒有 Reorder Buffer (ROB)。
    - 核心限制："No speculative instructions commit state"（不允許猜測指令修改架構狀態）。由於 $I_2O_2$ 缺乏 ROB 暫存機制，一旦指令寫回（ $W$）就會直接破壞架構暫存器檔案（ARF）。因此，在分支指令（beq）確定結果前，後續指令絕對不能被 Issue 或執行。
  - 指令時序推導與流水線停頓（Pipeline Stall Analysis）：
    - 0 mul  x1, x2, x3：週期 2 發射 ($I$)，週期 7 完成 $W$。
    - 1 addi x4, x5, 1：週期 3 發射 ($I$)，週期 5 完成 $W$。
    - 2 mul  x6, x1, x4：RAW 相依於指令 0（x1），週期 7 發射 ($I$)，週期 11 完成 $W$。
    - 3 beq  x6, x0, Target：RAW 相依於指令 2 的 x6。
      - 週期 3 完成 $F$、週期 4 Decode。
      - 因等待 x6 完成，beq 在 Issue 階段停頓至週期 7，週期 7 發射進入 $X_0$，週期 8 完成 $W$（確定分支成立 Target）。  
    - 分支後指令 4~6 與 Target 指令 T 的互動：
      - 控制停頓（Control Stall）：指令 4 (addi x8, x9, 1) 雖然在週期 4 就已 Fetch ( $F$)，但由於 beq 結果未定，指令 4 被強制鎖在 Decode 階段 ( $D\dots D$) 長達 4 個週期（週期 7~10）。
      - 當週期 8 beq 寫回並確定 Branch Taken 後，前段預取的指令 4、5、6 於週期 11 被標註 -- 清空（Flush）。
      - 目標指令 T 延後至週期 12 才開始 Fetch ( $F$)，週期 13 Decode、週期 14 Issue。
- 個人看法與分析：
  <br>$I_2O_2$ 對比 $I_4$ 在分支處理上的異同：
  - 相同點：兩者都缺乏 ROB，因此都無法支援猜測執行（Speculative Execution）。後續指令（如指令 4）必須在 Decode 階段苦等分支指令算完結果，否則一旦提前執行並 Writeback，就會寫入 ARF 造成無法復原的錯誤。
  - 相異點（執行速度差異）：在 $I_2O_2$ 中，分支指令 beq 只需要 1 個算術週期（$X_0$）並於週期 8 完成寫回（$W$），比 $I_4$（需要順序經過 $X_0 \to X_1 \to X_2 \to X_3$，週期 15 才 $W$）快了許多。這使得目标指令 T 在 $I_2O_2$ 可以在週期 12 就 Fetch，大大縮短了分支懲罰（Branch Penalty）。
- 總結：
  <br>本頁展示了在無 ROB 的 $I_2O_2$ 架構下，分支指令對流水線造成的控制阻塞現象。雖然算術單元的亂序寫回加速了分支結果的產生，但由於缺乏猜測執行能力，系統仍必須暫停後續指令發射，進一步突顯了後續章節引進 ROB（Reorder Buffer） 實現 Speculation 的重要性。

## slide：33
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0033.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片（SD4_page-0033.jpg）展示了在 $I_2O_1$ 微架構（In-order Frontend/Issue, Out-of-order Writeback, In-order Commit） 下，當遇到條件分支指令（Branch Instruction）且未進行猜測執行（No Speculation）時的流水線時序推導與 squash/flush 清空機制：
  - 流水線結構特徵（ $I_2O_1$ Architecture Constraints）：
    - 前端與發射（In-order Frontend & Issue）：指令按原始程式順序進入 Decode 與 Issue。
    - 亂序寫回與順序提交（OOO Writeback, In-order Commit）：具備 Reorder Buffer (ROB) 與 Future Status Buffer (FSB)。寫回階段（ $W$）將結果寫入 PRF，但必須等 Commit 階段（ $C$）按順序寫入 ARF。
    - 控制保護原則（Squash Control）：
      - "Must squash instructions in pipeline after branch to prevent PRF write"：分支未確認前被預取的指令，若發現分支成立（Taken），必須在流水線中將其清空（Squash），防止其錯誤寫入 PRF。
      - "Can remove from ROB immediately or wait until commit"：被廢棄的猜測指令可以選擇立刻從 ROB 中移除，或者留在 ROB 直到輪到 Commit 時再被無聲忽略（Squash/Drop）。
  - 指令時序與流水線停頓（Pipeline Stall Analysis）：
    - 0 mul  x1, x2, x3：週期 2 發射 ( $I$)，週期 7 完成 $W$，週期 8 Commit ( $C$)。
    - 1 addi x4, x5, 1：週期 3 發射 ( $I$)，週期 5 完成 $W$，於 ROB 處於 $r$ 狀態等待，週期 9 Commit ( $C$)。
    - 2 mul  x6, x1, x4：RAW 相依於指令 0（ x1），週期 7 發射 ($I$)，週期 11 完成 $W$，週期 12 Commit ( $C$)。
    - 3 beq  x6, x0, Target：RAW 相依於指令 2 的 x6。
      - 週期 3 完成 $F$、週期 4 Decode。
      - 在 Issue 階段停頓等待 x6 至週期 7，週期 11 發射進入 $X_0$，週期 12 完成 $W$，週期 13 Commit ( $C$)。
    - 分支後指令 4~6 與 Target 指令 T 的互動：
      - 控制停頓（Control Stall）：指令 4 雖然在週期 4 完成 $F$，但因 $I_2O_1$ 未開放分支猜測發射，指令 4 被鎖在 Decode 階段 ( $D\dots D$) 長達 4 個週期（週期 7~10）。
      - 於週期 11 beq 發射並確定 Branch Taken 後，前段預取的指令 4、5、6 在週期 13 標註 -- 清空。
      - 目標指令 T 於週期 13 才開始 Fetch ($F$)，週期 14 Decode、週期 15 Issue。   
- 個人看法與分析：
  - ROB 在分支失敗（Misprediction/Branch Taken）時的作用：
    - 相較於 $I_2O_2$，引入 ROB 的 $I_2O_1$ 架構雖然在此範例中尚未開啟動態猜測發射（Speculative Issue），但 ROB 提供了清晰的指令生命週期管理。當分支結果確定 Taken 時，硬體可以直接無效化（Squash）流水線與 ROB 中該分支之後的所有指令條目，確保 PRF/ARF 的狀態絕對不受破壞。  
  - 效能瓶頸與下一步改進（引入 Speculative Execution）：
    - 在 $I_2O_1$ 架構下，因為 Issue 依然是 In-Order，使得 beq 必須苦等前面的 mul 算完才能進入發射。這種「等待分支算完才敢繼續發射」的保守作法帶來了顯著的流水線氣泡（Bubble）。要完全解放硬體效能，就必須結合 Branch Predictor（分支預測器） 與 Issue Queue（IQ，如 $IO_2I$ 架構），讓後續指令在分支結果未知時就能預先猜測發射與執行。
- 總結：
  <br>本頁展示了在具備 ROB 的 $I_2O_1$ 架構下，條件分支指令導致的控制停頓與流水線清空（Squash）過程。影片說明了 ROB 如何作為保護架構狀態（ARF/PRF）的屏障，並為下一階段將介紹的「結合分支預測的猜測執行（Speculative Execution with Branch Prediction）」建立了關鍵概念。

## slide：34
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0034.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片展示了在 $IO_3$ 微架構（In-order Frontend, OOO Issue/Writeback/Commit） 下，當遭遇條件分支指令（Branch Instruction）時，缺乏控制猜測（No Control Speculation）所導致的致命缺陷——猜測指令非預期地寫入架構暫存器檔案（ARF）：
  - 流水線結構特徵（$IO_3$ Architecture Constraints）：
    - 前端順序，後端全亂序（In-order Frontend, OOO Issue/WB/Commit）：具備 Issue Queue (IQ)，允許指令亂序發射與寫回。
    - 缺乏 Reorder Buffer (ROB)：寫回階段（ $W$）直接將計算結果寫入 ARF（Architectural Register File）。
    - 控制猜測限制（No Control Speculation）：
      - "No control speculation for $IO_3$"：因為缺乏 ROB 的暫存機制，如果盲目猜測發射分支後續的指令，其結果一旦寫回就會不可逆地破壞 ARF。
      - "Could stall on branch"：如果不進行控制猜測，流水線就必須在分支指令確定結果前停頓。
  - 指令時序與錯誤情況推導（Pipeline Timing & Failure Analysis）：
    - 0 mul  x1, x2, x3：週期 2 發射 ( $I$)，週期 7 完成 $W$。
    - 1 addi x4, x5, 1：週期 3 發射 ($I$)，週期 5 完成 $W$。
    - 2 mul  x6, x1, x4：RAW 相依於指令 0（ x1），於 Issue Queue (IQ) 中等待至週期 7 發射 ( $I$)，週期 11 完成 $W$。
    - 3 beq  x6, x0, Target：RAW 相依於指令 2 的 x6。
      - 於週期 3 完成 $F$、週期 4 Decode、進入 IQ ( $i$)。
      - 在 IQ 中等待 x6 的結果直到週期 10，週期 11 才發射 ($I$) 進入算術單元 $X_0$，週期 12 完成 $W$（確定 Branch Taken）。
    - 分支後續指令（指令 4~6）的錯誤寫入（The Hazard of Speculation without ROB）：
      - 指令 4 (addi x8, x9, 1) 與指令 5 (addi x10, x11, 1) 沒有資料相依，於週期 7 與 8 提前發射 ( $I$) 並於週期 8 與 9 完成寫回 ( $W$)。
      - 指令 6 (addi x12, x13, 1) 於週期 11 發射 ( $I$)，週期 12 完成 $W$。
      - 致命後果：當週期 12 分支指令 beq 終於確定 Branch Taken 並準備跳轉至 Target (T) 時，指令 4、5、6（Speculative Instructions）早就已經將結果寫入 ARF（"Speculative Instructions Wrote to ARF"）。由於沒有 ROB 進行復原（Rollback），這些被錯誤執行的指令狀態無法撤銷，導致程式執行結果出錯！
      - 正確的目标指令 T 延後至週期 12 才開始 Fetch ($F$)。
- 個人看法與分析：
  - 展示「沒有 ROB 就不能做猜測執行」的經典案例：
    - 本頁範例極具啟發性。它清楚說明了為什麼 $IO_3$（亂序發射/寫回但無 ROB）在實務上不能對分支進行猜測執行（No Control Speculation）。如果不加以限制，讓 IQ 隨意發射分支後的指令，就會發生圖中指令 4、5、6 污染 ARF 的災難。
  - 修正方法與微架構演進：
    - 若要在 $IO_3$ 中避免此問題，系統必須在 Decode/Issue 階段強制 Stall 分支後的指令（直到 beq 完成），但這會嚴重削弱超純量處理器的效能。
    - 這正是為什麼現代高效能處理器必定採用 $IO_2I$ 架構（In-order Frontend, OOO Issue/WB, In-order Commit with ROB）——唯有配合 Reorder Buffer (ROB)，才能讓猜測指令的結果先「暫存」在 ROB 中，等到分支結果確定正確後才 Commit 到 ARF，若預測失敗則可直接 Flush 清空，同時兼顧高效能與安全性。
- 總結：
  <br>本頁投影片透過完整的時序圖，深刻示範了在缺乏 ROB 的 $IO_3$ 架構下進行猜測執行所帶來的狀態破壞風險。這也為本單元的架構比較畫下圓滿句點，說明了為何 ROB（Reorder Buffer） 是現代處理器實現「安全猜測執行（Safe Speculative Execution）」不可或缺的微架構元件。   

## slide：35
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0035.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片展示了在現代主流 $IO_2I$ 微架構（In-order Frontend, OOO Issue/Writeback, In-order Commit） 下，當遭遇條件分支指令（Branch Instruction）且進行猜測執行（Speculative Execution）時，流水線的時序推導與選取性還原機制（Selective Rollback）：
  - 流水線結構特徵（$IO_2I$ Architecture Constraints）：
    - 前端順序（In-order Frontend）：指令按順序經過 Fetch ( $F$)、Decode ( $D$)，並進入 Issue Queue (IQ, $i$)。
    - 後端亂序發射與寫回（OOO Issue & Writeback）：只要資料準備就緒，IQ 中的指令可亂序發射（ $I$）並寫回結果（ $W$）至 PRF（Physical Register File）。
    - 順序提交（In-order Commit with ROB）：配置 Reorder Buffer (ROB) 與 Future Status Buffer (FSB)。指令必須按原始程式順序提交（ $C$）並將結果寫入 ARF。
  - 指令時序與猜測錯誤還原推導（Timing & Selective Rollback Analysis）：
    - 0 mul  x1, x2, x3：週期 2 發射 ( $I$)，週期 7 完成 $W$，週期 8 Commit ( $C$)。
    - 1 addi x4, x5, 1：週期 3 發射 ( $I$)，週期 5 完成 $W$，於 ROB 處於 $r$ 狀態等待，週期 9 Commit ( $C$)。
    - 2 mul  x6, x1, x4：RAW 相依於指令 0（x1），於 IQ 中等待至週期 7 發射 ( $I$)，週期 11 完成 $W$，週期 12 Commit ( $C$)。
    - 3 beq  x6, x0, Target：RAW 相依於指令 2 的 x6。
      - 於週期 3 完成 $F$、週期 4 Decode、進入 IQ ( $i$)。
      - 在 IQ 中等待 x6 至週期 10，週期 11 發射 ( $I$) 進入算術單元 $X_0$，週期 12 完成 $W$（確定 Branch Taken），週期 13 Commit ( $C$)。
    - 分支猜測執行與還原（Speculative Execution & Rollback）：
      - 指令 4 (addi x8, x9, 1) 與指令 5 (addi x10, x11, 1) 在分支結果出來前（週期 7 與 8）即被猜測性地發射與執行（Speculative Issue），並分別於週期 8 與 9 將結果寫入 PRF（標示為 $W$ 與 $r$）。
      - 分支預測失敗處置（Branch Misprediction Handling）：當週期 11 分支指令 beq 發射並於週期 12 確定 Branch Taken 時，系統檢測到猜測錯誤：
        - Pipeline Flush：清空前段流水線（指令 4~11 被標註 -- 廢棄）。
        - Selective Rollback / PRF Cleanup："Need to clean up Speculative state In PRF. Needs selective rollback"。由於指令 4、5 的結果僅寫入 PRF/ROB 而尚未 Commit 到 ARF，系統只需透過暫存器重命名對照表（Rename Map Table）回復狀態，並釋放指令 4、5 佔用的 PRF 條目即可完成安全還原。
      - 正確的目标指令 T（Target）於週期 13 順利開始 Fetch ($F$)，週期 14 Decode、週期 15 Issue。
- 個人看法與分析：
  <br>$IO_2I$ 完美解決 $IO_3$ 的 ARF 污染問題：
  - 相較於前一頁 $IO_3$ 架構因缺乏 ROB 而導致猜測指令不可逆地污染 ARF 的重大缺陷，$IO_2I$ 透過 ROB + PRF 建立了「隔離層」。猜測執行的結果會被安全地鎖在 PRF 與 ROB 中，只有確認分支預測正確時才允許寫入 ARF（Commit）。
  - 猜測失敗的代價（Misprediction Penalty）：
    - 雖然 $IO_2I$ 能夠完美保障精確例外與架構狀態正確性，但選取性還原（Selective Rollback）與清空流水線（Flush）依然產生了約 2~3 個週期的時間氣泡。這也說明了為什麼現代處理器除了 $IO_2I$ 架構外，還需要極度精準的分支預測器（Branch Predictor）來盡可能降低預測失敗率。
- 總結：
  <br>本頁投影片作為猜測執行與分支處理單元的完結頁，完整展示了 $IO_2I$ 架構如何利用 ROB 與 PRF 實現「安全的猜測執行」與「高效的狀態還原（Selective Rollback）」。這是現代高效能 CPU 設計中最為關鍵且成功的微架構典範。

## slide：36
<div align="left" >
  <img src="./Lecture/SD4/SD4_page-0036.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片展示了在 $IO_2I$ 微架構（In-order Frontend, OOO Issue/WB, In-order Commit） 下，分支預測失敗（Misprediction）時，系統如何透過 ARF 與 PRF 之間的狀態同步 來完成狀態復原：
  - 流水線狀態與分支 Commit（Pipeline State & Branch Commit）：
    - 指令序列時序：
      - 0 mul  x1, x2, x3 與 1 addi x4, x5, 1 分別於週期 8 與週期 9 完成 Commit ( $C$)。
      - 2 mul  x6, x1, x4 於週期 12 完成 Commit ($C$)。
      - 3 beq  x6, x0, Target 於週期 11 發射 ($I$)、週期 12 完成 $W$，並於週期 13 完成 Commit ($C$)。
    - 猜測指令狀態（Speculative State）：
      - 指令 4 (addi x8, x9, 1) 與指令 5 (addi x10, x11, 1) 在週期 7 與 8 提前發射並執行，將計算結果寫入 PRF 並標示為 $r$ 狀態。
      - **核心差異**：投影片右側特別強調 "Speculative Instructions Wrote to PRF, Not ARF"（猜測指令的結果僅寫入實體暫存器 PRF，並未污染架構暫存器 ARF）。
  - 分支預測失敗還原機制（Misprediction Recovery Mechanism）：
    - "Copy ARF to PRF on Mispredict"：當週期 13 分支指令 beq Commit 並確認分支成立（Branch Taken / Mispredicted）時，處理器直接將 ARF 的正確架構狀態複製/同步回 PRF（或重新指向映射表 Map Table），瞬間將猜測指令（4、5、6）對 PRF 所作的修改全數清空與廢棄。
    - 流水線重置與重新 Fetch：
      - 流水線中所有未 Commit 的猜測指令（指令 4~12 被標註 --）均被 Squash 清空。
      - 正確的分支目標指令 T（Target）於週期 14 開始 Fetch ($F$)，週期 15 Decode、週期 16 Issue。
- 個人看法與分析：
  - 狀態復原（Rollback）的硬體設計巧思：
    - 在 $IO_2I$ 架構中，因為所有指令都必須在 ROB 中順序 Commit，所以 ARF 中永遠保存著「確定正確的歷史架構狀態」。當分支預測失敗時，只需執行 "Copy ARF to PRF"（或重置 Rename Map Table），就能以極低代價將 PRF 恢復到分支發生前一刻的正確狀態，完全避免了前幾頁 $IO_3$ 架構中 ARF 被永久破壞的災難。
  - 時序懲罰（Misprediction Penalty）的折衷：
    - 相較於前一頁在分支 Writeback（$W$）階段就進行 Selective Rollback 的作法，本頁展示的是在分支 Commit（$C$）階段才統一進行 Flush & Recovery 的情境。雖然目標指令 T 延後至週期 14 才 Fetch（比起在 $W$ 階段復原晚了 1~2 個週期），但硬體控制邏輯相對簡單且更為穩健。
- 總結：
  <br>本頁投影片透過完整的時序細節，清楚演繹了 $IO_2I$ 架構如何利用 ARF 作為安全底線（Safe Baseline），在分支預測失敗時藉由「將 ARF 複製回 PRF」與 Pipeline Flush 實現精確的狀態還原。這完整示範了現代亂序 CPU 兼具高執行效率與精確例外/錯誤復原能力的微架構機制。 

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
















