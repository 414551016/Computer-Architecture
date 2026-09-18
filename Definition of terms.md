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


## 何謂 Pipelined（管線化）？
Pipelined（管線化） 是一種 CPU 設計技術，將執行一條指令的過程切成多個階段，讓多條指令能同時在不同階段執行，以提升處理器效能。這個概念類似工廠的生產線（Pipeline）。
- 生產線比喻：
  <br>假設生產一輛車要經過：車身組裝 → 噴漆 → 檢驗 → 出貨。若一次只做一台車：車1完成後 → 車2才能開始。
  <br>但若採用生產線：車1 → 噴漆。車2 → 組裝。多台車可以同時進行不同工作。這就是 CPU 管線化也是相同概念。
- 非管線化（Non-Pipelined）：
  <br>一條指令完成後才執行下一條：
  - 指令1：取指 → 解碼 → 執行 → 完成
  - 指令2：取指 → 解碼 → 執行 → 完成
  - 指令3：取指 → 解碼 → 執行 → 完成
  <br>**CPU 常有部分硬體閒置。**
- **管線化（Pipelined）**
  <br>以經典 RISC-V 五級管線為例：
  - IF 取指令 (Instruction Fetch)。
  - ID 指令解碼 (Instruction Decode)。
  - EX 執行 (Execute)。
  - MEM 存取記憶體 (Memory Access)。
  - WB 寫回 (Write Back)。
  <br>**此時多條指令同時運作：**
  - Cycle 1: 指令1 IF
  - Cycle 2: 指令1 ID 指令2 IF
  - Cycle 3: 指令1 EX 指令2 ID 指令3 IF
  - Cycle 4: 指令1 MEM 指令2 EX 指令3 ID
- 管線化的優點：
  - 提高吞吐量（Throughput），
    <br>例如：
    - 單週期 CPU：100 條指令可能需要 500 個週期
    - 管線化 CPU：100 條指令可能只需約 104 個週期
    <br>因此：
    - 效能提高
    - CPU利用率提高
    - 硬體閒置減少
  - 管線化的問題：
    - Data Hazard（資料冒險）
      - 第1條指令執行：add x1,x2,x3。
      - 第2條指令執行：sub x4,x1,x5。
      <br>第二條指令需要等待第一條 x1 結果。
    - Control Hazard（控制冒險）
      <br>例：beq x1,x2,label，CPU 不知道是否跳轉。
    - Structural Hazard（結構冒險）
      <br>兩個階段同時搶同一個硬體資源。
  - **總結：**
    <br>Pipelined（管線化）是一種將 CPU 指令執行流程**分割為多個階段**，並讓多條指令同時在不同階段運作的處理器設計技術。其概念類似工廠生產線，可提高硬體利用率與整體吞吐量。以 RISC-V 為例，通常包含 IF、ID、EX、MEM、WB 五個階段。然而，管線化可能產生資料冒險、控制冒險及結構冒險等問題，因此需搭配 Forwarding、Stall 與 Branch Prediction 等機制解決。現代 CPU 幾乎都採用管線化架構作為提升效能的重要方法。

## Pipelined RISC-V Processor
如果您正在修 Computer Architecture（計算機結構） 或 RISC-V 相關課程，那麼 Pipelined RISC-V Processor（管線化 RISC-V 處理器） 是非常重要的核心概念。
<br>Pipelined RISC-V Processor 是將 CPU 執行指令的流程切分成多個階段，讓多條指令能夠同時進行不同工作，以提高處理器效能的 RISC-V 處理器。
- 為什麼需要 Pipeline？
  <br>假設執行一條指令需要：取指令（Fetch） → 解碼（Decode） → 執行（Execute） → 存取記憶體（Memory） → 寫回結果（Write Back）。
  <br>若不使用 Pipeline：指令1 完成後 → 指令2 才開始 → 指令3 才開始...
  <br>Pipeline 的想法：如同工廠生產線：工人1：切菜 → 工人2：炒菜 → 工人3：擺盤。
  <br>此時：指令1在執行 → 指令2在解碼 → 指令3在取指令，同時進行。
  
- 
























