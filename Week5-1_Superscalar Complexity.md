
### Week 5 (2026-10-06)課堂逐字稿
#### 教學資源：
- [SD5.pdf](./Lecture/SD5.pdf)
- Prompt：
  - 請說明本教學重點內容及你的看法，最後以250字內總結

## slide：1 -2
<div align="left" >
  <img src="./Lecture/SD5/SD5_page-0001.jpg" width="50%">
</div>

### VLIW（Very Long Instruction Word，超長指令字）
VLIW（Very Long Instruction Word，超長指令字） 是一種利用**指令級平行化（Instruction-Level Parallelism, ILP）**的處理器架構。
<br>其核心思想是：由編譯器負責找出可同時執行的指令，並將多個操作封裝成一個超長指令，讓 CPU 在同一個 Clock Cycle 同時執行。
- 傳統處理器：
  ```
  一般 RISC-V 指令：
    add x1,x2,x3
    sub x4,x5,x6
    mul x7,x8,x9
  CPU 一次取出一條指令：
    Cycle 1 → add
    Cycle 2 → sub
    Cycle 3 → mul
    ``
  ```
- VLIW 處理器：
  ```
  編譯器將可平行執行的指令組合：形成一個超長指令字（Instruction Word）。
    | add | sub | mul |
  執行時：三個功能單元同時工作。
    Cycle 1
    ├─ add
    ├─ sub
    └─ mul
  ```


## slide：2
<div align="left" >
  <img src="./Lecture/SD5/SD5_page-0001.jpg" width="49%">
  <img src="./Lecture/SD5/SD5_page-0002.jpg" width="49%">
</div>


