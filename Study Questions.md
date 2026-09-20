
## 第 1 題：
Why did the end of Dennard scaling change how architects improve performance?
>為什麼 Dennard 縮放比例定律的終結改變了架構師提升效能的方式？
- Dennard 縮放定律的失效：過往當晶體管尺寸縮小時，功率密度保持不變，因此晶片可以在不大幅增加功耗與發熱的前提下，獲得更高的主頻（Clock Frequency）。但在 2000 年代中期，由於漏電流（Leakage Current）與靜態功耗（Static Power）急劇上升，Dennard 縮放定律終止，晶片迎來「功率牆（Power Wall）」。
- 效能提升策略的根本轉變：
  - 從單核主頻轉向平行處理：無法繼續透過提升時脈頻率來換取效能，架構師轉而發展指令級平行（ILP）、多核心（Multicore） 與 執行緒級平行（TLP）。
  - 從通用算力轉向能源效率（Energy Efficiency）：架構設計的核心指標從單純追求「最高峰值效能」轉變為「每瓦效能（Performance per Watt）」。

## 第 2 題：
How do memory bandwidth and capacity each limit the benefits of faster processors?
> 記憶體頻寬與容量各自如何限制更快處理器帶來的優勢？
- 記憶體頻寬（Memory Bandwidth）的限制：
  - 記憶體牆（Memory Wall）：當 CPU/GPU 的算力大幅提升時，若記憶體單位時間內能傳送的資料量（BW）不足，處理器的大量算力單元將長時間處於等待資料的飢餓狀態（Stall）。
  - Roofline 模型中的 Memory-Bound 區塊：對於 Operational Intensity（算術強度）較低的演算法（如大矩陣向量乘法），即便算力再快，整體效能上限仍完全受限於頻寬。
- 記憶體容量（Memory Capacity）的限制：
  - 工作集（Working Set）溢出：<br>當處理的資料集（如大型語言模型 LLM 參數或巨型資料庫）超過主記憶體容量時，系統必須將資料移至速度極慢的外存（SSD/NVMe）或透過網路傳輸，導致嚴重的 I/O 懲罰。
  - 限制模型的擴展性：<br>在 AI 訓練與推理中，容量直接決定了能一次載入多大的模型或批量（Batch size）。

## 第 3 題：
Why can domain-specific architectures achieve higher energy efficiency, and what do they sacrifice?
> 為什麼特定領域架構能實現更高的能源效率？它們犧牲了什麼？
- 實現高能源效率（Performance/Watt）的原因：
  - 剔除通用控制開銷：<br>DSA（如 Google TPU、Nvidia Tensor Core）擺脫了傳統 CPU 複雜的指令解碼、動態分支預測與亂序執行（Out-of-Order）邏輯，將大部分晶片面積直接用於專用算力陣列（如 Systolic Array）。
  - 記憶體存取優化：利用 Domain-Specific 領域特有的資料流（Dataflow），設計專屬的 Scratchpad Memory 或 SRAM 緩衝區，減少對高耗能 DRAM 的存取頻率。
  - 精簡資料精度：使用針對特定領域優化的低精度算術單元（如 FP16、BF16、INT8/INT4）。
- 所犧牲的權衡（Tradeoffs）：<br>犧牲通用性（General Purpose）與靈活性：DSA 僅對特定數學運算（如矩陣乘法、卷積）高效；一旦演算法架構發生重大創新（如從 CNN 轉向 Transformer，或未來的全新 AI 演算法），專用晶片可能無法支援或效率大打折扣。

## 第 4 題：
What does the Roofline model's ridge point represent, and how does it shift if peak compute throughput doubles while memory bandwidth stays unchanged?
> Roofline 模型的折點代表什麼？如果峰值計算吞吐量翻倍但記憶體頻寬保持不變，折點會如何移動？
- 折點（Ridge Point）的代表意義：
  - 折點是 Roofline 模型中 「記憶體頻寬限制區（Memory-Bound）」 與 「計算能力限制區（Compute-Bound）」 的交界點。
  - 它代表了讓處理器達到最大峰值算力（Peak Performance）所需的最低算術強度（Operational Intensity, FLOPs/Byte）。
- 折點移動方向：
  - 折點公式：
    ```
                  Peak Performance
    Ridge Point = ------------------------------------
                  Memory Bandwidth
    ```
  - 若峰值計算吞吐量（Peak Compute Throughput）翻倍，而記憶體頻寬（Memory Bandwidth）保持不變，則折點需要的算術強度會提升為原來的 2 倍（折點在 Roofline 圖表中會向右且向上移動）。
  - 架構意涵：這意味著應用程式必須在每次記憶體存取中執行兩倍的計算量，才能完全發揮升級後的處理器算力；否則大部分應用會落入 Memory-Bound 區域。

## 第 5 題：
What problems do chiplets and HBM address, and what is one tradeoff or limitation of each?
> 小晶片 Chiplets 與高頻寬記憶體 HBM 解決了什麼問題？它們各自的權衡或限制是什麼？
- HBM（High Bandwidth Memory，高頻寬記憶體）：
  - 解決的問題：透過 3D 堆疊 DRAM 晶片與 2.5D 中介層（Interposer）微凸塊連接，提供遠高於傳統 DDR/GDDR 的介面位元寬（如 1024-bit），徹底緩解「記憶體頻寬牆」。
  - 權衡與限制（Tradeoff / Limitation）：極高成本與封裝複雜度。HBM 製造與先進封裝（如 CoWoS）成本非常昂貴，且相較於傳統插槽式 DRAM，HBM 的最大容量擴充性較為受限。
- Chiplets（小晶片 / 模塊化晶片）：
  - 解決的問題：打破傳統光罩面積限制（Reticle Limit），將大型單片晶片（Monolithic Die）拆分為多個小 Chiplet。這能大幅提高晶圓良率（Yield）、降低製造成本，並允許將不同製程節點 （如 3nm 計算核心 + 6nm I/O 介面）整合在一起。
  - 權衡與限制（Tradeoff / Limitation）：跨晶片連線的延遲與功耗開銷。Chiplet 之間的 Die-to-Die 互連介面（如 UCIe）會帶來額外的傳輸延遲（Latency）與動態功耗，且對基板與先進封裝工藝有極高要求。












