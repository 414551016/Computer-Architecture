# Computer Architecture
> 計算機架構
#  Lab 1: [Pipelined](https://github.com/414551016/Computer-Architecture/blob/main/Definition%20of%20terms.md#%E4%BD%95%E8%AC%82-pipelined%E7%AE%A1%E7%B7%9A%E5%8C%96) [RISC-V](https://github.com/414551016/Computer-Architecture/blob/main/Definition%20of%20terms.md#%E4%BD%95%E8%AC%82-risc-v) Processor
> 實驗一：具管線化的 RISC-V 處理器

**Institute of Computer Science and Engineering, National Yang Ming Chiao Tung University. Revision: 9-14-2026.**  
> 國立陽明交通大學資訊工程學系。版本：2026-09-14。

**In this lab, we will work with a 5-stage pipelined RISC-V processor and expand its functionality. The goal is to fully implement the rv32i ISA, add a diagnostic instruction (CSRW), and support a subset of rv32m, enabling C programs to run without system calls. Detailed instruction specifications are provided in the included `riscv-isa.txt`.** 
>本實驗要使用一個五級管線 RISC-V 處理器，並擴充它的功能。目標是完整實作 `rv32i` 指令集、加入診斷指令 `CSRW`，並支援部分 `rv32m` 指令，使 C 程式不依賴系統呼叫也能執行。每一條指令的詳細規格在附帶的 `riscv-isa.txt`。

**You will begin with a reference processor that has a complete datapath but limited control logic. Your task is to extend the control unit to support the full instruction set, incorporate pipelined controls, and add bypassing to reduce stalls and improve performance.**  
>起始版本的資料路徑（datapath）已完整，但控制邏輯有限。你的任務是擴充控制器以支援完整指令集，讓控制訊號隨管線傳遞，並加入旁路（bypassing）以減少停頓、改善效能。

**Pipelining increases throughput by overlapping instruction execution, but also introduces hazards. The reference design uses stalling and squashing; in this lab, you will implement bypassing as an optimization and evaluate its trade-offs.**  
>管線化藉由重疊多條指令的執行提高吞吐量，但也會造成 hazard（相依／衝突）。參考設計使用 stall（停住）與 squash（取消錯誤路徑指令）；本實驗要把 bypassing 作為最佳化，並觀察它的取捨。

**This lab provides experience in:**  
>本實驗可學習：

- **Understanding and extending instruction set architectures (ISAs).**  
  >理解並擴充指令集架構（ISA）。
- **Exploring pipelined processor microarchitecture.**  
  >探索管線式處理器的微架構。
- **Applying techniques to handle data and control hazards.**  
  >使用技術處理資料 hazard 與控制 hazard。

## 1. Reminder - 提醒
- **Submission Deadline: 9/28 (Mon) 11:59 p.m.**  
  >繳交期限：9 月 28 日（週一）晚上 11:59。
- **Please refer to Lab 0 for the academic integrity requirements.**  
  >學術誠信規定請參閱 Lab 0。
- **No sharing or distribution of lab materials is allowed.**  
  >不允許分享或散布實驗教材。

## 2. Setup 
### 2.1 Getting Started - 環境與開始
**Once you have the Lab 1 materials, extract them by entering the following commands:**  
>取得 Lab 1 材料後，以以下指令解壓縮並設定實驗根目錄：
```bash
tar -xf lab1.tar
cd lab1
export LAB1_ROOT=$PWD
```

**Within the lab root directory, you will find eight subdirectories, each serving a specific purpose:**  
>在實驗根目錄中有八個子目錄，各自用途如下：
- **`build`: Makefile and compiled code**
  >`build`：Makefile 與編譯產物。
- **`imuldiv`: Integer multiply/divide unit**
  >`imuldiv`：整數乘除法單元。
- **`riscvstall`: Pipelined RISC-V processor with stalling**
  >只有 stall 的管線式處理器。
- **`riscvbyp`: Pipelined RISC-V processor with bypassing**
  >具 bypassing 的管線式處理器。
- **`riscvlong`: Pipelined RISC-V processor with bypassing and a pipelined mul/div unit**
  >具有 bypassing 與管線化乘除法單元的處理器。
- **`tests`: Assembly test build system**
  >組合語言測試的建置系統。
- **`ubmark`: Benchmarks for evaluation**
  >用於效能評估的 benchmark。
- **`vc`: Additional Verilog components**
  >其他 Verilog 元件。

**The `tests` directory contains a build system that compiles assembly tests into Verilog memory hex (`.vmh`) files for initializing processor memory. Inside its `riscv` subdirectory are tests that check each ISA instruction, plus a few for pseudo-instructions. These are not implemented in hardware but expanded by the compiler or assembler into actual instructions.**  
>`tests` 目錄的建置系統會將組合語言測試編譯成 Verilog 記憶體十六進位檔（`.vmh`），用來初始化處理器記憶體。其中的 `riscv` 子目錄，包含各 ISA 指令的測試，以及少量虛擬指令測試。虛擬指令不需由硬體直接實作；編譯器或組譯器會先把它展開成真正的指令。

