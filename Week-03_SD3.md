Prompt：請說明本教學重點內容及你的看法，最後以250字內總結
### Week 3 課堂逐字稿

## slide：1 -2
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0001.jpg" width="49%">
  <img src="./Lecture/SD3/SD3_page-0002.jpg" width="49%">
</div>

- 本教學重點內容：
  - 課程影片上傳（Course video uploaded）：提示學生本週或最新的課程教學影片已經上傳至平台，可供學生觀看與複習。
  - Lab 1 作業繳交期限（Lab1 due next week）：公告實驗作業 Lab 1 將於下週截止繳交（Due next week）。
- 個人看法：
  - 這是一張典型且標準的課程開場與行政宣導投影片。
  - 教學目的：在正式進入複雜的微架構（如 Scoreboard、管線控制）等硬體技術主題前，先明確告知學生課務進度與實驗作業的時間節點，能幫助學生規劃時間與完成實務實作。
- 總結：
  <br>本投影片為課務行政公告，提醒學生課程影片已上傳，並通知 Lab 1 實驗作業將於下週截止繳交，提醒學生規劃時間完成學習與作業。

## slide：3
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0003.jpg" width="50%">
</div>

這張投影片主題為 「Types of Data Hazards（資料冒險/資料相依性的類型）」。
- 本教學重點內容：
  - 資料相依性（Data-dependence）與 Hazards 類型：<br>對於指令序列 $r_k \leftarrow r_i \text{ op } r_j$，依據資料讀寫順序可分為三類： 
    - RAW (Read-after-Write) / 真資料相依（Data-dependence）：後續指令需要讀取前指令尚未寫入的暫存器（例如 $r_3 \leftarrow r_1 \text{ op } r_2$ 後接 $r_5 \leftarrow r_3 \text{ op } r_4$）。這是真正的資料相依。
    - WAR (Write-after-Read) / 反相依（Anti-dependence）：後續指令試圖寫入前指令正在讀取的暫存器（例如 $r_3 \leftarrow r_1 \text{ op } r_2$ 後接 $r_1 \leftarrow r_4 \text{ op } r_5$）。
    - WAW (Write-after-Write) / 輸出相依（Output-dependence）：兩條指令試圖寫入同一個暫存器（例如 $r_3 \leftarrow r_1 \text{ op } r_2$ 後接 $r_3 \leftarrow r_6 \text{ op } r_7$）。
- 個人看法：
  <br>這張投影片是理解動態排程（如 Scoreboard 或 Tomasulo 演算法）的基礎核心。
  - RAW vs. WAR/WAW 的本質差異：RAW 代表真正的資料傳遞（真相依），無法憑空消除，必須透過 Forwarding/Bypassing 或 Stall 來解決；而 WAR 與 WAW 屬於「名字相依（Name Dependence）」，僅是因為暫存器數量有限而重複使用相同暫存器名稱所致。
  - 設計延伸：傳統的 Scoreboard 透過在 Issue 階段停頓指令來處理解決 WAW hazard；而更進階的處理器（如 Tomasulo 架構）則透過「暫存器重命名（Register Renaming）」完全消除 WAR 與 WAW，極大地解放了指令平行度（ILP）。
- 總結：
  <br>本投影片介紹了三種資料冒險：RAW（讀後寫）、WAR（寫後讀，反相依）與 WAW（寫後寫，輸出相依）。RAW 為真實資料相依，需透過轉發或停頓解決；WAR 與 WAW 則為暫存器名稱重複使用造成的假性相依，是後續管線設計與動態排程（如暫存器重命名）必須識別與克服的核心問題。

## slide：4
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0004.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：5
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0005.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：6
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0006.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：7
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0007.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：8
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0008.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：9
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0009.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：10
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0010.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：11
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0011.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：12
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0012.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：13
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0013.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：14
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0014.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：15
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0015.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：16
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0016.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：17
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0017.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：18
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0018.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：19
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0019.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：20
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0020.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：21
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0021.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：22
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0022.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：23
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0023.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：24
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0024.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：25
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0025.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：26
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0026.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：27
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0027.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：28
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0028.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

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

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：31
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0031.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：32
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0032.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：33
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0033.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：34
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0034.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：35
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0035.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：36
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0036.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

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

