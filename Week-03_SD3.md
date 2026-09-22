Prompt：請說明本教學重點內容及你的看法，最後以250字內總結
### Week 3 課堂逐字稿

## slide：1 -2
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0001.jpg" width="49%">
  <img src="./Lecture/SD3/SD3_page-0002.jpg" width="49%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：3
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0003.jpg" width="50%">
</div>

## slide：4
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0004.jpg" width="50%">
</div>

## slide：5
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0005.jpg" width="50%">
</div>

## slide：6
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0006.jpg" width="50%">
</div>

## slide：7
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0007.jpg" width="50%">
</div>

## slide：8
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0008.jpg" width="50%">
</div>

## slide：9
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0009.jpg" width="50%">
</div>

## slide：10
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0010.jpg" width="50%">
</div>

## slide：11
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0011.jpg" width="50%">
</div>

## slide：12
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0012.jpg" width="50%">
</div>

## slide：13
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0013.jpg" width="50%">
</div>

## slide：14
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0014.jpg" width="50%">
</div>

## slide：15
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0015.jpg" width="50%">
</div>

## slide：16
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0016.jpg" width="50%">
</div>

## slide：17
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0017.jpg" width="50%">
</div>

## slide：18
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0018.jpg" width="50%">
</div>

## slide：19
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0019.jpg" width="50%">
</div>

## slide：20
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0020.jpg" width="50%">
</div>

## slide：21
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0021.jpg" width="50%">
</div>

## slide：22
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0022.jpg" width="50%">
</div>

## slide：23
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0023.jpg" width="50%">
</div>

## slide：24
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0024.jpg" width="50%">
</div>

## slide：25
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0025.jpg" width="50%">
</div>

## slide：26
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0026.jpg" width="50%">
</div>

## slide：27
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0027.jpg" width="50%">
</div>

## slide：28
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0028.jpg" width="50%">
</div>

## slide：29 五階段管線（5-Stage Pipeline）中的異常處理（Exception Handling）機制
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0029.jpg" width="50%">
</div>

這張投影片討論的是五階段管線（5-Stage Pipeline）中的異常處理（Exception Handling）機制
- 投影片重點內容
  - 各管線階段可能發生的異常類別：
    - IF / PC 階段：PC 位址異常（PC address Exception）。
    - ID 階段：非法指令碼（Illegal Opcode）。
    - EX 階段：未對齊的跳躍目標位址（Misaligned branch target）。
    - MEM 階段：資料位址異常（Data address Exceptions）
    - 全階段：非同步中斷（Asynchronous Interrupts，如外部硬體中斷）。
  - 核心核心探討議題：
    - 當多個異常同時在不同管線階段觸發時，系統該如何進行優先順序處理與協調？
    - 外部非同步中斷應該在何時、何處（哪一個階段）被妥善處理？
- 個人看法：<br>在 CPU 設計中，異常處理是確保系統穩定運作與實現「精確中斷（Precise Interrupt）」的關鍵技術。
  - 挑戰點：管線化的優勢在於指令交錯執行，但這也代表「後進去的指令（較早階段）」可能會比「先進去的指令（較晚階段）」更早觸發異常。如果沒有妥善管理，會導致指令狀態混亂。
  - 解決方向：通常設計上會將各階段產生的異常標記在流水線暫存器（Pipeline Register）中，隨指令一路傳遞，直到 WB（寫回）階段前統一按指令順序處理，以確保程式執行狀態的正確性與可預測性。
- 總結：<br>本教學聚焦於五階段 CPU 管線中的異常處理機制，說明 PC 位址錯誤、非法指令、位址未對齊及資料異常會分別發生於不同階段。核心課題在於如何協調多個階段同時發生的異常，以及如何妥善處理解析外部非同步中斷，以維持系統執行的精確性與穩定性。


## slide：30
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0030.jpg" width="50%">
</div>

## slide：31
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0031.jpg" width="50%">
</div>

