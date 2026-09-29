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
















