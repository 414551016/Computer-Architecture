## 何謂 RISC-V？
RISC-V（讀作 "Risk Five"） 是一種開放式的指令集架構（Instruction Set Architecture, ISA），定義了 CPU 可以執行哪些指令以及軟體如何與硬體溝通。它由 University of California, Berkeley 於 2010 年左右提出，最大特色是開源、免費授權、可自由擴充。
<br>簡單來說：RISC-V 對 CPU 的地位，**就像文法規則對語言一樣**。只要依照 RISC-V 規範設計，就能製造出相容的處理器。
- 為什麼叫 RISC-V？
  - RISC = Reduced Instruction Set Computer（精簡指令集電腦）
  - V = 羅馬數字 5，代表伯克萊大學第五代 RISC 架構
- RISC-V 與 x86、ARM 的差異
  >RISC-V 最大優勢在於任何人都能免費使用與修改，不需要支付 ARM 授權費或取得 x86 授權。
  
  |架構|代表廠商|特性|
  |--|--|--|
  |x86|Intel、AMD|效能強、生態成熟|
  |ARM|Apple、高通、聯發科|低功耗|
  |RISC-V|開源社群|開源、可客製化|
- RISC-V 的特色
  - 開源：<br>企業、學校、研究機構都能自由設計自己的 CPU：不需授權費、不需專利限制。
  - 模組化設計：
    - 基本指令集很小：RV32I、RV64I。
    - 需要功能再加入：
      - M：乘除法
      - F：單精度浮點
      - D：雙精度浮點
      - A：原子操作
  - 容易教學與研究：<br>由於架構簡潔，許多計算機結構課程使用 RISC-V 作為教學架構。
  - 與您課程的關係：<br>在「計算機結構（Computer Architecture）」課程中，學生常需要設計。而實作平台通常就是 RISC-V。因為它的指令格式簡單，非常適合學習 CPU 設計原理。
    <br>Single-Cycle Processor → Pipelined Processor → Cache → Branch Prediction
    - 例如：add x3, x1, x2
      >表示：x3 = x1 + x2
      ><br>CPU 只需完成：讀取 x1, 讀取 x2, 相加, 寫回 x3,即可執行。
- 總結：<br>RISC-V 是一種開源的精簡指令集架構（ISA），由加州大學柏克萊分校提出，強調簡潔、模組化與可擴充性。與 x86 與 ARM 不同，RISC-V 不需支付授權費，任何人皆可自由設計相容處理器，因此近年廣泛應用於嵌入式系統、物聯網、AI晶片及學術研究。由於其指令格式規則且易於實作，許多計算機結構課程皆以 RISC-V 作為 CPU 設計與管線化處理器實驗平台。未來隨著開源硬體發展，RISC-V 被視為最具潛力的新世代處理器架構之一。
