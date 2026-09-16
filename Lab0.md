# Lab 0

Lab0 不是要你設計 CPU 或寫 Verilog 功能的實作題；它是後續實驗的「環境建置與學術誠信」說明。
<br>你需要完成的實作重點：
- 若使用 Windows，安裝 WSL2 與 Ubuntu 24.04。
- 在 Ubuntu 內安裝基本建置工具：build-essential、autoconf。
- 安裝三個後續實驗會用到的工具：
  - GTKWave：查看 Verilog 模擬的波形。
  - Icarus Verilog 12：編譯與模擬 Verilog。
  - RISC-V GNU Compiler Toolchain 14.2：把 RISC-V 程式編譯為實驗所需格式。
- 將 RISC-V 與 Icarus Verilog 的執行檔路徑加入 ~/.bashrc，重新載入設定。
- 以 iverilog -v、gtkwave -v、riscv32-unknown-elf-gcc -v 驗證三項工具都可正常執行。

若你是 Windows 使用者，建議依此順序操作：先裝 WSL/Ubuntu → 安裝基本工具 → GTKWave → RISC-V toolchain → Icarus Verilog → 最後才做三個版本檢查。版本指令能成功顯示資訊，才表示後續 Lab 的 Verilog 模擬、波形檢視與 RISC-V 編譯環境已備妥。
另外，Lab0 特別強調：
- 不得把程式碼分享給組別外同學，也不可抄用往年報告或材料。
- 可以使用生成式 AI 協助學習，但必須自行理解、查證與改寫；提交內容的正確性與原創性仍由你負責。
- 不可將實驗材料、程式或報告公開至 GitHub 等平台；違規可能導致嚴重處分，甚至課程不及格。
- macOS 流程使用 Xcode Command Line Tools、Homebrew、~/.zshrc；Intel Mac 或安裝異常則依講義建議聯絡助教。

**一句話總結：Lab0 的目標是建立「能編譯 RISC-V、模擬 Verilog、看波形」的環境，並確保你理解這門課對原創性與程式保密的要求。**