**Always test each newly implemented instruction with its corresponding assembly test before moving on. See Section 4 for testing procedures. Compile the tests as described in Section 4.1 before running them.**  
>每完成一條新指令，務必先跑該指令對應的組合語言測試，再進行下一步。測試流程見第 4 節；執行測試之前，先依第 4.1 節編譯測試。

**The processor source code is provided in three directories: `riscvstall` (stalling only), `riscvbyp` (with bypassing), and `riscvlong` (with a pipelined mul/div unit).**  
>處理器原始碼分為三個目錄：`riscvstall`（僅停頓）、`riscvbyp`（含旁路）、`riscvlong`（含管線化乘除法單元）。

### 2.2 Building the Project - 建置專案
**Before building the project, ensure you have completed the environment setup as outlined in Lab 0. First, compile the tests as described in Section 4.1:**  
>建置專案前，先確認已完成 Lab 0 的環境設定。接著依第 4.1 節先編譯測試：

```bash
cd $LAB1_ROOT/tests
mkdir build && cd build
../configure --host=riscv32-unknown-elf
make
../convert
```

**Next, compile the reference processors and run the RISC-V assembly tests.**  
>接著編譯參考處理器並執行 RISC-V 組合語言測試。

**Note: By default, only the `riscvstall` processor is enabled in the Makefile. After completing the bypass implementation, uncomment the corresponding `riscvbyp` entries in `$LAB1_ROOT/build/Makefile`. Similarly, after completing `riscvlong`, uncomment the corresponding entries before building and running its tests.**  
>注意：預設 Makefile 只啟用 `riscvstall`。完成 bypass 後，必須在 `$LAB1_ROOT/build/Makefile` 取消 `riscvbyp` 相關項目的註解。完成 `riscvlong` 後，也要取消它的相關項目註解，才能建置與測試。

```bash
cd $LAB1_ROOT/build
make
make check
make check-asm-riscvstall
make check-asm-rand-riscvstall
make check-asm-riscvbyp
make check-asm-rand-riscvbyp
make check-asm-riscvlong
make check-asm-rand-riscvlong
```

**Running `make` builds the processor simulators. Targets without `-rand` use synchronous memory with a fixed 1-cycle response. Targets with `-rand` use memory with random delays. To see how tests are defined, open the Makefile and check the “List of Assembly Tests” section. Add new tests by appending to the `tests` variable.**  
>`make` 會建立處理器模擬器。名稱沒有 `-rand` 的目標使用固定一個 cycle 回應的同步記憶體；有 `-rand` 的目標使用隨機延遲的記憶體。要查看測試如何定義，開啟 Makefile 的「List of Assembly Tests」區段；新增測試時，把檔名加到 `tests` 變數。

**To use the simulator without random delays, execute `make check-asm-riscvstall`. Alternatively, to introduce random delays, run `make check-asm-rand-riscvstall`, which uses `riscvstall-randdelay-sim` instead of `riscvstall-sim`.**  
>不使用隨機延遲時，執行 `make check-asm-riscvstall`；要模擬隨機延遲時，執行 `make check-asm-rand-riscvstall`，它使用 `riscvstall-randdelay-sim`，而非 `riscvstall-sim`。

**You may also run individual tests directly. For instance, to run `riscv-addi`:**  
>你也可以直接執行單一測試。例如要跑 `riscv-addi`：

```bash
cd $LAB1_ROOT/build
./riscvstall-sim +exe=../tests/build/vmh/riscv-addi.vmh +stats=1
```

**Use `+stats=1` to display statistics (off by default), and `+vcd=1` to generate a waveform file (`.vcd`) viewable in `gtkwave`. Each new run overwrites the file, so rename it if you want to keep it.**  
>`+stats=1` 顯示統計資料（預設關閉）；`+vcd=1` 產生可用 `gtkwave` 開啟的波形檔（`.vcd`）。每次新執行都會覆寫同名波形檔；要保留請先改名。

**The Makefile invokes `riscvstall-sim` and `riscvstall-randdelay-sim` for `make check-asm-riscvstall` and `make check-asm-rand-riscvstall`. The `riscvstall` simulators use the stall-based processor, while the `riscvbyp` simulators target the bypass-based processor. At first both share the same stall-based implementation, but once you add bypassing the two versions diverge.**  
>Makefile 分別以 `riscvstall-sim`、`riscvstall-randdelay-sim` 執行兩種 `riscvstall` 測試。`riscvstall` 模擬器使用 stall 處理器；`riscvbyp` 模擬器使用 bypass 處理器。起初兩者共用 stall 版實作；加入 bypass 後，兩者會分歧。