## slide：32
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0032.jpg" width="50%">
</div>

## slide：33
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0033.jpg" width="50%">
</div>

## slide：34
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0034.jpg" width="50%">
</div>

## slide：35
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0035.jpg" width="50%">
</div>

## slide：36
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0036.jpg" width="50%">
</div>

## slide：37
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0037.jpg" width="50%">
</div>

這張投影片主題為 「I4: In-Order Front-End, Issue, Writeback, Commit」，展示了一個經典的 5 階段順序處理管線（In-Order Pipeline）架構。
- 本教學重點內容：
  - 基本 5 階段管線架構（5-Stage Pipeline）：
    - F (Fetch，取指)：從指令記憶體讀取指令。
    - D (Decode / Issue，譯碼 / 發射)：解析指令並讀取暫存器，順序發射至執行階段。
    - X (Execute，執行)：由算術邏輯單元（ALU）進行運算或計算位址。
    - M (Memory，記憶體存取)：讀取或寫入資料記憶體。
    - W (Writeback / Commit，寫回 / 提交)：將結果寫回暫存器檔案，完成指令提交。
  - 「In-Order」（順序）核心特徵：
    - 從前端取指（Front-End）、發射（Issue）、寫回（Writeback）到最後的提交（Commit），指令全過程皆按照程式碼原始順序進行處理。
- 個人看法：
  <br>這張投影片代表了微架構設計中最基礎、最標準的 CPU 基準模型（Baseline Architecture）。
  - 優點：架構簡單、控制邏輯直觀，且因為所有階段均為順序（In-Order），能天然地支援精確中斷（Precise Interrupts）與簡單的流水線暫存器設計。
  - 局限：當發生長延遲操作（如 Memory Miss）或指令間資料相依（Data Hazard）時，整個管線容易發生停頓（Stall）。這也是後續課程探討「亂序執行（Out-of-Order）」與「超純量（Superscalar）」架構的關鍵背景與理由。
- 總結：<br>本投影片展示經典 5 階段順序管線（F-D-X-M-W），強調指令在前端取指、發射、寫回與提交全程皆按原始順序執行。此架構設計簡單且易於維持精確中斷，但面對資料相依與記憶體延遲時易生停頓。它是學習亂序執行與超純量處理器等進階微架構的最佳基礎標竿。


## slide：38
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0038.jpg" width="50%">
</div>

這張投影片展現了包含多條非對稱執行管線（Asymmetric Execution Pipelines）的進階 In-Order 架構。
- 本教學重點內容：
  - 多路/異構執行階段（Multiple Execution Paths）：
    - 前端（F, D）：指令順序進行取指（Fetch）與譯碼/發射（Decode/Issue）。
    - 分支執行管線：
      - ALU/算術路徑 ($X_0 \to X_1$)：處理一般的算術與邏輯運算
      - Memory/記憶體路徑 ($M_0 \to M_1$)：處理 Load/Store 等記憶體存取操作。
    - 後端（W）：兩條平行路徑運算完成後，匯合至 Writeback（寫回）階段進行結果提交。
  - 核心挑戰：結構衝突與結構冒險（Structural Hazards）：
   - 由於不同的執行路徑具備相同的流水線長度（皆為 2 階段），若不同類型的指令同時進入各自路徑，可能面臨同時抵達 W 階段搶奪 Write Port（寫回埠）的衝突。
- 個人看法：<br>這張圖是從單一流水線走向異構多執行單元（Asymmetric/Multi-pipeline Structure）的核心過渡模型。
  - 優點：允許不同類型的指令（如算術運算與記憶體存取）進行重疊與平行處理，提升了硬體資源利用率。
  - 隱憂與挑戰：雖然執行階段分流，但寫回埠（W Stage）成為集中的瓶頸點。若沒有設計適當的 Arbitration（仲裁）或 Stall（停頓）邏輯，極易產生寫回衝突；此外，不同執行時間也可能引發 WAW 或 RAW 等資料相依（Data Hazards）問題。
