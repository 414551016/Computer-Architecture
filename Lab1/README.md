# Lab 1
- 教學資源：
  - [Lab1](lab.pdf)

本次 Lab 的核心是：把既有的 5-stage RISC-V 流水線處理器，從「只有少量指令、以停頓處理相依性」逐步擴充成支援完整 rv32i、部分 rv32m、資料轉傳（bypassing）與流水化乘除法的版本。
重點可分成四個目標：
- 控制單元擴充（35%）
  > 在 riscvstall 中完成更多 rv32i 指令，例如立即數／暫存器運算、不同寬度與正負號的 load/store、jalr、各類 branch。
  > <br>關鍵是讀懂每條指令在 Decode 階段設定的控制訊號，並讓它們正確隨流水線送到 Execute、Memory、Writeback 階段。
- 補齊乘法高位指令（15%）
  > 實作 mulh、mulhu、mulhsu，分別處理 signed×signed、unsigned×unsigned、signed×unsigned，並取 64-bit 乘積的高 32 bits。
  > <br>除了改乘除法模組與控制／資料路徑，也必須自行撰寫至少一個 assembly 測試來驗證每一條指令。
- 實作資料轉傳 Bypassing（20%）
  > 在 riscvbyp 加入 mux 與控制邏輯，讓 Decode 階段可從 X、M、W 階段直接取得尚未寫回暫存器的結果。
  > <br>目的在減少不必要的 data hazard stall；但 load-use hazard 仍必須停頓，因為載入資料在記憶體回應前還不能轉傳。這是本次 Lab 最重要的流水線效能觀念。
- 整合流水化乘除法單元（30%）
  > 在 riscvlong 導入提供的四級流水化 Mul/Div 單元，讓乘除法執行期間，沒有相依性的其他指令仍可繼續前進。
  > <br>你要延長主流水線、重新處理 stall／bypass／資料相依；代價是所有指令的延遲都可能增加，因此需要用 benchmark 觀察效能取捨。

建議實作順序：
- 先在 riscvstall-CoreCtrl.v 逐條完成指令並立刻跑對應測試。
- 實作並測試三條高位乘法。
- 用 setup.sh 將成果帶到 riscvbyp，完成 forwarding 與「只針對 load-use 停頓」。
- 再帶到 riscvlong，整合流水化乘除法與新的 hazard handling。
- 以一般記憶體與 random-delay 記憶體測試，必要時用 VCD／gtkwave 看波形除錯。
- 跑四個 C benchmark，比較 stall 與 bypass 版本的統計結果。

繳交前要特別確認：
- 自訂的 mulh、mulhu、mulhsu 測試，以及至少一個 bypass 或曾遇到 bug 的測試都已加入編譯與 Makefile。
- 三個目錄 riscvstall、riscvbyp、riscvlong 的原始碼都在正確位置。
- 清除產生的 build 檔後，從 lab1 的上一層建立 student_id-lab1.tar.gz，再上傳 e3。
- 評分比例為 35%／15%／20%／30%，因此不要只完成控制訊號表；bypassing 與流水化 Mul/Div 也是主要成果。