這張投影片主題為 Scoreboard 在包含長延遲單元（如 4-stage MUL）管線中的具體指令執行追蹤與模擬。
- 本教學重點內容：
  - 指令序列與相依性關係（Instruction Sequence & Hazards）：
    - 範例程式碼包含 7 條指令（0: mul, 1: addi, 2: mul, 3: mul, 4: addi, 5: addi, 6: addi）。
    - RAW 相依性（Data Hazard）：例如指令 2 (mul x5, x1, x4) 依賴指令 0 (mul x1, x2, x3) 的寫入結果 x1；指令 3 依賴指令 2 的 x5。
    - WAW / 資源衝突：不同長度的執行路徑（2-stage ALU vs 4-stage MUL）會導致後發射的短指令試圖與先發射的長指令在同一週期寫回，需要透過 Scoreboard 控制。
  - 時間軸模擬（Cycle-by-Cycle Execution Timeline）：
    - 投影片下方標示的數字 $0 \sim 18$ 代表時間軸（Clock Cycles）。
    - 透過這個架構，學生需要逐步推算每條指令進入 F（Fetch）、D（Decode）、I（Issue/Scoreboard Read）、EX/MEM/MUL 執行階段 與 W（Writeback） 的精確時脈週期。
- 個人看法：
  <br>這是計算機架構課程中極為經典且重要的「手動管線追蹤（Pipeline Trace）」題目。
  - 教學目的：光看理論抽象概念（如 Scoreboard 結構）不足以理解細節，透過這種精確到 Clock Cycle 的模擬，能讓學生深刻體會到當發生 RAW/WAW hazard 時，Scoreboard 是如何動態發出 Stall（停頓）訊號，以及全旁路（Full Bypassing）硬體是如何省去等待週期。
  - 實務效益：理解這種非對稱管線的停頓與寫回衝突，是進一步邁向 Superscalar（超純量）與 Out-of-Order（亂序執行，如 Tomasulo 演算法）設計的核心基礎。   
- 總結：
  <br>本投影片提供具備 4 階段乘法器與 Scoreboard 管線的時間軸模擬範例。透過包含資料相依性（如 x1, x5 的 RAW hazard）的 7 條指令序列，展示指令在時脈週期 $0 \sim 18$ 間的推移過程。重點在於驗證 Scoreboard 如何動態偵測 Hazards 並仲裁暫存器寫回與旁路時機。 

## slide：43
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0043.jpg" width="50%">
</div>

這張投影片展現了 Scoreboard（記分板）動態排程在具備多路非對稱執行管線（含 4 階段 MUL）中的實際運算日誌（Execution Trace）與狀態轉移。
- 本教學重點內容：
  - 具體指令序列的管線推移（Pipeline Flow）：
    - RAW Hazard（資料相依性）處理：例如指令 0 (mul x1, x2, x3) 產生的結果 x1 被指令 2 (mul x5, x1, x4) 依賴。投影片顯示指令 2 在 Issue (I) 階段停頓（Stall）多個週期（Cyc 4~6），直到指令 0 完成並進行旁路（Bypassing）才解鎖發射。
    - 多路發射與阻塞：後方無相依或有相依的指令（如 addi）受到前面指令停頓的影響，在 Decode (D) 或 Issue (I) 階段形成佇列等待。
  - 記分板內部狀態變化與旁路判定（Scoreboard State & Bypassing）：
    - 下方表格展示了每一週期（Cyc 1~18）Data Avail. 欄位位元陣列（Bit-vector）右移與目標暫存器（Dest Regs, 如 x1, x11, x5 等）標記的演變。
    - 紅色數字標示：代表透過檢查 F 欄位與 Data Avail. 狀態，硬體可以在該週期觸發資料旁路（Bypass），將運算結果直接 Forwarding 至需要該資料的功能單元，避免額外的寫回等待週期。
    - 提出的隨堂問題：「What does the scoreboard look like at cycle 7?」，要求分析在第 7 個週期時 SB 各欄位的數值狀態。