- 總結：
  <br>本投影片展示包含算術與記憶體分流的雙路順序管線架構（F-D-$X_0$/$M_0$-$X_1$/$M_1$-W）。重點在於說明指令譯碼後可依類型分派至不同執行路徑以提升平行度。然而，異構路徑最終匯合於同一 Writeback 階段，會衍生寫回埠競爭與資料相依問題，是設計管線仲裁與控制邏輯的關注焦點。

## slide：39
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0039.jpg" width="50%">
</div>

這張投影片介紹的是具備長延遲執行路徑（4-stage MUL）的順序管線架構。
- 本教學重點內容：
  - 非對稱的多階段執行路徑（Asymmetric Multi-Stage Execution）：
    - 取指與發射（F, D）：前級仍維持順序處理。
    - 多路平行執行單元：
      - 一般算術路徑 ($X_0 \to X_1$)：耗時較短（2 階段）。
      - 記憶體路徑 ($M_0 \to M_1 \to M_2 \to M_3$)：4 階段設計。
      - 乘法/複雜運算路徑 ($Y_0 \to Y_1 \to Y_2 \to Y_3$)：4 階段設計（4-stage MUL）。
    - 寫回階段（W）：所有執行單元算完後皆匯入 W 階段寫回暫存器。
  - 效能與硬體開銷的權衡（Trade-off）：
    - 全旁路（Full Bypassing）：為了避免長延遲運算拉高 CPI（降低效能），硬體需要極為複雜且昂貴的全旁路 forwarding 電路。
    - 新增 Issue 階段：為了維持與優化時脈週期時間（Cycle time），將暫存器讀取與指令發射（Issue）至功能單元（Functional Unit）的步驟獨立或優化處理。
- 個人看法：<br>此架構反映出真實 CPU 處理器在面對「不同運算需要不同週期」時的折衷設計。
  - 優點：允許乘法或長記憶體存取等慢速運算管線化（Pipelined），不至於讓簡單的 ALU 運算被卡住，有助於維持高 throughput。
  - 瓶頸與複雜度：由於執行路徑長度不一（2 階段 vs. 4 階段），若較晚發射的短指令比較早發射的長指令先算完，會產生 WAW 衝突 或 亂序寫回（Out-of-Order Completion） 的問題；且跨長度的 Bypassing 電路會讓晶片面積與功耗大增。
- 總結：
  <br>本投影片展示包含 4 階段乘法器與記憶體路徑的多管道順序 CPU 架構。重點說明長延遲運算單元雖能提高平行度，但需要極昂貴的全旁路電路以避免 CPI 增加，同時需獨立發射階段來確保時脈週期效能，並進一步衍生了結構衝突與寫回順序控制的挑戰。

## slide：40
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0040.jpg" width="50%">
</div>

這張投影片主題為 「I4: In-Order Front-End, Issue, Writeback, Commit (4-stage MUL)」，進一步展示了引入Scoreboard（記分板）與ARF（架構暫存器檔案）機制後的完整順序管線結構。
- 本教學重點內容：
  - 結構組件與階段分工：
    - 前端階段（F, D, I）：除了取指（Fetch）與譯碼（Decode）外，獨立出 I (Issue，發射) 階段，並在此階段結合 SB (Scoreboard) 進行相依性檢查與暫存器讀取。
    - 多路執行單元：包含 2 階段算術路徑 ($X_0 \to X_1$)、4 階段記憶體路徑 ($M_0 \to \dots \to M_3$) 與 4 階段乘法路徑 ($Y_0 \to \dots \to Y_3$)。
    - 寫回階段（W）：將結果寫回 ARF (Architectural Register File)。
  - 硬體狀態維護機制（ARF vs. SB）：
    - ARF（架構暫存器檔案）：在 I 階段進行讀取（R），並在 W 階段進行寫入（W），儲存程式當前的實際架構狀態。
    - SB（記分板）：在 I 階段進行讀取與更新（R/W） 以檢查 hazard，並在 W 階段釋放狀態（W）。