**Commands such as `make check-asm-`, `make check-asm-rand-`, and `make run-bmark-*` produce a `.vcd` waveform dump for each test. Automatic tests for `riscvstall`, `riscvbyp`, and `riscvlong` run in sequence will overwrite existing `.vcd` files.**  
>`make check-asm-`、`make check-asm-rand-`、`make run-bmark-*` 等指令，會為每個測試產生 `.vcd` 波形檔。依序跑 `riscvstall`、`riscvbyp`、`riscvlong` 的自動測試會覆寫既有 `.vcd`。

## 3 Pipelined 5-Stage RISC-V Processor with Bypassing
**In this lab you will use a fully implemented RISC-V datapath with stalling and a partially completed control unit. The datapath includes the iterative multiply/divide unit.**  
>本實驗使用一個已完成的、採 stall 的 RISC-V 資料路徑與部分未完成的控制器。資料路徑已含反覆運算式（iterative）乘除法單元。

**The lab has four main objectives:**  
>本實驗有四項主要目標：
- 1. **Extend the control unit to support more instructions.**
  >擴充控制器以支援更多指令。
- 2. **Implement additional M-extension instructions.**
  >實作額外的 M extension 指令。
- 3. **Add bypassing to the datapath and the control unit.**
  >在資料路徑與控制器加入 bypassing。
- 4. **Integrate a pipelined multiply/divide unit.**
  >整合管線化乘除法單元。

**Begin with Objective 1 in `riscvstall`. For Objective 2, complete the missing M-extension instructions. Then copy source files to `riscvbyp` for Objective 3, rename the files, and update include paths. Finally move to `riscvlong` for Objective 4 and integrate the pipelined mul/div unit.**  
>先在 `riscvstall` 完成目標一；再補齊目標二缺少的 M extension 指令。之後將原始碼複製到 `riscvbyp`，改名與更新 include path，完成目標三。最後移到 `riscvlong` 整合管線化乘除法單元，完成目標四。

### 3.1 Objective 1: Enhancing the Control Unit - 擴充控制器
**In this objective, you will only modify the control unit (`riscvstall-CoreCtrl.v`). All required datapath inputs and control outputs already exist. Add an entry to the control-output table for every RISC-V instruction. The control-signal columns are predefined; normally no additional signals are needed, except perhaps helper signals for branches.**  
>此目標只修改控制器 `riscvstall-CoreCtrl.v`。資料路徑所需輸入與控制器輸出都已存在。你必須為每條 RISC-V 指令在控制輸出表中加上一列。控制訊號欄位已事先定義，通常不用再新增訊號；分支指令可能需要輔助訊號。

**The processor has five stages: Fetch (F), Decode (D), Execute (X), Memory (M), and Writeback (W). Signal suffixes `_Fhl`, `_Dhl`, `_Xhl`, `_Mhl`, `_Whl` identify the stage of use. `hl` means valid for one cycle after a clock edge.**  
>處理器有五級：取指（F）、解碼（D）、執行（X）、記憶體（M）、寫回（W）。訊號後綴 `_Fhl`、`_Dhl`、`_Xhl`、`_Mhl`、`_Whl` 表示該訊號使用的 stage。`hl` 表示時脈邊緣後的一個 cycle 內有效。

**Below are the rv32i and rv32m instructions to be implemented. Refer to `riscv-isa.txt` for details.**  
>以下列出要實作的 `rv32i` 與 `rv32m` 指令；細節請查 `riscv-isa.txt`。

**Already Implemented: Minimal Subset for Assembly Tests**  
>已完成：足以執行基本組合測試的最小子集合

- **Register-Immediate Arithmetic: `addi`, `ori`, `lui`, `auipc`**
  >暫存器－立即數算術。
- **Register-Register Arithmetic: `add`**
  >暫存器－暫存器算術。
- **Memory: `lw`, `sw`**
  >記憶體存取。
- **Jump: `jal`**
  >跳躍。
- **Branch: `bne`, `blt`**
  >分支。
- **Diagnostic: `csrw`**
  >診斷指令。

**rv32im: Subset for Running Raw C Code (No Syscalls)**  
>可執行不含系統呼叫之原始 C 程式的 rv32im 子集合

- **Register-Immediate Arithmetic: `andi`, `xori`, `slli`, `srli`, `srai`, `slti`, `sltiu`**
- **Register-Register Arithmetic: `sub`, `slt`, `sltu`, `sll`, `srl`, `sra`, `and`, `or`, `xor`**
- **Memory: `lb`, `lbu`, `lh`, `lhu`, `sb`, `sh`**
- **Jump: `jalr`**
- **Branch: `beq`, `bge`, `bltu`, `bgeu`**
- **Multiply/Divide: `mul`, `div`, `divu`, `rem`, `remu`**

**The control unit differs from a traditional multi-cycle processor. Instead of a finite-state machine (FSM), control signals are pipelined to the datapath stage where needed. Each control-table row specifies one instruction's control signals, not a state.**  
>本實驗的控制器不同於傳統多周期處理器。它不使用有限狀態機（FSM），而是把控制訊號沿管線送至需要它的資料路徑 stage。控制表的每一列描述一條指令所需的控制訊號，而非一個狀態。

