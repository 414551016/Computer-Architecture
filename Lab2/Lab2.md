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

Each entry in the ROB uses a valid bit to indicate if it is active; this bit is set when the entry is allocated and cleared when the entry is committed. The pending bit is set at allocation and cleared when the result is written back to the ROB. The physical register bits store the destination register for the entry in the architectural register file.
> ROB 中的每個表項都使用 Valid 位元來表示是否活躍；該位元在分配表項時設為 1，在提交時清零。Pending 位元在分配時設為 1，在結果寫回 ROB 時清零。Physical Register 位元儲存該表項在架構暫存器檔案中的目標暫存器地址。

Two 4-bit pointers manage the ROB: the head pointer, which indicates the next entry to be committed, and the tail pointer, which indicates the next available entry for allocation. The tail pointer increments with each new allocation, and the head pointer increments upon commitment. Although capacity issues are unlikely in this lab, ensure boundary checks are in place to stall the processor if the ROB becomes full.
> 由兩個 4-bit 指標管理 ROB：Head 指標指出下一個要提交的表項，Tail 指標指出下一個可用於分配的表項。每次新分配時 Tail 指標加 1，提交時 Head 指標加 1。雖然本實驗不太可能出現容量不足的問題，但請確保設有邊界檢查，以便在 ROB 滿載時讓處理器暫停（Stall）。

Instruction data is stored in the provided array, rob_data, located in the datapath. The ROB generates the control signals for this array.
> 指令資料儲存在資料通道中的 rob_data 陣列中，ROB 負責產生該陣列的控制訊號。

Finally, speculative bits are not needed in this lab's simplified design. In cases where a conditional branch in the execute stage (X) could impact an instruction in decode (D), the ROB simply skips allocation if the instruction in D is squashed. While this would increase cycle time in a real processor, it is acceptable for this lab's simulation.
> 最後，在本實驗簡化的設計中不需要推測位元。當執行階段（X）條件分支可能影響解碼階段（D）的指令時，如果 D 階段的指令被沖刷（Squashed），ROB 只需要跳過分配即可。這在真實處理器中會增加 Cycle 時間，但對於本實驗的模擬是可以接受的。

### 4. Building the Scoreboard／建立記分板
Before building the reorder buffer, you will first complete the scoreboard implementation in riscvooo-CoreScoreboard.v. The scoreboard is responsible for tracking register dependencies and determining whether an instruction can safely proceed through the pipeline.
> 在建立重排序緩衝區之前，您將首先在 riscvooo-CoreScoreboard.v 中完成記分板的實作。記分板負責追蹤暫存器相依性，並判斷指令是否可以安全地在管線中推進。

Since instructions may have different execution latencies depending on the functional unit they use, the scoreboard must keep track of the status of each architectural register and determine when a source operand becomes available.
> 由於指令根據所使用的功能單元（Functional Unit）可能有不同的執行延遲，記分板必須追蹤每個架構暫存器的狀態，並確定來源運算元何時可用。

The scoreboard maintains the following information for each register:
> 記分板為每個暫存器維護以下資訊：
- pending: Indicates whether the register is waiting for a value produced by an in-flight instruction.
  > pending: 表示該暫存器是否正在等待由在途指令產生的數值。
- functional_unit: Records which functional unit is producing the register value.
  > functional_unit: 記錄是哪一個功能單元正在產生該暫存器的值。
- reg_latency: Tracks the progress of the instruction producing the register value.
  > reg_latency: 追蹤產生該暫存器值的指令的進度。
- reg_rob_slot: Records the ROB slot associated with the instruction that writes to the register.
  > reg_rob_slot: 記錄與寫入該暫存器的指令相關聯的 ROB 槽位（Slot）。

The processor contains three functional units: ALU, MEM, MUL.
> 處理器包含三個功能單元：ALU（算術與邏輯操作）、MEM（記憶體操作）、MUL（乘法與除法操作）。
- ALU:Handles arithmetic and logical instructions.
  > ALU（算術與邏輯操作）：處理算術與邏輯指令。
- MEM:Handlesmemoryoperations.
  > MEM（記憶體操作）：處理記憶體操作。
- MUL:Handlesmultiply and divide operations.
  > MUL（乘法與除法操作）：處理乘法與除法運算。

Because these functional units have different execution latencies, the scoreboard must correctly track when their results become available and whether an instruction can obtain its operands through bypassing.
> 由於這些功能單元的執行延遲不同，記分板必須正確追蹤其結果何時可用，以及指令是否可以透過旁路（Bypassing）取得運算元。