- 個人看法：<br>這張投影片展現了硬體如何透過輕量化控制模組（Scoreboard）來管理具備非對稱延遲的多管線架構。
  - 優點：Scoreboard 能在 I 階段精確追蹤哪些暫存器正被長延遲運算（如 4-stage MUL）佔用，有效防範 RAW/WAW 等 Data Hazards 與 Writeback 競爭。
  - 局限：因為 Front-End 與 Issue 仍嚴格保持順序（In-Order），只要前方的指令被 SB 擋住（Stall），後方無相依性的指令也無法超越執行，硬體平行度的發揮仍受限於順序發射的本質。
- 總結：
  <br>本投影片介紹結合 Scoreboard (SB) 與 ARF 的 4 階段乘法順序管線架構。重點說明在 Issue 階段利用 SB 進行動態相依性檢查與暫存器讀取，並於 Writeback 階段更新 ARF。此機制能精確管控多路執行路徑的 Hazards 與資源競爭，是向亂序執行（Out-of-Order）邁進的關鍵過渡設計。

## slide：41
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0041.jpg" width="50%">
</div>

這張投影片主題為 「Basic Scoreboard（基礎記分板）」，詳細展示了 Scoreboard 控制邏輯的硬體結構與運作原理。
- 本教學重點內容：
  - 記分板表格欄位結構（Table Fields）：
    - P (Pending)：標示是否有指令正在執行中，且準備寫入該目標暫存器（In-flight）。
    - F (Functional Unit)：紀錄當前是由哪一個功能單元（Functional Unit）負責寫入該暫存器。
    - Data Avail. (Data Availability)：以 Bit-vector（如欄位 $4, 3, 2, 1, 0$）追蹤運算結果資料位於功能單元流水線的哪一階段。
  - 動態追蹤與旁路（Bypassing）機制：
    - 位置標示：Data Avail. 欄位中的 $1$ 代表結果資料當前處於該 Functional Unit 的第 $l$ 階段；若 $1$ 推進至 column 0，則表示該指令已進入 Writeback（寫回）階段。
    - 資料旁路仲裁：結合 F 與 Data Avail. 欄位資訊，系統能精確判定結果資料何時、何處可用，以控制旁路（Bypassing/Forwarding）線路的開啟 timing。
    - 時脈位移：每經過一個時脈週期（Cycle），Data Avail. 欄位中的 Bit 會向右位移（Shift right）一個位置，反映資料在管線中的推進。
- 個人看法：<br>Scoreboard 是動態排程（Dynamic Scheduling）極為經典的控制心臟。
  - 優點：相較於完全靜態的編譯器排程，Scoreboard 透過簡單的狀態表（Bit-shifting）即可在硬體端動態追蹤多路流水線的資料進度，有效解決 Data Hazards 並控制 Bypassing 時機。
  - 局限：傳統 Scoreboard 通常僅追蹤 RAW hazard 與結構衝突；若沒有搭配暫存器重命名（Register Renaming）技術，在面對 WAW 或 WAR 衝突時仍需要 Stall 管線，這也是後續發展出 Tomasulo 演算法的重要動機。
- 總結：
  <br>本投影片說明 Basic Scoreboard 的硬體結構與運算機制，利用 Pending (P)、Functional Unit (F) 及 Data Availability 欄位動態監控暫存器寫回狀態。透過狀態 Bit 每週期右移的特性，系統能精確仲裁資料旁路（Bypassing）時機並解除相依性停頓，是硬體動態排程與 hazard 控制的關鍵核心。

## slide：42
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0042.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：43
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0043.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：44
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0044.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：45
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0045.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：46
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0046.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：47
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0047.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：48
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0048.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：49
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0049.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：50
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0050.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：






















