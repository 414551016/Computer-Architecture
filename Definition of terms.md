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


## 何謂 rv32i？
RV32I（RISC-V 32-bit Integer Base Instruction Set） 是 RISC-V 最基本的 32 位元整數指令集架構（ISA）。其中：<br>RV = RISC-V。<br>32 = 32 位元處理器。<br>I = Integer（基本整數指令集）。<br>RV32I 提供 CPU 最基本的功能，包括：整數加減運算、邏輯運算（AND、OR、XOR）、載入與儲存資料（Load/Store）、分支與跳躍控制（Branch/Jump）。<br>RV32I 具有 32 個通用暫存器（x0~x31），每個暫存器寬度為 32 位元。<br>例：add x3, x1, x2
**計算機結構課程最常見的 RV32I 整數運算指令**
```
add
addi
sub
and
andi
or
ori
xor
xori
sll
srl
sra
slt
slti
lw
sw
beq
bne
jal
jalr
若加上 M Extension：
mul
mulh
div
rem
```


## 何謂 rv64i？
RV64I（RISC-V 64-bit Integer Base Instruction Set） 是 RISC-V 的 64 位元基礎整數指令集架構。其中：<br>RV = RISC-V<br>64 = 64 位元處理器<br>I = Integer（基本整數指令集）。<br>RV64I 保留 RV32I 的所有基本功能，但：<br>暫存器擴充為 64 位元。<br>可直接處理 64 位元整數。<br>支援更大的記憶體位址空間。<br>適合 Linux、伺服器與高效能運算系統。<br>例：ld x5, 0(x10)表示從記憶體載入 64 位元資料到暫存器 x5。


## 何謂 ALU
ALU（Arithmetic Logic Unit，算術邏輯單元） 是 CPU 內部負責執行數學運算與邏輯運算的核心元件，可以視為 CPU 的「計算器」。<br>簡單來說：ALU 負責計算，控制單元（Control Unit）負責指揮。
- ALU 的功能：
  - 算術運算（Arithmetic）：加法 (+)、減法 (-)、乘法 (*)、除法 (/)
    <br>範例：5 + 3 = 8
    <br>CPU 會將數值送入 ALU 計算後得到結果。
  - 邏輯運算（Logic）：AND、OR、XOR、NOT
    <br>範例：1010 AND 1100 = 1000
  - 比較運算：==、!=、<、>、<=、>=、`
    <br>RISC-V 常見指令：slt x1, x2, x3
    <br>表示：若 x2 < x3，則 x1 = 1，否則 x1 = 0
  - 位元移動（Shift）：sll、srl、sra
    <br>範例：0101 << 1 結果：1010
- 在 CPU 中的位置：
```
       CPU
 ┌─────────────────┐
 │ Control Unit    │
 │       ↓         │
 │ Register File   │
 │       ↓         │
 │      ALU        │
 │       ↓         │
 │     Memory      │
 └─────────────────┘