- 個人看法：<br>**這張圖是整章微架構動態排程教學的最精髓精華**。
  - 實務價值：它透過文字化的流水線時間軸與表格狀態圖解，把「抽象的控制邏輯」轉化為「可驗證的演算法狀態演進」。讀者能清晰看到 Scoreboard 如何精確計算 Data Avail. 的位移（Shift）來抓準 Bypassing 時間點。
  - 瓶頸體會：從時間軸可以看出，即使引進了 Scoreboard 與 Bypassing，指令 2 仍因為前面長延遲的乘法運算而在 I 階段被卡住很久。這極大地凸顯了「In-Order Issue」的效能天花板，自然而然為後續引出「Out-of-Order Issue（如 Tomasulo 演算法與 Reservations Stations）」打下了最堅實的理論基礎。
- 總結：
  <br>本投影片透過 7 條指令序列的 Cycle-by-Cycle 執行日誌，展示 Scoreboard 如何動態處理 RAW 資料相依與管線停頓。重點在於說明記分板利用位元位移追蹤 Data Avail.，並精確控制 Bypassing 觸發時機。此追蹤過程驗證了 Scoreboard 的動態排程能力，同時揭示了順序發射（In-Order Issue）面對長延遲運算時的瓶頸。

## slide：44
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0044.jpg" width="50%">
</div>

這張投影片主題為 「I2O2: In-order Frontend/Issue, Out-of-order Writeback/Commit」，展現了結合順序發射與亂序寫回（Commit）特性的微架構。
- 本教學重點內容：
  - 混合式管線架構模式（I2O2）：
    - In-order Frontend / Issue ($I_2$)：指令從 Fetch (F)、Decode (D) 到 Issue (I) 階段皆嚴格按照程式碼原始順序進行處理。
    - Out-of-order Writeback / Commit ($O_2$)：由於不同執行單元長度不一（例如 2 階段算術單元 $X_0 \to X_1$ vs. 4 階段乘法單元 $Y_0 \to \dots \to Y_3$），執行速度較快的短指令會超越先發射但執行慢的長指令，先一步算完並亂序寫回（Out-of-Order Writeback）暫存器。
  - 硬體狀態控制（Scoreboard + ARF）：
    - I 階段：讀取 ARF（架構暫存器檔案），同時對 Scoreboard (SB) 進行讀寫以實施相依性檢查。
    - W 階段：結果完成時，動態更新 ARF 並釋放 SB 狀態。
- 個人看法：
  <br>I2O2 展現了處理器從純順序（In-Order）邁向完全亂序（Out-of-Order）的過渡設計。
  - 優點：前端設計簡單，且允許短指令不必死等前方慢速指令完成即可先寫回，提高了 execution pipeline 的運算效能。
  - 致命缺陷（精確中斷喪失）：由於寫回與提交是亂序的（Out-of-Order Commit），若後發射的短指令已經寫回更新了 ARF，而先發射的長指令此時突然觸發硬體異常（Exception），CPU 將無法還原至發生異常當下的精確狀態。這也是為什麼現代高效能處理器必須導入 ROB（Reorder Buffer） 來達成「亂序執行、順序提交（In-Order Commit）」。
- 總結：
  <br>本投影片介紹 I2O2 架構，重點在於前端順序發射（In-Order Issue），但因多路執行管道長短不一，導致指令亂序寫回與提交（Out-of-Order Writeback/Commit）。此設計雖能提升多功能單元的吞吐量，但亂序更新 ARF 會破壞系統的「精確中斷（Precise Interrupt）」機制，凸顯了後續微架構需要 Reorder Buffer 來強制順序提交的必要性。

## slide：45
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0045.jpg" width="50%">
</div>

