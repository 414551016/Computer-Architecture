# Computer Architecture - Problem Set #1

### 第 1 題：平均 CPI
>Compute the Clocks Per Instruction (CPI) of a machine which has an average CPI for ALU operations of 1.1, a CPI for branches/jumps of 3.0, and a hit rate of 60% in the cache. A hit in the cache takes 1 cycle pipelined and a cache miss takes 120 cycles. Assume 22% of instructions are loads, 12% are stores, 20% are branches/jumps and the balance are ALU operations.
><br>計算一台機器的平均每指令時脈週期數（CPI）。ALU 運算的平均 CPI 是 1.1；branch/jump 的 CPI 是 3.0；cache 命中率是 60%。Cache hit 需要 1 個 cycle，cache miss 需要 120 個 cycles。假設指令中 Load 占 22%、Store 占 12%、Branch/Jump 占 20%，其餘皆為 ALU 指令。

答案與步驟
- ALU 比例：
  ```
  1 - 0.22 - 0.12 - 0.20 = 0.46
  ```
- Load/Store 的平均 cache 存取成本：
  ```
  0.6(1) + 0.4(120) = 48.6
  ```
- 整體 CPI：
  ```
  0.46(1.1)+0.20(3.0)+(0.22+0.12)(48.6)
  =0.506 + 0.6 + 16.524
  答：平均CPI = 17.63
  ```
<br>**知識點與目標：** CPI 是平均每一條指令花幾個 clock cycles。即使 cache miss 只占 40%，但它非常慢，所以會嚴重拉高總 CPI。