**Table 1: Summary of control signals.**  
>表 1：控制訊號摘要。

| English signal meaning | 中文說明 |
|---|---|
| `INST_VAL`: valid instruction, used for assertions | 有效指令；供 assertion 檢查。 |
| `J_EN`: jump determinable in Decode (`jal`, `jr`) | 解碼期可判定的跳躍。 |
| `BR_SEL`: branch type | 分支型別，決定檢查哪些分支條件。 |
| `PC_SEL`: PC mux select | PC 多工器選擇。 |
| `OP0_SEL` / `OP1_SEL`: operand mux select | 運算元 0／1 多工器選擇。 |
| `RS_EN` / `RT_EN`: read operand from regfile | 是否由暫存器檔讀取運算元；用於判斷 stall 或 bypass。 |
| `ALU_FN`: ALU function | ALU 功能。 |
| `MULDIV_FN`: mul/div function | 乘除法功能。 |
| `MULDIV_EN`: mul/div request valid | 乘除法請求是否有效。 |
| `MULDIV_SEL`: select lower/upper 32 result bits | 選擇乘除結果低／高 32 位元。 |
| `EX_SEL`: execute output mux select | 選擇 ALU 或 mul/div 的執行期輸出。 |
| `MEM_REQ`, `MEM_LEN`, `MEM_SEL` | 記憶體請求、資料長度（word=0、byte=1、halfword=2）、符號／無符號回應選擇。 |
| `WB_SEL`: writeback mux select | 選擇執行期輸出或記憶體回應寫回。 |
| `RF_WEN`, `RF_WADDR` | 暫存器檔寫入啟用與寫入位址。 |
| `CSR_WEN` | CSR 寫入啟用。

**All control signals are set in Decode (D) and pipelined to the stage where they are needed. For example, `alu_fn_Dhl` is set in Decode and becomes `alu_fn_Xhl` in Execute to drive the ALU.**  
>所有控制訊號都在解碼期（D）設定，並沿管線傳到實際需要它們的 stage。例如 `alu_fn_Dhl` 在 D 設定，傳到執行期成為 `alu_fn_Xhl`，用來控制 ALU。

**Instruction encodings, fields, and control-signal fields are defined in `riscv-InstMsg.v`. These parameters are global `define`s beginning with `RISCV_INST_MSG_`, to avoid namespace conflicts.**  
>指令編碼、欄位及控制訊號欄位定義在 `riscv-InstMsg.v`。這些參數是以 `RISCV_INST_MSG_` 開頭的全域 ``define``，用來避免名稱空間衝突。

### 3.2 Example: Adding the `lh` Instruction - 加入 `lh` 指令的範例
**This section demonstrates adding `lh` from the rv32i ISA. Because the datapath already supports all rv32i instructions, only the control unit changes.**  
>本節以 rv32i 的 `lh` 為例，說明如何加一條指令。因資料路徑已支援所有 rv32i 指令，所以只需修改控制器。

**For subword memory operations such as `lb`, use `lw` as a model: `lw` reads operand 0 from the register file and operand 1 as an immediate, uses the ALU to form the address, issues a memory request in X, and writes the response in W.**  
>對 `lb` 這種子字組記憶體操作，可參考 `lw`：`lw` 從暫存器檔讀取運算元 0，使用立即數作為運算元 1，ALU 在 X 算出位址，於 X 發出記憶體請求，最後在 W 寫回回應資料。

**`lh` is the same as `lw`, except that it reads a halfword and sign-extends it. Set memory length to 2 (`ml_h`) and choose the sign-extended halfword response (`dmm_h`) in the control-output table.**  
>`lh` 與 `lw` 相同，差別是它讀取 halfword（半字，16 位元）後要做 sign extension（符號延伸）。在控制表中，記憶體長度設為 2（`ml_h`），回應多工器選擇符號延伸的 halfword（`dmm_h`）。