The scoreboard provides the following main functions:
> 記分板提供以下主要功能：
- DependencyTracking: Determine whether the source registers of an instruction are available.
  > 相依性追蹤 (Dependency Tracking): 判斷指令的來源暫存器是否可用。
- Hazard Detection: Stall an instruction when a required operand is not ready or when a writeback conflict occurs.
  > 冒險偵測 (Hazard Detection): 當所需的運算元未準備好或發生寫回衝突時，使指令暫停（Stall）。
- Latency Tracking: Track the progress of instructions through different functional units while consid ering pipeline stalls.
  > 延遲追蹤 (Latency Tracking): 在考慮管線暫停的情況下，追蹤指令在不同功能單元中的進度。
- Operand Bypassing: Select the appropriate bypass source when an operand is available from a later pipeline stage.
  > 運算元旁路 (Operand Bypassing): 當運算元可從較後面的管線階段取得時，選擇適當的旁路來源。
- ROBTracking: Associate each destination register with its allocated ROB slot for ROB bypassing and commit handling.
  > ROB 追蹤 (ROB Tracking): 將每個目標暫存器與其分配的 ROB 槽位關聯起來，以用於 ROB 旁路與提交處理。

The input signals used for dependency and hazard detection include:
> 用於相依性與冒險偵測的輸入訊號包括：<br>Input signals (輸入訊號): src0, src1, src0_en, src1_en, dst, dst_en, func_unit, latency, stalls.
- src0andsrc1: Specify the source registers of the current instruction.
  > `src0` and `src1`：指定目前指令的來源暫存器。
- src0_en and src1_en: Indicate whether each source register is used.
  > `src0_en` and `src1_en`：表示是否使用各個來源暫存器。
- dst: Specifies the destination register.
  > `dst`：指定目的暫存器。
- dst_en: Indicates whether the instruction writes to a destination register.
  > `dst_en`：表示該指令是否會寫入目的暫存器。
- func_unit: Specifies which functional unit executes the instruction.
  > `func_unit`：指定由哪個功能單元執行該指令。
- latency: Specifies the expected execution latency of the instruction.
  > `latency`：指定該指令預期的執行延遲。
- stalls: Indicates the current pipeline stall conditions.
  > `stalls`：表示目前管線的停等情況。

The scoreboard generates the following control signals: 
> 記分板產生以下控制訊號：<br>Output signals (控制訊號): stall_hazard, src0_byp_mux_sel, src1_byp_mux_sel, src0_byp_rob_slot, src1_byp_rob_slot, wb_mux_sel, stall_wb_hazard_X, stall_wb_hazard_M.
- stall_hazard: Indicates whether the instruction must stall due to a dependency or resource conflict.
  > `stall_hazard`：表示該指令是否必須因相依性或資源衝突而停等。
- src0_byp_mux_sel and src1_byp_mux_sel: Select the bypass source for each source operand.
  > `src0_byp_mux_sel` and `src1_byp_mux_sel`：選擇各個來源運算元的旁路來源。
- src0_byp_rob_slot and src1_byp_rob_slot: Specify the ROB slot associated with each source register.
  > `src0_byp_rob_slot` and `src1_byp_rob_slot`：指定各個來源暫存器所對應的 ROB 槽位。
- wb_mux_sel: Selects which functional unit uses the writeback path.
  > `wb_mux_sel`：選擇由哪個功能單元使用寫回路徑。
- stall_wb_hazard_X and stall_wb_hazard_M: Indicate writeback conflicts between functional units.
  > `stall_wb_hazard_X` and `stall_wb_hazard_M`：表示功能單元之間的寫回衝突。

Complete the scoreboard logic in riscvooo-CoreScoreboard.v without changing the provided module interface. Your implementation should correctly track register dependencies, update instruction latency according to pipeline stalls, detect hazards, and generate the required bypass and writeback control signals.
> 在不修改提供的模組介面的前提下，完成 riscvooo-CoreScoreboard.v 中的記分板邏輯。您的實作應正確追蹤暫存器相依性、根據管線暫停更新指令延遲、偵測冒險，並產生所需的旁路與寫回控制訊號。

After completing the scoreboard, run the provided test suites and verify that the processor correctly handles register dependencies and operand bypassing. Some cases related to out-of-order commit may still fail at this stage. These cases will be addressed after implementing the reorder buffer in the next section.
> 完成記分板後，執行提供的測試套件，驗證處理器是否正確處理暫存器相依性和運算元旁路。在此階段，某些與亂序提交相關的測試案例可能仍會失敗，這些問題將在下一節實作 ROB 後解決。

### 5. Building the ROB／建立 ROB












