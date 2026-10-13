# Lab3 (2026-10-13) Week 6
## 教學資源：
- [［Lab3.pdf］](https://github.com/414551016/Computer-Architecture/blob/main/Lab3_Week6/lab3.pdf)
- Prompt：
  - 請將本作業lab3.pdf內容，以英/中翻譯比對
    <br>請說明本作業重點內容及你的看法，最後以250字內總結
- Prompt：作業說明
  - 請說明本次Lab3作業內容、重點及目標為何？
  - 我是初學者，我該如何完成作業規定內容，請詳細說明作業步驟為何？
  - 好的，請先幫我完成本次作業規定任務及目標，之後我再上傳到E3。

本實驗專案旨在指導學生動手設計與優化一個雙發射超純量 RISC-V 處理器。在第一部分中，學生必須親自建構關鍵的控制邏輯、指令導向機制與分數計分板，以確保處理器能夠安全且有效率地同步執行兩個指令，同時處理各種資料相依性。隨後的第二部分則挑戰學生透過精進硬體資源利用率與排程策略來突破效能瓶頸，藉此提升程式執行速度並達成指定的效能等級。整個學習過程涵蓋了從基礎功能實現、效能分析到進階微架構優化的完整電腦結構設計流程。

- 一、 Lab3.pdf 內容英中對照翻譯

  Computer Architecture Lab 3: Superscalar RISC-V Processor | 電腦架構實驗三：超純量 (Superscalar) RISC-V 處理器
  - 簡介 (Introduction)
    <br>In this lab, you will design and implement a two-wide superscalar processor. We provide a functional datapath, and your task will be implementing the necessary control logic, instruction steering mechanism, and a scoreboard to enable the processor to execute two instructions per cycle efficiently. 
    > 在本次實驗中，您將設計並實作一個雙發射（Two-Wide）超純量處理器。我們提供了一個可運作的資料通道（Datapath），您的任務是實作必要的控制邏輯、指令轉向/轉發機制（Instruction Steering Mechanism）以及記分板（Scoreboard），以使處理器能夠高效地每個週期執行兩條指令。
    
    This lab will provide you with experience in: | 本實驗將為您提供以下經驗：
    - The principles of superscalar processor design and multi-issue pipelines. 
      >超純量處理器設計與多發射管線（Multi-issue Pipelines）的基本原理。
    - How to implement control logic and instruction steering for in-order execution.
      > 如何為順序執行（In-order Execution）實作控制邏輯與指令轉向機制。
    - The use of a scoreboard to manage dependencies and maximize instruction throughput. 
      > 如何使用記分板來管理資料相依性（Dependencies）並最大化指令吞吐量。
  - 1. 提醒事項 (1 Reminder)
    - Submission Deadline: 11/16 (Mon) 11:59 p.m. <br>繳交期限：11 月 16 日（星期一）晚上 11:59。
    - Please refer to Lab 0 for the academic integrity requirements.<br>學術誠信要求請參閱 Lab 0。
    - No sharing or distribution of lab materials is allowed. <br>禁止分享或散布實驗材料。
  - 2. 環境設定 (2 Setup)
    - 2.1 Getting Started | 2.1 開始使用
      <br>Once you have the Lab 3 materials, extract them by entering the following commands: TC: 取得 Lab 3 材料後，請輸入以下指令解壓縮：
      ```
      % tar -xzf lab3.tar.gz
      % cd lab3
      % export LAB3_ROOT=$PWD
      ```

      Within the lab root directory, you will find eight subdirectories, each serving a specific purpose: TC: 在實驗根目錄下，您會找到八個子目錄，各自有特定的用途：
      - build: Contains the Makefile and compiled code. TC: build：包含 Makefile 與編譯後的程式碼。
      - imuldiv: Integer multiply/divide unit. TC: imuldiv：整數乘除法單元。
      - riscvssc_part1: Superscalar RISC-V processor source code. TC: riscvssc_part1：超純量 RISC-V 處理器原始碼。
      - riscvssc_part2: Your optimized code. TC: riscvssc_part2：您進行優化後的程式碼。
      - tests: Assembly test build system. TC: tests：組譯測試建立系統。
        - riscv: RISC-V assembly tests. TC: riscv：RISC-V 組譯測試案例。
        - scripts: Miscellaneous scripts for build system. TC: scripts：建置系統所需的其他腳本。
      - ubmark: Benchmarks for evaluation. TC: ubmark：用於效能評估的基準測試（Benchmarks）。
      - Contains additional Verilog components. TC: vc：包含額外的 Verilog 組件。

      Note: When you first run make in $LAB3_ROOT/build, you’ll encounter errors because the control unit in riscvssc_part1 is incomplete. You’ll need to make modifications before compiling and running tests. TC: 注意：當您第一次在 $LAB3_ROOT/build 中執行 make 時會遇到錯誤，因為 riscvssc_part1 中的控制單元尚不完整。您需要在編譯與運行測試前進行修改。

## 請說明本次Lab3作業內容、重點及目標為何？
本次 Lab 3：Superscalar RISC-V Processor（超純量 RISC-V 處理器），核心任務是：
<br>先完成一個「每個時脈週期最多可發出兩條指令」的處理器，再在限定的硬體資源下改善效能，最後用測試與報告證明設計正確、效能有提升。
<br>以下依據你提供的講義（2026/10/4 修訂版）及壓縮檔目錄整理。你這次要求的是作業說明，因此我沒有執行講義中的安裝、修改程式或繳交指令。來源：[［Lab3.pdf］]()












