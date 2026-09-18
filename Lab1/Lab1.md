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