```verilog
`RISCV_INST_MSG_LH : cs={y, n, br_none, pm_p, am_rdat, y, bm_imm_i, n,
alu_add, md_x, n, mdm_x, em_x, ld, ml_h, dmm_h, wm_mem, y, rd, n};
```

**Ensure this appears on one source-code line. Add `riscv-lh.vmh` to the Makefile's `tests` list, then run `make check-asm-riscvstall`. For most instructions, adding a control-table row is sufficient, but verify the datapath and select appropriate controls.**  
>確定上列在原始碼中是一整行。將 `riscv-lh.vmh` 加入 Makefile 的 `tests` 清單，然後執行 `make check-asm-riscvstall`。多數指令只要新增控制表的一列即可，但仍須確認資料路徑並選擇正確控制訊號。

### 3.3 Objective 2: Remaining RISC-V M Instructions (`mulh`, `mulhu`, `mulhsu`)
**Three multiply instructions are missing: `mulh`, `mulhu`, and `mulhsu`. Implement them and write at least one assembly test for each.**  
>尚缺三條乘法指令：`mulh`、`mulhu`、`mulhsu`。必須實作它們，且每條至少撰寫一個組合語言測試。

**They return the high 32 bits of a 64-bit product:**  
>它們回傳 64 位元乘積的高 32 位元：

- **`mulh`: signed × signed**
  >有號數 × 有號數。
- **`mulhu`: unsigned × unsigned**
  >無號數 × 無號數。
- **`mulhsu`: signed × unsigned**
  >有號數 × 無號數。

**Study existing multiplication code. In particular, extend `imuldiv-IntMulIterative.v` and `imuldiv-IntMulDivIterative.v`, then update datapath and control logic so each instruction generates the correct high 32-bit result.**  
>研究既有乘法程式，特別是擴充 `imuldiv-IntMulIterative.v` 與 `imuldiv-IntMulDivIterative.v`；再更新資料路徑與控制邏輯，讓每條指令產生正確的高 32 位元結果。

### 3.4 Objective 3: Implementing Bypassing - 實作旁路
**After completing `riscvstall`, copy source files to `riscvbyp` and run:**  
>完成 `riscvstall` 後，把原始碼複製到 `riscvbyp` 並執行：

```bash
cd $LAB1_ROOT/riscvbyp
./setup.sh
```

**`setup.sh` copies files from `../riscvstall`, renames files and relevant build entries from the `riscvstall` prefix to `riscvbyp`, and performs basic build updates. Verify filenames afterward.**  
>`setup.sh` 會從 `../riscvstall` 複製檔案，將檔名與相關建置項目的 `riscvstall` 前綴改為 `riscvbyp`，並做基本建置更新。之後請確認檔名正確。

**Add bypass muxes in `riscvbyp-CoreDpath.v`; Figure 1 helps identify the muxes and the values that must be forwarded. Add control signals in `riscvbyp-CoreCtrl.v` to select the bypass muxes.**  
>在 `riscvbyp-CoreDpath.v` 加入 bypass 多工器；圖 1 可協助找出位置與應轉送的值。在 `riscvbyp-CoreCtrl.v` 加入控制訊號，選擇這些 bypass 多工器。

**Bypassing forwards values needed in Decode before they reach the register file. The processor must be fully bypassed, forwarding from X, M, and W. Helper signals may describe whether a source register should be forwarded; for example, `rs1_X_byp_Dhl`. These helper signals determine bypass mux selection.**  
>Bypassing 會在值尚未寫入暫存器檔之前，將 Decode 所需的值直接轉送過去。處理器必須完整支援從 X、M、W 轉送。可使用輔助訊號描述某來源暫存器是否應被轉送，例如 `rs1_X_byp_Dhl`；它們決定 bypass mux 的選擇。

**Finally, integrate the modified control unit and datapath in `riscvbyp-Core.v`. Bypassing does not remove all stalls: a load-use hazard must still stall because a load's memory response is not yet available. Modify stall logic so that it stalls only for load-use hazards, not every data hazard. Introduce a pipelined `is_load` indicator for this purpose.**  
>最後在 `riscvbyp-Core.v` 整合修改後的控制器與資料路徑。Bypassing 並不能消除所有 stall：load-use hazard 仍必須 stall，因為 load 的記憶體回應尚未可用。修改 stall 邏輯，使其只在 load-use hazard 時停頓，而不是每種資料相依都停頓。可加入沿管線傳遞的 `is_load` 指示訊號來判斷。

### 3.5 Additional Architectural Details - 補充架構細節
**Bubble bits indicate whether a stage contains an invalid entry. When a stage is stalled or squashed while the next stage can advance, insert a bubble into that next stage. If the next stage is also stalled, retain its pipeline state. Invalid bubbles must not cause side effects such as register writes or memory requests.**  
>Bubble bit 表示某 pipeline stage 是否為無效項目。若一個 stage 被 stall 或 squash，但下一個 stage 可前進，便在下一個 stage 插入 bubble；若下一 stage 也被 stall，就維持它原本的 pipeline state。無效 bubble 不可造成副作用，例如寫入暫存器或發出記憶體請求。

**Instruction and data memory use a `val/rdy` handshake: a response is accepted on a rising clock edge only when both `val` and `rdy` are asserted. If the processor cannot accept a response, the memory model retains pending information until transfer completes. Random-delay memory may delay response availability.**  
>指令與資料記憶體使用 `val/rdy` 握手：只有在上升緣時 `val` 與 `rdy` 都為 asserted，回應才被接受。若處理器不能接受回應，記憶體模型會保留待處理資訊直到傳輸完成。random-delay 記憶體也可能延後回應可用時間。

**This backpressure lets memory transfers wait while the processor is stalled. The reference core needs no separate response-side skid buffer. When modifying the pipeline, consume every response exactly once and keep response-ready signals consistent with the accepting stage.**  
>這種 backpressure（反壓）可讓記憶體傳輸在處理器 stall 時等待。參考 core 不需獨立的 response-side skid buffer。修改管線時，必須確保每個回應剛好被消費一次，且 response-ready 訊號要與實際接受回應的 stage 一致。

### 3.6 Objective 4: Integrating a Pipelined MulDiv Unit - 整合管線化乘除法單元
**The reference core uses iterative mul/div and stalls D and X until a result is ready. It is simple but inefficient. Integrate pipelined mul/div so independent instructions continue in parallel, and stall only for a true data dependency.**  
>參考 core 使用 iterative mul/div，會讓 D、X stage 一直 stall 到結果完成。這很簡單但效率差。此目標要整合 pipeline mul/div，使獨立指令能平行繼續，只有真正資料相依時才 stall。

**A functional 4-stage pipelined model is provided in `riscvlong/riscvlong-CoreDpathPipeMulDiv.v`. It performs multiplication/division with functional operators (`*`, `/`, `%`) in its first stage and uses three dummy stages to pipeline the result. Bypassing inside the mul/div unit is not allowed.**  
>`riscvlong/riscvlong-CoreDpathPipeMulDiv.v` 已提供功能性四級 pipeline 模型。第一級以運算子 `*`、`/`、`%` 計算乘除法，後三級是用來管線化結果的 dummy stage。**不允許在 mul/div 單元內部做 bypass。**

**Your goal is to support additional M instructions, integrate the unit, and implement logic that executes it in parallel while correctly managing hazards.**  
>目標是支援額外 M 指令、整合此單元，並完成讓它平行執行及正確管理 hazard 的邏輯。

```bash
cd $LAB1_ROOT/riscvlong
./setup.sh
```

**Replace iterative `imuldiv_IntMulDivIterative` with the provided pipelined unit: include `riscvlong-CoreDpathPipeMulDiv.v` in `riscvlong-CoreDpath.v`, update affected include paths, add stall/bypass signals in `riscvlong-CoreCtrl.v` and `riscvlong-CoreDpath.v`, then wire everything in `riscvlong-Core.v`.**  
>以提供的管線化單元取代 iterative `imuldiv_IntMulDivIterative`：在 `riscvlong-CoreDpath.v` include `riscvlong-CoreDpathPipeMulDiv.v`，更新受影響的 include path，在 `riscvlong-CoreCtrl.v`、`riscvlong-CoreDpath.v` 加入 stall／bypass 訊號，最後在 `riscvlong-Core.v` 把各部分接好。

**A direct solution is to extend the main pipeline by two stages. The first two mul/div stages overlap X and M; the final two are inserted before W. Feed the mul/div unit immediately after Decode rather than after Execute, and connect pipeline stall signals correctly. This increases latency for all instructions, not only `mul` and `div`, so benchmark performance is expected to change.**  
>直接的做法是主管線加長兩級。mul/div 前兩級與既有 X、M 重疊；最後兩級插在 W 前。mul/div 應在 Decode 後立即接收資料，而不是 Execute 後；也必須正確連接管線的 stall 訊號。這會增加**所有**指令（不僅 `mul`、`div`）的延遲，因此 benchmark 效能預期會改變。

**After extending the pipeline, add forwarding, stalling, and bypassing for hazards. More efficient multi-cycle designs are possible, but this simplified design is sufficient for the lab.**  
>延長管線後，要為 hazard 加入 forwarding、stalling、bypassing。雖可有更有效率的多周期設計，但此簡化設計已足以完成本實驗。

## 4 Testing Methodology - 測試方法
**Most assembly tests are provided. You must create custom tests for `mulh`, `mulhu`, and `mulhsu`, and at least one additional test that either targets a bug you found or verifies bypass paths. You may use macros in `riscv-macros.h` or raw assembly.**  
>大部分組合測試已提供。但你必須為 `mulh`、`mulhu`、`mulhsu` 撰寫自訂測試，並額外至少寫一個測試：針對你遇到的 bug 或驗證完成版處理器的 bypass path。可用 `riscv-macros.h` 的巨集或直接寫組合語言。

**All tests are in `$LAB1_ROOT/tests/riscv`. New tests must follow existing naming conventions, be included in the appropriate `.mk` file, and have their `.vmh` name added to the `tests` variable in `$LAB1_ROOT/build/Makefile`.**  
>所有測試位於 `$LAB1_ROOT/tests/riscv`。新測試必須遵循既有命名規則、加入適當的 `.mk` 檔，並將它的 `.vmh` 檔名加入 `$LAB1_ROOT/build/Makefile` 的 `tests` 變數。

**Test files normally include `riscv-macros.h` and begin with `TEST_RISCV_BEGIN` to set up `.text`; every test ends with `TEST_RISCV_END`, which includes pass/fail routines.**  
>測試檔通常 include `riscv-macros.h`，並以 `TEST_RISCV_BEGIN` 設定 `.text` 區段開頭；每個測試以 `TEST_RISCV_END` 結束，其中含有 pass／fail 例程。

**`TEST_IMM_OP(instruction, source value, immediate value, expected result)` is a common macro for immediate arithmetic tests.**  
>`TEST_IMM_OP(指令, 來源值, 立即數值, 預期結果)` 是常用的立即數算術測試巨集。

## Page 8 - Building tests and evaluation
**For example, the macro can verify `0 + 0 = 0`, `1 + 1 = 2`, and so on. Macro implementations are in `riscv-macros.h`. Usually `csrw` writes a special CSR so the simulator can track status: value 1 means pass; a line number means failure.**  
>例如，此巨集可驗證 `0 + 0 = 0`、`1 + 1 = 2` 等。巨集的實作在 `riscv-macros.h`。通常 `csrw` 會把資料寫入特殊 CSR，讓模擬器追蹤狀態：寫入 1 表示通過；寫入行號表示失敗位置。

**Other common macros include `SRC0_EQ_X` macros, which test matching source and destination registers, and `BYP` macros, which verify bypassing logic.**  
>其他常見巨集有 `SRC0_EQ_X`，用來測來源與目的暫存器相同的情況；以及 `BYP`，用來驗證 bypassing 邏輯。

### 4.1 Compiling New Assembly Tests - 編譯新的組合測試
**To see currently compiled tests, open `$LAB1_ROOT/tests/riscv/riscv.mk`. To compile tests, create a separate `build` directory and run `configure` for the RISC-V cross compiler:**  
>要看目前被編譯的測試，開啟 `$LAB1_ROOT/tests/riscv/riscv.mk`。編譯測試時，建立獨立的 `build` 目錄，並對 RISC-V cross compiler 執行 `configure`：

```bash
# Assembly tests
cd $LAB1_ROOT/tests
mkdir build
cd build
../configure --host=riscv32-unknown-elf