這張投影片說明 I2O2 架構下 Scoreboard（記分板）運作機制與控制限制。
- 本教學重點內容：
  - 功能與結構承襲：
    - 基本運作與 I4 架構類似，但可用於追蹤寫回埠（Writeback Port）上的結構衝突（Structural Hazards）。
    - 根據各功能單元管線的長度（Length of Pipeline），動態設定 Data Avail. 欄位中的位元。
  - WAW Hazards（寫後寫衝突）的處理機制：
    - 保守停頓策略：此架構透過在 Issue（發射）階段保守地暫停（Stall）指令來避免 WAW 衝突，因此當前的 Basic Scoreboard 結構已足夠使用。
    - 複雜度開銷：若要在允許發射後再動態處理解決 WAW 衝突，則需要更複雜的 Scoreboard 設計。
- 個人看法：
  <br>這反映了微架構設計在「硬體複雜度」與「執行效能」之間的權衡（Trade-off）。
  - 優點：藉由在 Issue 階段直接 Blocking 掉可能產生 WAW 的指令，硬體可以用非常輕量、精簡的 Scoreboard 控制邏輯（Basic Scoreboard）維護寫回正確性，省去複雜的重命名或佇列機制。
  - 瓶頸：保守的 Stall 會產生不必要的流水線停頓，降低指令平行度（ILP）；這說明了為什麼更進階的 CPU 會採用暫存器重命名（Register Renaming）技術（如 Tomasulo 演算法）來徹底消除 WAW/WAR 假性相依，進而解放性能上限。
- 總結：
  <br>本投影片說明 I2O2 架構下的 Scoreboard 機制，其透過設定 Data Avail. 位元追蹤 Writeback 埠的結構衝突。為確保正確性，系統選擇在 Issue 階段保守停頓指令以防範 WAW 衝突，使 Basic Scoreboard 足以應付需求。此折衷設計降低了硬體複雜度，但也暴露了順序發射限制 ILP 的效能瓶頸。

## slide：46
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0046.jpg" width="50%">
</div>

這張投影片展現了與上一頁相同結構的 I2O2（順序發射 / 亂序寫回） 架構，並著重於範例指令序列的執行追蹤。
- 本教學重點內容：
  - I2O2 範例追蹤架構模型：
    - 前端保持順序（In-Order Fetch/Decode/Issue），並由 Scoreboard (SB) 進行動態檢查。
    - 多路平行執行路徑包含 2 階段 ALU ($X_0 \to X_1$)、4 階段 Memory ($M_0 \to \dots \to M_3$) 與 4 階段 Multiplier ($Y_0 \to \dots \to Y_3$)。
    - 各單元算完後可亂序寫回（Out-of-Order Writeback）至 ARF。
  - 追蹤目標（Cycle-by-Cycle Trace）：
    - 提供相同的 7 條指令序列（包含 mul 與 addi），供學生比對在 I2O2 亂序寫回 模式下，指令於時脈週期 $0 \sim 18$ 的推移情況與 I4 順序寫回架構有何差異。
- 個人看法：
  <br>對比上一節課的 I4（順序寫回），I2O2 讓短指令（如 addi）能提早於慢速指令（如 mul）前完成寫回（Out-of-Order Commit）。
  - 效能提升：減少了短指令在寫回階段被慢速指令卡住的 stall 時間，提高 pipe 吞吐量。
  - 設計隱憂：亂序寫回破壞了「精確中斷（Precise Interrupt）」。當較晚發射的短指令已寫回暫存器，而較早發射的慢指令突然發生硬體 Exception 時，CPU 狀態將無法完美復原，這促成了後續 Reorder Buffer (ROB) 架構的誕生。
- 總結：
  <br>本投影片提供 I2O2（順序發射、亂序寫回）管線的指令追蹤範例。重點在於展示多路執行單元如何讓短指令超越長延遲指令先一步完成寫回，以提升運算效率。然而此設計破壞了精確中斷機制，亦引出了現代 CPU 導入 ROB 實現順序提交的必要性。

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






















