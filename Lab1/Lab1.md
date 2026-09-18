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

### 1. Reminder - 提醒
- **Submission Deadline: 9/28 (Mon) 11:59 p.m.**  
  >繳交期限：9 月 28 日（週一）晚上 11:59。
- **Please refer to Lab 0 for the academic integrity requirements.**  
  >學術誠信規定請參閱 Lab 0。
- **No sharing or distribution of lab materials is allowed.**  
  >不允許分享或散布實驗教材。

### 2. Setup 
#### 2.1 Getting Started - 環境與開始
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

#### 2.2 Building the Project - 建置專案



















