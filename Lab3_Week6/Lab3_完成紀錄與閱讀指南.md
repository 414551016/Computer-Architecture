# Lab3 完成紀錄與閱讀指南

學號：414551016；本機驗證日期：2026-10-13。

## 交付檔案

- [414551016-lab3.tar.gz](C:/Users/LSS/Documents/1151/1151_535513-計算機架構/Lab3_Week6/submission/414551016-lab3.tar.gz)：程式提交包，根目錄為 lab3，139 個檔案。
- [414551016-lab3-report.pdf](C:/Users/LSS/Documents/1151/1151_535513-計算機架構/Lab3_Week6/submission/414551016-lab3-report.pdf)：繁體中文四頁報告，含設計圖表、瓶頸證據、效能比較及 AI 協助說明。

這兩個檔案已準備好，尚未上傳 E3。請分別上傳；不要把本說明、work 目錄或原始課程壓縮檔當成提交成果。

## 已完成的驗證

| 項目 | Part 1 | Part 2 |
|---|---:|---:|
| 正常指令測試 | 43/43 | 43/43 |
| 隨機延遲指令測試 | 43/43 | 43/43 |
| 正常 benchmark | 4/4 | 4/4 |
| 隨機延遲 benchmark | 4/4 | 4/4 |
| 額外定向與隨機程式，三種延遲 | 39/39 | 39/39 |
| 提交包全新解壓、重新編譯後的四類必要測試 | 94/94 | 94/94 |

另執行原 Makefile 的 13 組元件測試，未出現 FAILED。正式的八個 make 測試目標也逐一執行完成，並核對每項結果，未以指令結束碼代替測試內容。

| Benchmark | Part 1 正常週期 | Part 2 正常週期 | Level 2 上限 |
|---|---:|---:|---:|
| vvadd | 1424 | 1191 | 1200 |
| bin-search | 1578 | 1213 | 1300 |
| cmplx-mult | 3826 | 3304 | 3500 |
| masked-filter | 8809 | 6998 | 7500 |

四個公開測試都符合 Level 1 與 Level 2。Level 3 的公開／隱藏測試排名仍由課程端評定，不能以本機結果宣稱已取得排名分數。也未做硬體綜合、面積與時序收斂。

## Part 1：你需要理解的設計

1. A 能執行全部支援指令；B 只能執行簡單 ALU。兩條都需要 A 時必須分開。
2. 第二條讀第一條的結果是 RAW；兩條寫同一非零目的暫存器是 WAW。這兩種情況不能同時發射。
3. 只發出第一條時，consumed0_Dhl 記住它已執行。保留原本兩條指令及其 PC，下一次只發出第二條，避免重複、遺失或使用錯誤 PC。
4. Scoreboard 按 A/B 各五個執行／寫回位置保存目的暫存器。查詢時優先使用最近的較舊生產者；最新結果尚未準備好就等待，不能使用更舊值。
5. 停頓代表保留指令；氣泡代表沒有有效指令。後方仍可前進時要插入氣泡，否則會重複寫回。
6. 程式原本缺少 B 的控制管線，已補上有效位元、目的暫存器、ALU 控制和寫回。

Part 1 只修改兩個允許的檔案；打包時逐檔與原始壓縮檔比對確認。未修改 Part 1 資料路徑、課程測試或計分器。

## Part 2：兩項最終優化

### 1. 提早判斷分支

在 D 階段以正確旁路資料比較分支条件，較早決定下個取指位址。較舊分支不成立時可以與獨立 ALU 配對；成立時取消較新的 ALU。分支指令仍經過原本管線階段，沒有移除 X0、X1、X2、X3 或 W。

### 2. 乘法結果旁路

原始功能模型的乘法結果在 result1_reg 已經算好，之後還會通過 result2_reg、result3_reg。最終設計從既有暫存結果新增 X1/X2 的轉送接點，使相依指令可以提早讀到結果。單一乘除法單元、所有原本暫存階段及 W 寫回仍然保留；除法／餘數仍依原規則等到 X3。

這項優化讓複數乘法在分支優化版本的 3704 週期基礎上再減少 400 週期，達到 3304。試驗過的佇列版本未能全面改善效能，因此不包含在最終提交包。

## 工作副本與證據

- Windows 工作副本：C:/Users/LSS/Documents/1151/1151_535513-計算機架構/Lab3_Week6/work/lab3
- [最終驗證摘要](C:/Users/LSS/Documents/1151/1151_535513-計算機架構/Lab3_Week6/work/evidence/final-verification.json)
- [提交包逐檔 SHA-256 清單](C:/Users/LSS/Documents/1151/1151_535513-計算機架構/Lab3_Week6/work/evidence/package-manifest.json)
- [Part 1 全部必要測試](C:/Users/LSS/Documents/1151/1151_535513-計算機架構/Lab3_Week6/work/evidence/part1/summary.json)
- [Part 2 全部必要測試](C:/Users/LSS/Documents/1151/1151_535513-計算機架構/Lab3_Week6/work/evidence/part2/summary.json)
- [額外 78 項測試](C:/Users/LSS/Documents/1151/1151_535513-計算機架構/Lab3_Week6/work/evidence/extra-summary.json)

work/validation 內保留額外測試程式與紀錄；work/report-preview 內保留四頁報告預覽；work/create_report.py 可重建報告。這些輔助資料不在程式提交包內。

## 重跑方法（Ubuntu WSL）

工具已存在於 /opt/riscv/bin 與 /opt/iverilog-12/bin。非互動 shell 需要明確設定 PATH。

```bash
export PATH=/opt/riscv/bin:/opt/iverilog-12/bin:$PATH
cd "/mnt/c/Users/LSS/Documents/1151/1151_535513-計算機架構/Lab3_Week6/work/lab3/build"
make -B check-asm-riscvssc_part1
make -B check-asm-rand-riscvssc_part1
make -B run-bmark-riscvssc_part1
make -B run-bmark-rand-riscvssc_part1
make -B check-asm-riscvssc_part2
make -B check-asm-rand-riscvssc_part2
make -B run-bmark-riscvssc_part2
make -B run-bmark-rand-riscvssc_part2
```

若從提交包開始，須先在 tests/build、ubmark/build 各執行 configure、make、convert。可參照報告第 4 頁；Part 2 已完成，**不要再執行 setup.sh 覆蓋它**。

## 上傳前核對

- [x] 學號與兩個檔名正確。
- [x] 報告恰為四頁，已逐頁檢視。
- [x] 壓縮檔根目錄是 lab3，保留原始結構。
- [x] 提交包不含生成的波形、執行檔、測試輸出或測試 build 目錄。
- [x] 提交包從新目錄重新建置與測試，結果與開發版本完全相同。
- [x] Windows 與 WSL 讀取的壓縮檔 SHA-256 相同。
- [ ] 你閱讀報告，確認能說明指令配對、scoreboard 與兩項優化。
- [ ] 你在 E3 分別上傳兩個檔案，核對顯示檔名與「已繳交」狀態。

Lab0 允許 AI 輔助，但要求提交內容反映學生理解。報告已如實揭露工具協助，請閱讀後再自行上傳。

## 檔案指紋

程式包 SHA-256：`8a723c9ad82e5df4740b348631d19e1c818eb5f612cd5cba2910fba4fe358067`

報告 SHA-256：`27028a90c907b98796bea1c2205386e2dc4ea0884c51a93362dbb4464c0b8606`
