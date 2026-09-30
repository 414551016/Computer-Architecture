# Computer Architecture
## Computer Architecture Lab 2: Out-of-Order RISC-V Processor - Reorder Buffer 實驗說明書。
> 電腦架構 — 實驗二：亂序執行 RISC-V 處理器 - 重排序緩衝區 (Reorder Buffer)

## 簡介 (Introduction)
In this lab, you will complete the scoreboard and implement a reorder buffer (ROB) for an out-of-order, single-issue RISC-V processor. The provided processor framework includes an incomplete scoreboard and a dummy ROB implementation. Your objectives are to complete these components and create appropriate test cases.
> 在本次實驗中，您將為一個亂序（Out-of-Order）、單發射（Single-Issue）的 RISC-V 處理器完成記分板（Scoreboard）並實作重排序緩衝區（reorder buffer，ROB）。所提供的處理器框架包含一個未完成的記分板和一個虛設的（Dummy）ROB 實作。您的目標是完成這些組件並建立適當的測試用例。

This lab will provide you with experience in:
> 本實驗將為您提供以下經驗：
- The fundamentals of reorder buffers and their role in out-of-order execution.
  > 理解重排序緩衝區的基本原理，以及它在亂序執行重排序緩衝區的基本原理及其在亂序執行中的角色。
- How to design and implement a scoreboard for dependency tracking, hazard detection, and operand bypassing.
  > 如何設計與實作記分板，以進行相依性追蹤（Dependency Tracking）、冒險偵測（Hazard Detection）與運算元旁路（Operand Bypassing）。
  > <br>學習如何設計及實作記分板，用於相依性追蹤、冒險偵測與運算元旁路傳遞。  
- How to design and implement in-order commitment logic within an out-of-order processor.
  > 如何在亂序處理器中設計與實作順序提交（In-Order Commitment）邏輯。<br>學習如何在亂序處理器中，設計及實作依序提交的邏輯。

### 1. Reminder／提醒事項
- Submission Deadline: 10/12 (Mon) 11:59 p.m.
  > 繳交期限：10 月 12 日（星期一）晚上 11:59。
- Please refer to Lab 0 for the academic integrity requirements.
  > 學術誠信要求請參閱 Lab 0。
- No sharing or distribution of lab materials is allowed.
  > 禁止分享或散布實驗材料。

### 2. Setup／環境設定
#### 2.1 Getting Started／開始使用
After obtaining the Lab 2 materials, extract them using the following commands:
> 取得 Lab 2 材料後，使用以下指令進行解壓縮：
```
% tar -xf lab2.tar
% cd lab2
% export LAB2_ROOT=$PWD
```
Inside the lab root directory, you'll find these subdirectories, each serving a specific purpose:
> 在實驗根目錄下，您會找到以下子目錄，各自有其特定用途：

|目錄 | English | 中文 |
| --- | --- | --- |
| `build` | Makefile and compiled code. | Makefile 與編譯後的程式碼。 |
| `riscvooo` | Out-of-Order RISC-V processor source code (includes a placeholder reorder buffer). | 亂序 RISC-V 處理器原始碼（包含暫代用的重排序緩衝區）。 |
| `tests` | Assembly test build system. | 組合語言測試的建置系統。 |
| `tests/riscv` | RISC-V assembly tests. | RISC-V 組合語言測試。 |
| `tests/scripts` | Utility scripts for the build system. | 建置系統所用的輔助腳本。 |
| `ubmark` | Benchmarks for evaluation. | 用於評估的基準測試程式。|
| `vc`|Additional Verilog components.|額外的 Verilog 組件。|

Most directories remain unchanged from the previous lab. The new directory, riscvooo, contains the OoO processor framework, including an incomplete scoreboard and a dummy ROB implementation.
> 大多數目錄與上次實驗相同。新增的目錄 riscvooo 包含亂序處理器框架，其中包括未完成的記分板與虛設的 ROB 實作。