# Benchmarks
cd $LAB1_ROOT/ubmark
mkdir build
cd build
../configure --host=riscv32-unknown-elf
```

**The `--host=riscv32-unknown-elf` option chooses the course cross compiler instead of standard `gcc`. Then compile and convert the assembly tests:**  
>`--host=riscv32-unknown-elf` 指定使用課程提供的 cross compiler，而不是一般 `gcc`。接著編譯並轉換組合測試：

```bash
make
../convert
```

**`make` compiles assembly into binaries. Since the Verilog processor cannot run these directly, `convert` creates object dumps and `.vmh` files in `bin`, `dump`, and `vmh`. The simulator can load and run a test as long as its `.vmh` is in `vmh`. Add its filename to the Makefile. Linker warnings about missing `_start` are expected because the simulator uses a custom entry point.**  
>`make` 將組合語言編譯成執行檔。但 Verilog 處理器不能直接執行它們，所以 `convert` 會建立 object dump 與 `.vmh`，放入 `bin`、`dump`、`vmh`。只要需要的 `.vmh` 在 `vmh`，模擬器就能載入測試執行。記得把檔名加入 Makefile。連結器警告缺少 `_start` 是預期現象，因為模擬器使用自訂 entry point。

**If you add or modify assembly tests, rerun `make` and `../convert` in the build directory. Full setup is needed only when the build directory was deleted. `make install` is not required.**  
>若新增或修改組合測試，只須在 build 目錄重跑 `make` 與 `../convert`。只有刪掉 build 目錄後才需要完整設定；本實驗不需 `make install`。

### 5 Evaluation - 評估
**Evaluation uses C benchmarks in `$LAB1_ROOT/ubmark`:**  
>評估使用 `$LAB1_ROOT/ubmark` 的 C benchmarks：

- **`ubmark-vvadd.c`: Vector-vector addition**
  >向量加向量。
- **`ubmark-cmplx-mult.c`: Complex multiplication**
  >複數乘法。
- **`ubmark-masked-filter.c`: Masked filtering**
  >遮罩式過濾。
- **`ubmark-bin-search.c`: Binary search**
  >二元搜尋。

**Run all benchmarks in `build`; statistics are saved automatically in `.out` files. `riscvstall` uses the suffix `-stall.out`; `riscvbyp` uses `-byp.out`. For example, the `ubmark-vvadd.c` output for `riscvstall` is `ubmark-vvadd-stall.out`. To run the stall benchmarks:**  
>在 `build` 執行所有 benchmark；統計資料會自動存到 `.out`。`riscvstall` 使用 `-stall.out` 後綴，`riscvbyp` 使用 `-byp.out`。例如，`riscvstall` 執行 `ubmark-vvadd.c` 的輸出為 `ubmark-vvadd-stall.out`。執行 stall benchmark：

```bash
cd $LAB1_ROOT/build
make run-bmark-riscvstall
```

將上述目標中的 `riscvstall` 換成 `riscvbyp`，即可執行 bypass 版本。

## 6 Submission 
### 6.1 Modified Files - 繳交／應修改檔案

**For this assignment, the following files should be modified:**  
>本作業預期修改下列檔案：

```text
riscvstall-CoreCtrl.v, riscvstall-InstMsg.v
imuldiv-IntMulIterative.v, imuldiv-IntMulDivIterative.v,
imuldiv-MulDivReqMsg.v
riscvbyp-CoreCtrl.v, riscvbyp-CoreDpath.v, riscvbyp-Core.v
riscvlong-CoreCtrl.v, riscvlong-CoreDpath.v, riscvlong-Core.v,
riscvlong-CoreDpathPipeMulDiv.v
```

### 6.2 Deliverables - 繳交成果

**Submit a `.tar.gz` of the working directory and preserve the original structure. Ensure sources are in `$LAB1_ROOT/riscvstall`, `$LAB1_ROOT/riscvbyp`, and `$LAB1_ROOT/riscvlong`. Before packaging, remove generated files:**  
>繳交工作目錄的 `.tar.gz`，且要保留原始目錄結構。確認原始碼位於 `$LAB1_ROOT/riscvstall`、`$LAB1_ROOT/riscvbyp`、`$LAB1_ROOT/riscvlong`。打包前先移除編譯產物：

```bash
cd $LAB1_ROOT/build
make clean
cd $LAB1_ROOT/tests
rm -rf build
cd $LAB1_ROOT/ubmark
rm -rf build
```

**Create the tarball:**  
>建立壓縮檔：
```bash
cd $LAB1_ROOT
cd ..
tar -cvzf student_id-lab1.tar.gz lab1
```

**The submission must include `riscvstall` source, `riscvbyp` source, `riscvlong` source, and the additional M-extension assembly tests.**  
>繳交檔必須包含：`riscvstall` 原始碼、`riscvbyp` 原始碼、`riscvlong` 原始碼，以及額外 M extension 組合測試。

### 6.3 Submission Instructions - 繳交說明

- **Ensure code is inside the `lab1` folder. If the tarball is not created from this folder, grading will not be possible.**  
 > 確認程式碼位於 `lab1` 資料夾內。若壓縮檔不是從此資料夾建立，助教將無法評分。
- **Submit the tarball via e3.**  
  >透過 e3 繳交壓縮檔。

## 7 Grading Rubric - 評分標準
| Objective | 中文 | 比例 |
|---|---|---:|
| Objective 1: RISCV-stall | 補齊 stall 處理器控制器 | 35% |
| Objective 2: RISC-V M Instructions | 實作額外 M 指令 | 15% |
| Objective 3: RISCV-bypass | 實作 bypass 處理器 | 20% |
| Objective 4: RISCV-long | 整合長管線與 pipeline mul/div | 30% |

## 8 Tips - 提示
- **Use incremental development - never code everything at once and hope it works.**  
  >採漸進式開發；不要一次改完所有程式才期待它通過。
- **Use `gtkwave` to debug with waveforms.**  
  >使用 `gtkwave` 透過波形除錯。
- **Take advantage of the unit testing framework.**  
  >善用單元測試框架。
- **Sketch the hardware before coding.**  
  >寫程式前先畫出硬體資料流。
- **Define control-datapath interactions clearly.**  
  >清楚定義控制器和資料路徑間的互動。

## 9 Acknowledgments - 致謝

**This lab is adapted from ECE 4750 at Cornell University and ECE 475 at Princeton University.**  
>本實驗改編自 Cornell University 的 ECE 4750 與 Princeton University 的 ECE 475。

**Figure 1: Datapath**  
>圖 1：資料路徑。**
圖中核心資料流的英文／中文對照如下：

| English label | 中文 |
|---|---|
| Fetch / Decode / Execute / Memory / Writeback | 取指／解碼／執行／記憶體／寫回五級管線。 |
| PC | 程式計數器。 |
| Inst Mem | 指令記憶體。 |
| Reg File | 暫存器檔。 |
| Data Mem | 資料記憶體。 |
| ALU | 算術邏輯單元。 |
| Muldiv | 乘除法單元。 |
| Subword | 子字組資料處理（byte／halfword 的符號或零延伸）。 |
| `op0_mux`, `op1_mux`, `execute_mux`, `wb_mux`, `pc_mux` | 分別選擇運算元、執行結果、寫回資料、下一個 PC 的多工器。 |
| `branch_targ`, `J_targ`, `Jr_targ` | 分支、`jal`、`jalr` 的目標位址。 |
| `rf_rdata*`, `rf_wen_out`, `rf_waddr` | 暫存器檔讀取資料、寫入啟用、寫入位址。 |
| `dmemreq_*`, `dmemresp_mux_sel` | 資料記憶體請求／回應相關訊號。 |

> 初學者讀圖方式：先沿著一條普通 `add` 指令走 F→D→X→M→W；接著比較 `lw`、branch、`mul` 各自在哪個 mux 或單元選擇不同路徑。這能幫助你理解控制表的每個欄位。










