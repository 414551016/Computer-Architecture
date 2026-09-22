Prompt：請說明本教學重點內容及你的看法，最後以250字內總結
### Week 3 課堂逐字稿

## slide：1 -2
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0001.jpg" width="49%">
  <img src="./Lecture/SD3/SD3_page-0002.jpg" width="49%">
</div>

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

## slide：38
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0038.jpg" width="50%">
</div>

## slide：39
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0039.jpg" width="50%">
</div>

## slide：40
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0040.jpg" width="50%">
</div>

## slide：41
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0041.jpg" width="50%">
</div>

## slide：42
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0042.jpg" width="50%">
</div>

## slide：43
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0043.jpg" width="50%">
</div>

## slide：44
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0044.jpg" width="50%">
</div>

## slide：45
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0045.jpg" width="50%">
</div>

## slide：46
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0046.jpg" width="50%">
</div>

## slide：47
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0047.jpg" width="50%">
</div>

## slide：48
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0048.jpg" width="50%">
</div>

## slide：49
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0049.jpg" width="50%">
</div>

## slide：50
<div align="left" >
  <img src="./Lecture/SD3/SD3_page-0050.jpg" width="50%">
</div>






