### 2.2 Building the Project／建置專案
The commands below describe the build and test procedure. As usual, we'll start by compiling the reference processors and running the RISC-V assembly tests:
> 以下指令說明建置與測試流程。照常，我們先編譯參考處理器並執行 RISC-V 組合語言測試：
```
% cd $LAB2_ROOT/tests
% mkdir build && cd build
% ../configure --host riscv32-unknown-elf
% make && ../convert

% cd $LAB2_ROOT/build
% make
% make check
% make check-asm-riscvooo
% make check-asm-rand-riscvooo
```
Then run the benchmark:
> 接著執行基準測試：
```
% cd $LAB2_ROOT/ubmark
% mkdir build && cd build
% ../configure --host riscv32-unknown-elf
% make && ../convert

% cd $LAB2_ROOT/build
% make
% make check
% make run-bmark-riscvooo
% make run-bmark-rand-riscvooo
```

### 3. Out-of-Order Processor Description／亂序處理器說明
The out-of-order (OoO) processor in Lab 2 is derived from the riscvlong microarchitecture from Lab 1, so most of the design should feel familiar. After you complete the scoreboard, the processor with the dummy ROB operates as a simplified I2O2 processor: fetch, decode, and issue occur in order, while execution, writeback, and commit are out of order. You will then implement and integrate the ROB to convert it into an I2OI processor. Key differences from the lecture model include:
> Lab 2 中的亂序（OoO）處理器衍生自 Lab 1 的 riscvlong 微架構，因此大部分設計應該很熟悉。完成記分板後，帶有虛設 ROB 的處理器運作方式就像簡化的 I2O2 處理器：擷取（Fetch）、解碼（Decode）、發射（Issue）順序進行，而執行（Execution）、寫回（Writeback）、提交（Commit）則是亂序的。接著您將實作並整合 ROB，將其轉換為 I2OI 處理器。與課堂模型的關鍵差異包括：
- The pipeline includes three pipes: The MUL pipe handles muldiv operations and takes four cycles to execute. The MEM pipe handles memory accesses and takes two cycles to execute. The ALU pipe handles all other operations and takes one cycle to execute.
  > 管線包含三個管道：MUL 管道處理乘除法操作，需要 4 個週期執行；MEM 管道處理記憶體存取，需要 2 個週期執行；ALU 管道處理所有其他操作，需要 1 個週期執行。
- Memory writes occur directly in the M stage without the need for a store buffer. This simplifies the design in this lab by ensuring that memory operations execute sequentially and without exception handling.
  > 記憶體寫入直接在 M 階段發生，不需要 Store Buffer。這確保了記憶體操作按順序執行且無例外處理，簡化了本實驗設計。
- Unlike some configurations discussed in lecture, this processor includes a single (architectural) register file. Instead of using a physical register file or storing uncommitted data directly in the ROB, we have a dedicated buffer within the datapath to hold data that has been written back but not yet committed.
  > 與課堂討論的部分配置不同，此處理器僅包含單一（架構）暫存器檔案（ARF）。我們在資料通道內有一個專用緩衝區，用於存放已寫回但尚未提交的資料，而不是使用實體暫存器檔案（PRF）或直接將未提交資料存放在 ROB 中。
- The reorder buffer in this lab does not include speculative bits, as speculative execution is not needed.
  > 本實驗中的重排序緩衝區不包含推測位元（Speculative Bits），因為不需要推測執行。

In this lab, you will work with a reorder buffer containing 16 entries, sufficient for the maximum expected in-flight instructions. The structure of the ROB is illustrated in Table 1.
> 在本實驗中，您將使用包含 16 個表項（Entries）的重排序緩衝區，這足以容納預期的最大在途（In-Flight）指令數。ROB 的結構如表 1 所示：

**Table 1: Reorder Buffer Contents／表 1：重排序緩衝區內容**
Entry／項目 | Valid／有效 | Pending／等待結果 | Physical Register／實體暫存器 | Data／資料 |
| --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 0 | 0x00000000 |
| 1 | 1 | 0 | 3 | 0xDEADBEEF |
| ... | ... | ... | ... | ... |
| 15 | 1 | 1 | 0 | 0x00000000






















