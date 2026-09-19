# Computer Architecture - Problem Set #1

### 第 1 題：平均 CPI
Compute the Clocks Per Instruction (CPI) of a machine which has an average CPI for ALU operations of 1.1, a CPI for branches/jumps of 3.0, and a hit rate of 60% in the cache. A hit in the cache takes 1 cycle pipelined and a cache miss takes 120 cycles. Assume 22% of instructions are loads, 12% are stores, 20% are branches/jumps and the balance are ALU operations.
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
<br>**知識點與目標：** 
- CPI 是平均每一條指令花幾個 clock cycles。
- 即使 cache miss 只占 40%，但它耗時很高(非常慢)，所以會嚴重拉高總 CPI。

### 第 2 題：比較處理器效能
You are a processor designer and have to make a decision between building a processor which executes at 1GHz and has an average CPI 1.2 and a processor which executes at 2GHz, but has a CPI of 2. Which is better to build and why?
> 你是處理器設計者，要在下列兩種處理器中選擇：處理器 A：時脈 1 GHz，平均 CPI = 1.2，處理器 B：時脈 2 GHz，CPI = 2，哪一個比較好？為什麼？

使用公式：
$$
\(\text{Instruction time}=\frac{\text{CPI}}{\text{Clock rate}}\)
$$
| 處理器 | 計算 | 每條指令時間 |
| --- | --- | --- |
| A | $1.2 / 1\text{ GHz}$ | 1.2 ns |
| B | $2 / 2\text{ GHz}$ | 1.0 ns |

**答案：選擇處理器 B。** 它每條指令平均只需 1.0 ns，比 A 的 1.2 ns 快，約快 20%。

### 第 3 題：RISC-V 資料 Hazard
For the following RISC-V code snippet, identify all of the RAW, WAW, and WAR hazards. Provide a list for each hazard. Hint: remember that you have to check more than just neighboring instructions.
>請找出下列 RISC-V 程式中的所有 RAW、WAW 與 WAR hazard（危險），並分別列出。提示：不要只檢查相鄰指令。
1. add  x1, x2, x3
2. sub  x3, x4, x6
3. mul  x5, x4, x7
4. addi x5, x5, 1
5. sub  x6, x3, x9
6. andi x2, x1, x9
讀寫暫存器整理

| 指令 | 讀取 registers | 寫入 register |
| --- | --- | --- |
| `add x1, x2, x3` | x2、x3 | x1 |
| `sub x3, x4, x6` | x4、x6 | x3 |
| `mul x5, x4, x7` | x4、x7 | x5 |
| `addi x5, x5, 1` | x5 | x5 |
| `sub x6, x3, x9` | x3、x9 | x6 |
| `andi x2, x1, x9` | x1、x9 | x2 |

解答

| 類型 | 指令組合 | Register | 原因 |
| --- | --- | --- | --- |
| RAW | `mul` → `addi` | x5 | 後者讀取前者剛寫入的 x5。 |
| RAW | `sub x3` → `sub x6` | x3 | 後者讀取前者剛寫入的 x3。 |
| RAW | `add x1` → `andi x2` | x1 | 後者讀取前者剛寫入的 x1。 |
| WAW | `mul` → `addi` | x5 | 兩者都寫入 x5。 |
| WAR | `add x1` → `sub x3` | x3 | 前者讀 x3，後者才寫 x3。 |
| WAR | `add x1` → `andi x2` | x2 | 前者讀 x2，後者才寫 x2。 |
| WAR | `sub x3` → `sub x6` | x6 | 前者讀 x6，後者才寫 x6。 |

### 知識點與目標
- **RAW (Read After Write)**：先寫後讀，是真正的資料相依。
- **WAW (Write After Write)**：兩條指令寫同一個 register。
- **WAR (Write After Read)**：先讀後寫同一個 register。
- 解題時，先列出每條指令讀／寫的 register，再檢查所有前後指令組合。