```
  工作流程：**暫存器讀取資料** → **ALU** → **產生結果** → **寫回暫存器**
- 在 RISC-V 中的例子：
  - add x5, x1, x2 含意：x5 = x1 + x2
    <br>執行流程：x1 讀出，x2 讀出，↓ ALU 做加法 ↓ 結果寫入 x5

**總結**<br>ALU（Arithmetic Logic Unit，算術邏輯單元）是 CPU 中負責執行算術與邏輯運算的核心組件。其主要功能包括加減乘除、位元運算（AND、OR、XOR）、資料比較及位移運算等。當程式執行時，CPU 會先從暫存器取得資料，再交由 ALU 完成計算，最後將結果寫回暫存器或記憶體。在 RISC-V 等處理器中，ALU 通常位於 Pipeline 的 Execute（EX）階段，是指令執行的關鍵單元。ALU 的設計效率直接影響處理器的效能、功耗與硬體複雜度，因此是計算機結構與處理器設計中的重要核心元件。


## 何謂 RAW、WAW 與 WAR Hazard？
在 Pipeline（管線化處理器） 中，多條指令會同時執行，因此可能發生資料相依（Data Dependency）問題，稱為 Data Hazard（資料冒險）。
- 三種常見的資料冒險為：
  - RAW（Read After Write）為先寫後讀相依，後續指令需使用前一指令尚未寫回的結果，是最常見且必須處理的冒險。
  - WAR（Write After Read）為先讀後寫相依，可能因執行順序改變而使讀取到錯誤資料。
  - WAW（Write After Write）為寫後寫相依，兩條指令寫入相同目的暫存器時可能造成結果覆蓋。

### RAW（Read After Write）寫後讀相依（真實相依）
後面的指令要讀取資料，但前面的指令尚未完成寫入。例如：
```
add x1, x2, x3 # x1 = x2 + x3
sub x4, x1, x5 # 需要讀取 x1
問題：
add 尚未把結果寫入 x1
sub 就要讀取 x1
因此產生 RAW Hazard。
```
**解決方式**
- Forwarding（旁路/前推）
- Stall（停滯等待）
<br>RAW 是管線處理器中最常見的 Hazard。

### WAR（Write After Read）讀後寫相依（反相依）
前面的指令還沒完成讀取資料，後面的指令卻先把資料改掉。例如：
```
I1: sub x5, x1, x2
I2: add x1, x3, x4
若執行順序錯誤：
I2 先改寫 x1
I1 才去讀 x1
則 I1 讀到錯誤資料。
```

### WAW（Write After Write）寫後寫相依（輸出相依）
意思是：兩個指令都要寫同一個目的暫存器，但順序錯亂。例如：
```
I1: add x1, x2, x3
I2: sub x1, x4, x5
正確結果應是：最後 x1 為 I2 的結果
但若：I2 先寫入而I1 後寫入，則最終 x1 變成 I1 的值。產生 WAW Hazard。
```
**解決方式**
- Register Renaming（暫存器重新命名）
- Scoreboarding
- Tomasulo Algorithm
<br><br>
## RISC-V 常用的整數運算指令（Arithmetic Instructions）
add、sub、mul 與 addi 是 RISC-V 常用的整數運算指令，用來進行整數計算。add 用於兩個暫存器相加，sub 用於相減，mul 用於相乘，而 addi 則是將暫存器內容與立即數（常數）相加。前三者屬於暫存器對暫存器（Register-to-Register）運算，addi 則屬於暫存器對立即數（Register-to-Immediate）運算。例如 add x5,x1,x2 表示 x5=x1+x2，而 addi x5,x1,10 表示 x5=x1+10。這些指令由 CPU 的 ALU 在 Execute（EX）階段完成運算，是 RISC-V 程式執行的基本組成單元。
**總結**
RISC-V 常用的整數運算指令主要包括算術運算（add、addi、sub）、邏輯運算（and、or、xor）、位移運算（sll、srl、sra）、比較運算（slt、slti）、資料存取（lw、sw）以及流程控制（beq、bne、jal、jalr）等。其中 add 與 addi 為最基本的加法指令，sub 為減法，slt 用於比較大小，lw 與 sw 負責記憶體存取，而分支與跳躍指令則負責程式流程控制。若處理器支援 M Extension，還可使用 mul、div、rem 等乘除法指令。這些指令構成 RISC-V 處理器執行程式的核心基礎。
### add（Addition）：將兩個暫存器的值相加。
```
語法：add rd, rs1, rs2
rd：目的暫存器
rs1：來源暫存器1
rs2：來源暫存器2
範例：
add x5, x1, x2 代表：x5 = x1 + x2
```

### sub（Subtraction）將兩個暫存器相減。
```
語法：sub rd, rs1, rs2
範例：sub x5, x1, x2 代表：x5 = x1 - x2
```

### mul（Multiply）兩個暫存器相乘。
```
語法：mul rd, rs1, rs2
範例：mul x5, x1, x2 代表：x5 = x1 × x2
```
**注意**：mul 屬於 M Extension（RV32M/RV64M），並不包含在最基本的 RV32I 中。

### addi（Add Immediate）將暫存器與一個立即數（Immediate）相加。
```
語法：addi rd, rs1, imm
其中：imm = 常數
範例：addi x5, x1, 10 代表：x5 = x1 + 10
```
**add 與 addi 的差別**：add為兩個暫存器。addi為一個暫存器 + 一個常數

### div 除法
```
div rd, rs1, rs2
範例：div x5, x1, x2 代表：x5 = x1 ÷ x2
```

## RISC-V 常用的邏輯運算指令（Logic Instructions）
### AND 位元與
```
and rd, rs1, rs2
```

### OR 位元或
```
or rd, rs1, rs2
```

### XOR 位元互斥或
```
xor rd, rs1, rs2
```

## RISC-V 常用位移運算指令（Shift Instructions）
### sll(SHIFT LEFT LOGICAL) 左移
```
sll rd, rs1, rs2
```

### srl(SHIFT RIGHT LOGICAL) 右移
```
srl rd, rs1, rs2
```

### sra(SHIFT RIGHT ARITHMETIC) 算術右移
```
sra rd, rs1, rs2
```

## RISC-V 常用比較指令（Compare Instructions）
- slt(Set Less Than) 小於則設為1
```
slt rd, rs1, rs2
若 rs1 < rs2，rd = 1，否則 rd = 0
```


















