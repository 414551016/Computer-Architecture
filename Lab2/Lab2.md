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




























