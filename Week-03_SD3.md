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

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：39
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0039.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：40
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0040.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

## slide：41
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0041.jpg" width="50%">
</div>

- 本教學重點內容：
- 個人看法：
- 總結：

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






















