# 第22AR講 Memory

### 教學資源：
- [11010黃婷婷教授計算機結構_第22AR講 Memory(48:11)](https://www.youtube.com/watch?v=fs6n2Yjt3X4&list=PLpXfHEl2fzl47WOaypHoOWxBIhG42_Vlq&index=31)
- Prompt：
  - 請將本教學內容英/中翻譯比對<br>請說明本slide教學重點內容及你的看法，最後以250字內總結
- 教學內容
  - [Outline](#outline)
  - [Memory Technology](#memory-technology)
  - [Comparisons of Various Technologies](#comparisons-of-various-technologies)

## Outline 
<div align="left" >
  <img src="./Lecture/22AR_Memory-0001.png" width="49%">
</div>

Hierarchy   [ˈhaɪərɑːki]海.而.起    n.等級制度；統治集團；等級體系

教學內容英/中翻譯比對：[[Top]](#教學資源)
  <br>關於記憶體階層（Memory Hierarchy）單元的大綱（Outline），內容主要對應經典教科書《Computer Organization and Design》（David A. Patterson 與 John L. Hennessy 著）的第五章結構。

  投影片中列出的七個核心主題：
  - Memory hierarchy（記憶體階層）：介紹區域性原理（Principle of Locality，包含時間與空間區域性），以及如何利用不同速度、容量與成本的儲存媒體（暫存器、快取、主記憶體、磁碟）打造兼顧大容量與高速度的記憶體系統。
  - The basics of caches（快取記憶體基礎）：探討快取的基本運作機制，包含區塊放置（Direct Mapped、Set Associative、Fully Associative）、位址標籤（Tag）比對、讀取命中/失誤（Hit/Miss）處理，以及寫入策略（Write-Through 與 Write-Back）。
  - Measuring and improving cache performance（量測與改進快取效能）：學習如何計算平均記憶體存取時間（AMAT）與 CPU 停頓時間，並透過調整區塊大小、提高關聯度（Associativity）及導入多層級快取（Multi-level Caches）來降低失誤率與失誤代價（Miss Penalty）。
  - Virtual memory（虛擬記憶體）：說明作業系統與硬體如何協同管理主記憶體與磁碟之間的資料交換，涵蓋分頁（Paging）、分頁表（Page Table）、轉譯後備緩衝區（TLB）以及記憶體保護機制。
  - A common framework for memory hierarchy（記憶體階層的通用框架）：將快取與虛擬記憶體歸納為統一的設計框架，探討「區塊放置、尋找、替換策略（如 LRU）與寫入策略」這四個核心問題，並介紹快取失誤的「3Cs 模型」（Compulsory、Capacity、Conflict）。
  - Using a Finite State Machine to Control a Simple Cache（使用有限狀態機控制簡易快取）：從硬體實作角度出發，示範如何透過有限狀態機（FSM）設計快取控制器（Cache Controller），處理讀寫請求與主記憶體之間的資料傳輸狀態轉換。
  - Parallelism and Memory Hierarchies: Cache Coherence（平行化與記憶體階層：快取一致性）：探討多核心處理器架構下，各核心擁有獨立快取時可能發生的資料不一致問題，以及硬體如何透過偵聽協定（Snooping Protocols，如 Write Invalidate）來維持快取一致性。


## Memory Technology
<div align="left" >
  <img src="./Lecture/22AR_Memory-0002.png" width="49%">
</div>

教學內容英/中翻譯比對：[[Top]](#教學資源)
<br>Memory Technology | 記憶體技術
- Random access: | 隨機存取：
  - Access time same for all locations | 所有記憶體位置的存取時間皆相同
  - SRAM: Static Random Access Memory | SRAM：靜態隨機存取記憶體
    - Low density, high power, expensive, fast | 密度低、功耗高、價格昂貴、速度快
    - Address not divided | 位址不分割（一次輸入完整位址）
    - Use for caches | 用於快取記憶體（Cache）
  - DRAM: Dynamic Random Access Memory | DRAM：動態隨機存取記憶體
    - High density, low power, cheap, slow | 密度高、功耗低、價格便宜、速度慢
    - Dynamic: need to be refreshed regularly | 動態特性：需要定期刷新（Refresh）以維持資料
    - Addresses in 2 halves (memory as a 2D matrix): 位址分為兩半（將記憶體視為二維矩陣）：
      - RAS/CAS (Row/Column Access Strobe) | 列位址選通 / 行位址選通（RAS/CAS）
  - Use for main memory | 用於主記憶體（Main Memory）
- Magnetic disk | 磁碟（傳統硬碟）

教學重點內容：
<br>本頁投影片在建立 記憶體階層（Memory Hierarchy） 的硬體基礎，核心重點如下：
- 隨機存取（Random Access）定義：點出 SRAM 與 DRAM 共同的核心特性。無論資料存放在哪個實體位置，存取延遲（Access Time）都相同（這也是它們與序列存取裝置如磁帶、或受機械尋道影響的磁碟最大的不同）。
- SRAM 與 DRAM 的特性對比：
  - SRAM（靜態）：利用正反器（Flip-Flop）結構儲存，只要供電資料就不會遺失，速度快但電晶體數量多導致密度低、功耗與成本高，因此專門用來打造容量小但極需速度的 快取（Cache）。
  - DRAM（動態）：利用電容儲存電荷，結構極簡因此密度高、成本低，但電容會漏電必須定期刷新（Refresh）；為了減少晶片接腳數，將記憶體排成二維陣列並透過 RAS/CAS 分兩次傳送列與行位址，適合當作大容量的 主記憶體（Main Memory）。
- 非隨機存取對照（Magnetic disk）：在最下方列出磁碟，作為接下來探討「區塊存取、機械延遲與大容量非揮發性儲存」的銜接伏筆。

我的看法與補充
- 完美的「工程權衡（Trade-off）」教材：這張投影片非常精準地解釋了為什麼現代電腦不全部使用最快的 SRAM，也不全部使用最便宜的 DRAM——因為沒有任何單一技術能同時滿足「極速、大容量、低成本」，這正是推動記憶體階層架構誕生的根本原因。
- 從硬體物理連貫到架構設計：投影片中特別點出 DRAM 的 RAS/CAS 位址分割，這在電腦架構中非常重要。它直接解釋了為什麼 DRAM 連續讀取同一列（Row Buffer Hit）會比跨列讀取快上許多，進而影響到記憶體控制器（Memory Controller）的排程演算法與程式的空間局部性（Spatial Locality）優化。

內容總結：
<br>本投影片介紹電腦系統中的核心記憶體技術，重點對比兩種隨機存取記憶體（存取時間不隨位置改變）：<br>SRAM（靜態）無需刷新即可維持資料，具備極高速度但密度低、成本與功耗高，適合用於快取（Cache）；<br>DRAM（動態）結構簡單、密度高且便宜，但需定期刷新，並透過 RAS/CAS 將位址分為兩半以二維矩陣存取，適合做為主記憶體。<br>最後帶出磁碟做為大容量儲存的銜接。整體清楚展現了速度、容量與成本間的硬體權衡，為記憶體階層架構奠定基礎。

## Comparisons of Various Technologies
<div align="left" >
  <img src="./Lecture/22AR_Memory-0003.png" width="49%">
</div>

教學內容英/中翻譯比對：
<br>Comparisons of Various Technologies | 各種記憶體技術之比較
- Memory technology / Typical access time / $ per GB in 2008 <br> 記憶體技術 / 典型存取時間 / 2008年每 GB 價格（美元）
- SRAM | 0.5 – 2.5 ns | $2000 – $5,000 <br>SRAM（靜態隨機存取記憶體） | 0.5 – 2.5 奈秒 | $2,000 – $5,000 美元
- DRAM | 50 – 70 ns | $20 – $75 <br>DRAM（動態隨機存取記憶體） | 50 – 70 奈秒 | $20 – $75 美元
- Magnetic disk | 5,000,000 – 20,000,000 ns | $0.20 – $2<br>磁碟（傳統硬碟） | 5,000,000 – 20,000,000 奈秒（即 5–20 毫秒） | $0.20 – $2 美元
- Ideal memory | 理想的記憶體（目標）
  - Access time of SRAM | 擁有像 SRAM 一樣的極快存取速度
  - Capacity and cost/GB of disk | 擁有像磁碟一樣的大容量與低廉的每 GB 成本

教學重點內容：
<br>「理想記憶體（Ideal Memory）」的矛盾：點出系統設計者的終極夢想。既要 SRAM 的速度，又要磁碟的容量與價格。由於單一物理元件無法同時達成這兩點，**因此必須透過記憶體階層（Memory Hierarchy）搭配局部性原理（Principle of Locality），用架構設計來「模擬」出理想記憶體的假象**。

我的看法與時代演進補充
- 極具說服力的量化教學：把磁碟的存取時間刻意寫成 5,000,000 – 20,000,000 ns 而不是 5 – 20 ms，是教學上非常高明的設計，統一用「奈秒（ns）」為單位，能讓學生在視覺上直觀感受到 CPU 等待硬碟讀取時那種「天文數字」般的漫長停頓。
- 填補鴻溝的現代技術（Flash / SSD）：這份投影片採用 2008 年的經典教材數據（出自 Hennessy & Patterson《計算機結構》），當時 DRAM 與磁碟之間存在著高達 10 萬倍的「存取時間鴻溝（Access Time Gap）」。在現代電腦架構中，NAND Flash（固態硬碟 SSD） 已經強勢填補了這個中間地帶——其存取時間落在數萬奈秒（數十微秒）等級，每 GB 成本也大幅下降，成為現代儲存系統不可或缺的一層。

內容總結：
<br>本投影片透過具體數據量化比較 SRAM、DRAM 與傳統磁碟的效能與成本。三者在存取時間與每 GB 價格上呈現劇烈的反向數量級落差：SRAM 極快（約 1 ns）但極貴；DRAM 居中（50–70 ns）；磁碟雖最便宜，但存取延遲高達數百萬奈秒，與 DRAM 相差十萬倍。為實現「兼具 SRAM 速度與磁碟大容量、低成本」的理想記憶體目標，電腦架構師必須利用局部性原理，將這些不同特性的元件整合成記憶體階層，以發揮最大系統效益。

## Processor Memory Latency Gap
<div align="left" >
  <img src="./Lecture/22AR_Memory-0004.png" width="49%">
</div>

教學內容英/中翻譯比對：
<br>Processor Memory Latency Gap | 處理器與記憶體的延遲鴻溝
- Performance (Y-axis: 1, 10, 100, 1000)<br>效能（縱軸為對數刻度：1, 10, 100, 1000）
- Year (X-axis: 1980 – 2000)<br>年份（橫軸：1980 年至 2000 年）
- Moore's Law | 摩爾定律
- Proc: 60%/yr. (2X/1.5 yr)<br>處理器效能：每年成長 60%（每 1.5 年翻倍）
- DRAM: 9%/yr. (2X/10 yrs)<br>DRAM 效能（存取速度）：每年僅成長 9%（每 10 年才翻倍）
- Processor-memory performance gap: (grows 50% / year)<br>處理器與記憶體的效能差距：（每年擴大 50%）

教學重點內容：
<br>這張圖表是電腦架構領域最經典的「記憶體牆（Memory Wall）」起源圖，核心重點如下：
- 不對等的演進速度（對數座標的視覺衝擊）：
  - 縱軸採用對數刻度（Logarithmic Scale）。自 1980 年起算，處理器（Proc）受惠於摩爾定律與微架構創新，效能以每年 60%（約每 1.5 年翻倍）的驚人斜率攀升，20 年間成長了近 1000 倍。
  - 反觀 DRAM 的製造工藝雖然也受惠於摩爾定律，但產業研發重心放在「增加容量密度與降低成本」，而非「降低存取延遲」，導致其速度每年僅進步約 9%（需 10 年才翻倍）。
- 每年擴大 50% 的效能鴻溝：<br>兩條曲線的垂直距離代表 CPU 等待記憶體讀取資料的時間成本。由於這道鴻溝以每年 50% 的速度急劇擴大，若沒有架構上的補救措施，再快的 CPU 也會因為「等不到資料」而處於閒置狀態（Memory Stall）。

我的看法與現代技術演進補充：
- 「記憶體階層」誕生的歷史必然性：在 1980 年代初期（圖表最左側），CPU 時脈與 DRAM 存取時間相當接近，當時的電腦幾乎不需要快取（Cache）。這張圖完美解釋了為什麼到了 1990 年代後，多層級快取（L1/L2/L3 Cache）、亂序執行（Out-of-Order Execution）與硬體預取（Prefetching）會成為現代 CPU 的標準配備——它們全都是為了掩蓋這道致命的延遲鴻溝。
- 2026 年的現況延伸（從「延遲牆」走向「頻寬牆」與 AI 瓶頸）：2004 年後單核時脈受限於功耗牆（Power Wall）而趨緩，處理器轉向多核心與 GPU/AI 加速器發展。到了現代大型語言模型（LLM）與高效能運算時代，這道鴻溝不僅依然存在，更演變為嚴峻的記憶體頻寬瓶頸，直接催生了 HBM（高頻寬記憶體）、3D 晶片堆疊（如教材中提到的 2.5D/3D Die Stacking）以及存算一體（Processing-in-Memory, PIM）等前沿技術。

內容總結：
<br>本投影片以 1980 至 2000 年的對數圖表，揭示著名的處理器與記憶體延遲鴻溝（記憶體牆）。受惠於摩爾定律，處理器效能以每年 60%（1.5 年翻倍）的速度飛躍成長；然而 DRAM 研發偏重容量而非速度，存取效能每年僅提升 9%（10 年翻倍）。兩者差距以每年 50% 的速度劇烈擴大，使 CPU 頻繁陷入等待資料的閒置狀態。這項物理與產業趨勢迫使電腦架構師必須導入多層級快取與平行存取等技術，來彌補主記憶體速度跟不上運算核心的困境。

## Solution: Memory Hierarchy
<div align="left" >
  <img src="./Lecture/22AR_Memory-0005.png" width="49%">
</div>

教學內容英/中翻譯比對：
<br>Solution: Memory Hierarchy | 解決方案：記憶體階層
- An Illusion of a large, fast, cheap memory | 營造「大容量、高速度、低成本記憶體」的假象
  - Fact: Large memories slow, fast memories small<br>物理現實：大容量的記憶體速度慢，高速度的記憶體容量小
  - How to achieve: hierarchy, parallelism<br>實現方式：階層化（Hierarchy）與平行化（Parallelism）
- An expanded view of memory system: | 記憶體系統的展開視圖：
  - Processor (Control / Datapath) | 處理器（控制單元 / 資料路徑）
    <br>Memory (從左側處理器內部向右展開至外部多層方塊)<br>記憶體（由內而外依序為：暫存器、快取、主記憶體、輔助儲存裝置）
  - Speed: Fastest $\longrightarrow$ Slowest | 速度：最快（最左側靠近運算單元） $\longrightarrow$ 最慢（最右側）
  - Size: Smallest $\longrightarrow$ Biggest | 容量：最小 $\longrightarrow$ 最大
  - Cost: Highest $\longrightarrow$ Lowest | 單位成本：最高 $\longrightarrow$ 最低

教學重點內容：
<br>這張投影片正式提出了電腦架構中最核心的設計哲學，核心重點如下：
- 「假象（Illusion）」的系統設計藝術：面對「大容量必慢、高速度必小且貴」的物理鐵律，架構師不試圖尋找單一完美的儲存元件，而是透過記憶體階層（Memory Hierarchy）與平行化（Parallelism），讓程式設計師與作業系統感覺彷彿擁有一個「既像暫存器/快取一樣快、又像硬碟一樣大且便宜」的理想記憶體。
- 由內而外的系統展開視圖：圖示清楚描繪了記憶體與處理器（Processor）的空間位置關係。最左側緊貼 Datapath（資料路徑） 的是容量最小、速度最快、單位成本最高的儲存層（暫存器與 L1/L2 Cache）；越往右側遠離處理器核心，容量越龐大、成本越低廉，但存取速度也隨之遞減（L3 Cache $\rightarrow$ 主記憶體 DRAM $\rightarrow$ SSD/磁碟）。 

我的看法與教材連結：
- 「階層」背後的隱形推手——局部性原理（Principle of Locality）：投影片點出了「hierarchy（階層）」這個架構，而這個架構之所以能成功騙過使用者、創造出「高速且大容量」的假象，全賴軟體程式執行時具備的時間局部性（Temporal Locality）與空間局部性（Spatial Locality）（正如經典教科書《Computer Architecture》第 2.1 節所述）。因為 CPU 大多數時間只會反覆存取一小塊熱點資料，所以只要把這小塊資料留在最左側的小容量高速記憶體中，整體系統就能跑出接近最快層級的速度。
- 平行化（Parallelism）的關鍵角色：投影片中特別與 hierarchy 並列提及的 parallelism 非常精闢——包含多通道記憶體（Multi-channel DRAM）、交錯記憶體（Memory Interleaving）以及快取與主記憶體之間的區塊平行傳輸（Block Transfer），這些平行化設計大幅提升了資料搬運的頻寬，是現代多核心 CPU 與 GPU 餵飽運算單元的關鍵。

內容總結：
<br>面對「大容量記憶體速度慢、高速度記憶體容量小」的物理現實，本投影片提出記憶體階層（Memory Hierarchy）作為解決方案。系統透過階層化與平行化設計，在處理器資料路徑（Datapath）旁配置最小、最快、最貴的記憶體，並向外逐層擴展至容量最大、速度最慢、成本最低的儲存裝置。藉由將常用資料保留在靠近核心的高速層級，記憶體階層成功為系統營造出「同時具備大容量、高速度與低成本」的理想記憶體假象。

#### 說明L1/L2/L3 Cache
在現代 CPU 中，Cache（快取記憶體） 是位於 CPU 與主記憶體（DRAM）之間 的高速記憶體，用來減少 CPU 等待資料的時間。<br>由於 CPU 的運算速度遠快於 DRAM，如果每次都直接存取主記憶體，CPU 大部分時間都在等待資料，因此發展出多層快取架構。

L1、L2、L3 Cache 是 CPU 與 DRAM 之間的多層高速緩衝區，其中 L1 最快但最小，L3 最大但較慢；其目的是提高 Cache Hit Rate，減少存取 DRAM 的延遲，進而提升整體系統效能。

為何需要 L1/L2/L3 Cache？
CPU Register ↓ L1 Cache ↓ L2 Cache ↓ L3 Cache ↓ DRAM ↓ SSD
越往下：容量越大、價格越便宜、存取速度越慢
```
          CPU Core
              │
        ┌─────┴─────┐
        │  L1 Cache │
        └─────┬─────┘
              │
        ┌─────┴─────┐
        │  L2 Cache │
        └─────┬─────┘
              │
        ┌─────┴─────┐
        │  L3 Cache │
        └─────┬─────┘
              │
           DRAM
```
- L1 Cache：特性
  - 最接近 CPU、速度最快、容量最小：32KB ~ 128KB
  - 每個核心通常有自己的 L1：互不共享。
    - Core 0 → L1
    - Core 1 → L1
    - Core 2 → L1
- L2 Cache 特性：
  - 介於：L1 - L2 -L3 之間。容量較大：256KB ~ 2MB

## Memory Hierarchy: Principle
<div align="left" >
  <img src="./Lecture/22AR_Memory-0006.png" width="49%"> (16:13)
</div>

Principle [ˈprɪnsəpl]坤.死.坡    n.原則；行為準則；原理

教學內容英/中翻譯比對：
<br>Memory Hierarchy: Principle | 記憶體階層：運作原理
- At any given time, data is copied between only two adjacent levels:<br>在任何給定時間，資料只會在「相鄰的兩個層級」之間進行複製傳輸：
  - Upper level: the one closer to the processor | 上層（Upper level）： 較靠近處理器的那一層
    - Smaller, faster, uses more expensive technology | 容量較小、速度較快、採用成本較昂貴的技術
  - Lower level: the one away from the processor | 下層（Lower level）： 較遠離處理器的那一層
    - Bigger, slower, uses less expensive technology | 容量較大、速度較慢、採用成本較低廉的技術
- Block: basic unit of information transfer | 區塊（Block）：資訊傳輸的基本單位
  - Minimum unit of information that can either be present or not present in a level of the hierarchy<br>在記憶體階層的某一層中，資訊「存在（Hit）」或「不存在（Miss）」的最小單位

Diagram Labels | 圖示標註
- To Processor / From Processor | 傳送至處理器 / 來自處理器
- Upper Level Memory (Block X) / Lower Level Memory (Block Y) | 上層記憶體（區塊 X） / 下層記憶體（區塊 Y）

教學重點內容：
<br>這張投影片定義了記憶體階層在實際運作時的標準抽象模型與核心術語，重點如下：
- 相鄰層級傳輸原則（Adjacent-Level Transfer）：無論系統共有多少層（如暫存器、L1/L2/L3 Cache、主記憶體、SSD/磁碟），資料搬運永遠只發生在「緊鄰的兩層」之間（例如 L2 與 L1 之間，或主記憶體與 L3 之間），不會跨層直接傳輸，這簡化了硬體控制與資料一致性的設計。
- 上層（Upper）與下層（Lower）的相對概念：這是一組相對的稱呼（例如對主記憶體而言，L3 Cache 是上層；但對 L2 Cache 而言，L3 Cache 則是下層）。越往「上層」越靠近 CPU，速度越快但容量小且昂貴；越往「下層」則相反。
- 區塊（Block / Cache Line）的核心定義：資料不是以單一「位元組（Byte）」為單位在層級間搬運，而是打包成固定大小的區塊（Block）。CPU 每次只向最上層請求資料，若該區塊存在即為 Hit（命中）；若不存在則為 Miss（失誤），此時必須從下層把整個區塊複製上來。

我的看法與系統設計連結：
- 「Block」是空間局部性（Spatial Locality）的硬體落實：為什麼每次 Miss 時要大費周章搬運整個 Block（現代 CPU 常見為 64 Bytes）而不是只拿 CPU 當下要的那 4 Bytes？因為這能順便把相鄰位址的資料一起帶進上層，只要程式接下來循序讀取陣列或指令，就能直接 Hit。這讓一次高昂的跨層讀取延遲，分攤（Amortize）到多次後續存取上。
- Block 大小的雙面刃（Trade-off）：在系統設計中，Block 並不是越大越好。過大的 Block 雖然能提升空間局部性的命中率，但會增加單次搬運的傳輸時間（Miss Penalty），同時也會減少上層記憶體能容納的總區塊數，反而可能引發更頻繁的區塊替換（Conflict / Capacity Miss）。

內容總結：
<br>本投影片闡述記憶體階層的運作原理與核心定義。系統運作時，資料永遠只在相鄰的兩個層級間複製傳輸：靠近處理器的上層容量小、速度快且昂貴；遠離處理器的下層則容量大、速度慢且便宜。階層間資訊傳輸與判斷存在（Hit）或不存在（Miss）的最小基本單位稱為區塊（Block）。透過以區塊為單位的相鄰層級搬運機制，硬體能有效利用空間局部性，將相鄰資料預先載入高速上層，藉此分攤下層記憶體的存取延遲並提升整體效能。

## Why Hierarchy Works?
<div align="left" >
  <img src="./Lecture/22AR_Memory-0007.png" width="49%"> (18:51)
</div>

教學內容英/中翻譯比對：
<br>Why Hierarchy Works? | 為什麼記憶體階層能夠有效運作？
- Principle of Locality: | 局部性原理（Principle of Locality）：
  - Program access a relatively small portion of the address space at any instant of time <br>程式在任何一個瞬間，只會存取整個記憶體位址空間中相對很小的一部分
  - 90/10 rule: 10% of code executed 90% of time <br>90/10 法則：程式中 10% 的程式碼佔據了 90% 的執行時間
- Two types of locality: | 兩種局部性：
  - Temporal locality: if an item is referenced, it will tend to be referenced again soon <br>時間局部性： 如果某個資料項目被存取過，它在不久的將來很可能再次被存取
  - Spatial locality: if an item is referenced, items whose addresses are close by tend to be referenced soon<br>空間局部性： 如果某個資料項目被存取過，位址與它相近的其他項目在不久的將來也很可能被存取

圖表標註 (Graph Labels):
- Probability of reference (Y-axis) | 存取機率（縱軸）
- address space: $0$ to $2^n - 1$ (X-axis) | 記憶體位址空間：$0$ 到 $2^n - 1$（橫軸）

教學重點內容
<br>這張投影片揭示了記憶體階層之所以能成功創造「高速且大容量」假象的軟體行為基石，核心重點如下：
- 局部性原理與 90/10 法則：程式並非均勻隨機地存取所有記憶體，而是在特定時間內高度集中在少數熱點區域（即 10% 的核心程式碼如迴圈，消耗了 90% 的執行時間）。底部的「存取機率 vs. 位址空間」分布圖，形象化地展示了在龐大的 $0 \sim 2^n-1$ 位址空間中，只有少數幾個窄區間擁有極高的存取機率。
- 時間局部性（Temporal Locality）與空間局部性（Spatial Locality）：
  - 時間局部性（例如迴圈計數器、重複呼叫的函式）解釋了「為什麼把剛用過的資料留在上層快取（Cache）是有價值的」。
  - 空間局部性（例如陣列的連續元素、循序執行的指令）解釋了「為什麼上一張投影片要以整個 Block（區塊） 為單位把相鄰資料一併搬入上層」。

我的看法與系統設計連結：
- 「軟體特性」決定「硬體架構」的典範：記憶體階層本身並不具備任何魔法，如果一個程式完全違反局部性原理（例如在數 GB 的陣列中做完全隨機的跳躍讀取），快取命中率（Hit Rate）會趨近於零，整個系統效能反而會因為頻繁的 Cache Miss 搬運而暴跌。這提醒了工程師：寫出「對快取友善（Cache-Friendly）」的程式碼（如 Row-major 走訪二維陣列）與升級硬體同樣重要。
- 從快取一路延伸至虛擬記憶體（Virtual Memory）：局部性原理不僅支撐了硬體快取的運作，也同樣是作業系統中虛擬記憶體分頁（Paging）與 TLB（轉譯後備緩衝區） 能夠避免每次記憶體存取都多花一倍時間查表的核心理論基礎（如教材第 2.4 節與附錄 B 所述）。

內容總結：
<br>本投影片解釋記憶體階層得以奏效的核心理論——局部性原理。根據 90/10 法則，程式在任何時間點僅集中存取極小範圍的位址空間（約 10% 的程式碼佔 90% 執行時間）。局部性分為兩種：時間局部性（剛被存取的資料很快會再用，支撐將資料保留在快取的設計）與空間局部性（相鄰位址的資料很快會被存取，支撐以「區塊」為單位預先搬運的機制）。正因程式具備這項行為規律，小容量的高速快取才能滿足絕大多數的存取需求。





















