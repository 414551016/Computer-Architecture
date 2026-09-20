
### Week 1 課堂逐字稿
#### slide：1
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0001.jpg" width="50%">
</div>

Computer Architecture = 計算機架構
<br>這門課並不是教如何寫程式，而是教：「電腦到底如何執行程式？」從軟體一路往下看到硬體，是資工系的重要核心課程。

#### slide：2
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0002.jpg" width="50%">
</div>

Agenda（課程大綱）
- What is Computer Architecture?
  >什麼是計算機架構？
- Course Logistics
  >課程規則與安排

#### slide：3 What is Computer Architecture?
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0003.jpg" width="50%">
</div>

What is Computer Architecture?（什麼是計算機架構？）
- Computer architecture is the design of abstraction and implementation layers that allow applications to execute efficiently.
  >計算機架構是在應用程式與硬體技術之間建立多層次抽象與實作機制，使程式能有效率地執行。
- 重點：
  - Application（應用）
  - Physics/Technology（物理技術）
  <br>中間需要許多層來連接。

#### slide：4 The Computer Systems Stack（電腦系統層級架構）
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0004.jpg" width="50%">
</div>

層級：
|英文	|中文|
|--|--|
|Application  |應用  |
|Algorithm	|演算法|
|Programming Language	|程式語言|
|Operating System/Virtual Machines	|作業系統|
|Compiler	|編譯器|
|Instruction Set Architecture (ISA)	|指令集架構|
|Microarchitecture	|微架構|
|Register-Transfer Level (RTL)	|暫存器傳輸層|
|Gate Level	|邏輯閘|
|Circuit	|電路|
|Device	|元件|
|Physics / Technology|物理技術|

**考試常問：ISA、Microarchitecture、RTL 差在哪裡？**
<br>ISA（指令集架構）、Microarchitecture（微架構） 與 RTL（暫存器傳輸級） 是電腦系統疊層（Computer Systems Stack）中硬體與軟體交界處的三個不同抽象層次：
|階層  |定義與核心概念  |角色與責任  |範例|
|--|--|--|--|
|ISA(Instruction Set Architecture)  |軟硬體的介面與契約定義處理器能理解的指令集、暫存器數量、記憶體位址模式等規格。   |規範「處理器應該做什麼（What）」，使軟體/編譯器能編譯出可執行的程式碼。   |x86, ARM, RISC-V|
|Microarchitecture  |硬體的設計與組織實現 ISA 所規範功能的硬體架構設計概念（如管線化、快取階層、分支預測）。  |決定「硬體要如何實現（How）ISA」，直接影響 CPU 的效能與功耗。|Intel Alder Lake, Apple M1/M2, Cortex-A78|
|RTL(Register-Transfer Level)  |硬體的程式碼實現用硬體描述語言寫出資料如何在暫存器與組合邏輯間傳輸的詳細邏輯。   |將微架構設計轉化為「可被合成與晶片製造的程式碼」。|Verilog, SystemVerilog, VHDL 代码|

階層關係與具體範例
<br>以運算 a = b + c 為例：
- ISA：編譯器將其轉譯為 ISA 規範的組合語言指令（如 RISC-V 的 add x4, x2, x3）。ISA 規定了 add 指令格式與操作數位置。
- Microarchitecture：設計師規劃這條 add 指令要在哪一個流水線（Pipeline）階段執行、是否需要亂序執行（Out-of-order execution）、如何從快取（Cache）預取資料。
- RTL：工程師編寫具體的 Verilog/VHDL 程式碼，例如定義加法器電路 assign x4 = x2 + x3; 以及暫存器觸發時脈（Clock）的邏輯。

簡單來說：ISA 是軟硬體溝通的「語言規範」，Microarchitecture 是 CPU 的「藍圖設計」，而 RTL 則是把藍圖寫成「具體的電路程式碼」。

#### slide：5 The Computer Systems Stack（電腦系統層級架構）
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0005.jpg" width="50%">
</div>

Compiler、OS、ISA（編譯器把 C 轉為組合語言）
- Compiler（編譯器把 C 轉為組合語言）
  <br>例如：a = b + c; 變成：add x1, x2, x3
- ISA
  <br>RISC-V 指令：add、addi、lw、sw
- OS
  <br>Linux Windows macOS 負責管理硬體。

**總結**：
<br>這張告訴你：C語言 → Compiler → RISC-V 指令 → CPU 執行 之後學 RISC-V 時會一直看到。

#### slide：6 The Computer Systems Stack
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0006.jpg" width="50%">
</div>

低階硬體世界
- How data flows through system.
  <br>資料如何在硬體內部流動。
  ```
  從下到上
  Physics ↓ Devices ↓ Circuits ↓ Logic Gates ↓ RTL
  ```

看法：這是數位電路課與計算機架構課的連結。
```
AND Gate ↓ ALU ↓ CPU
```

#### slide：7 This Course
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0007.jpg" width="50%">
</div>

- 本課程主要聚焦在：
  - ISA
  - Microarchitecture
  - RTL

表示你不會深入：半導體製程、電晶體設計，而是專注於 CPU 設計。

#### slide：8 Architecture is Constantly Changing（架構持續演進）
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0008.jpg" width="50%">
</div>

驅動因素
- Application Requirements
  <br>應用需求：例如：AI、Gaming、Cloud
- Technology Constraints

我的看法：這張是研究領域的核心思想：需求推動架構、架構推動科技、科技再推動應用，三者互相影響。

本教學頁面的重點在於說明電腦架構（Computer Architecture）如何受到應用需求與技術限制的雙向推動而持續演進：
- 電腦系統疊層（The Computer Systems Stack）
  <br>圖表左側展示了從最上層的軟體應用到最底層的物理技術所構成的抽象層級：
  - 軟體/應用層：Application → Algorithm → Programming Language → OS / Virtual Machines → Compiler。
  - 架構/介面層：Instruction Set Architecture (ISA) → Microarchitecture → Register-Transfer Level (RTL)。
  - 硬體/物理層：Gate Level → Circuits → Devices → Physics / Technology。
- 架構變革的兩大核心推動力
  <br>圖表右側指出推動電腦架構變化的兩大方向（即上下兩個箭頭）：
  - 由上而下的驅動力 —— 應用需求（Application Requirements）
    - 引導架構改進：新的應用需求（如 AI、大數據、遊戲）會驅動並建議如何改進電腦架構。
    - 提供研發資金：成功的應用帶來商業收益，進而資金回流用於支援新硬體與架構的研發。
  - 由下而上的限制與突破 —— 技術限制（Technology Constraints）
    - 限制執行效率：物理與半導體技術的極限（如功耗、散熱、製程）會限制哪些設計能夠被高效實現。
    - 開創新架構可能：新技術的突破（如新材料、新製程）能讓過去無法實現的新架構變為可能。
- 架構的回饋機制（Feedback Mechanism）
  <br>電腦架構位於中央樞紐位置，能夠提供回饋資訊（Provide feedback），進一步引導上層應用發展以及下層技術研究的方向。

#### slide：9-10 Computers Then
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0009.jpg" width="48%">
  <img src="./Lecture/SD1/SD1_page-0010.jpg" width="48%">
</div>

過去的電腦：IBM 650
<br>特色：
- 早期大型電腦
- 體積巨大
- 成本昂貴

#### slide：11 Computers Now
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0011.jpg" width="50%">
</div>

現代電腦類型：
- Personal（個人電腦）
- Autonomous（自動駕駛）
- Embodied（機器人）
- Spatial（空間運算）
- AI Factory（AI資料中心）

我的看法：AI 已成為主流運算需求。未來許多架構設計都圍繞 AI。

#### slide：12 Moore's Law（摩爾定律）
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0012.jpg" width="50%">
</div>

#### slide：13-14 Sequential Processor Performance
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0013.jpg" width="48%">
  <img src="./Lecture/SD1/SD1_page-0014.jpg" width="48%">
</div>

#### slide：15 Amdahl's Law（阿姆達爾定律）
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0015.jpg" width="50%">
</div>

本教學頁面討論的核心主題為阿姆達爾定律（Amdahl's Law）與平行化的效能極限。以下為教學重點內容整理、個人的觀點評析與總結：
- Speedup（加速比）定義：
  ```
                    未改進時執行整個任務的時間
  Speedup（加速比）= ------------------------------------
                    使用改進技術後執行整個任務的時間

  指標用於量化「加入某種硬體優化或平行處理器後，系統整體變快了多少倍」。
  ```
- 可平行化比例（Parallel Portion）對加速比的限制：
  <br>圖表展現了在不同「可平行化比例」（$50\%, 75\%, 90\%, 95\%$）之下，增加處理器數量（Number of Processors）對整體加速比的影響：
  - 邊際效應遞減：不論處理器增加到幾千甚至上萬個，加速比最終都會趨於平緩並達到上限。
  - 串行瓶頸（Serial Bottleneck）：整體加速比的最大上限取決於無法被平行化的串行部分（1 - Parallel Portion）。
    - 若可平行化比例為 50%，無論放再多處理器，加速比極限就是 2 倍。
    - 若可平行化比例提升至 95%，理論加速比極限可達 20 倍。
- 對此定律的看法：
  - 指出硬體堆疊的盲點：Amdahl's Law 揭示了「暴力增加 CPU 核心數」無法無限制提升效能的現實，硬體盲目堆疊只會帶來嚴重的資源浪費與功耗上升。
  - 強調軟硬體協同設計（Co-design）：若要讓更多核心發揮價值，關鍵不在於硬體有多強，而在於**軟體演算法**與**編譯器**能否將串行邏輯拆解為可平行執行的任務（即拉高 Parallel Portion）。
- 總結：
  <br>Amdahl's Law 提醒架構師與軟體工程師：系統的最終效能往往不由「最快的部分」決定，而是由「無法改進的瓶頸（串行部分）」所限制。因此在進行系統優化時，應優先找出並縮減不可平行的瓶頸段落，才能最大化硬體投資的報酬率（ROI）。

#### slide：16 Upheaval in Computer Design（電腦設計的重大變革）
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0016.jpg" width="50%">
</div>

探討了推動半導體與電腦架構演進的物理限制，以及當前產業正面臨的重大轉型與範式轉移（Paradigm Shift）。
- 本教學頁面重點內容
  - 過去 50 年：摩爾定律主導（Moore's Law Ruled）<br>軟體模型的紅利：透過微縮（Scaling）技術，可以在不改變軟體寫法與模型的情況下，直接獲得更高的處理效能與更佳的能源效率（即「免費的午餐」）。
  - 過去 10 年：技術微縮趨緩甚至停滯（Technology Scaling Slowed/Stopped）
    - 丹納德縮放定律終結（Dennard Scaling is over）：工作電壓（Supply voltage）無法再按比例下降，導致晶片功耗與散熱問題加劇。
    - 摩爾定律減速：每個電晶體的成本不再顯著下降。
    - CMOS 無替代品：短期內尚無能商業化替代 CMOS 的新技術。
    - 能耗瓶頸：能源效率（Energy efficiency）成為限制系統效能的主要關卡。
  - 2020 年代起的轉變（2020s Shift）<br>AI / ML 驅動：人工智慧與機器學習成為算力需求的龐大推手。
  - 軟體開發者再無「免費午餐」（No "free lunch" for software developers）<br>軟體工程師必須主動調整架構，平行化（Parallelism）與異質運算（Heterogeneity）已成為強制要求。
- 對此頁面的看法與分析
  - 單核效能紅利終結：傳統單純拉高 CPU 時脈的時代早已結束。如 Amdahl's Law 所預示，當單核效能無法靠製程自然提升時，系統設計必須轉向微架構創新與平行處理。
  - DSA（領域特定架構）的崛起：如 Hennessy 與 Patterson（本課程教材作者）所強調，為了因應 AI/ML 的算力爆炸，傳統通用型 CPU（如 x86）逐漸讓位給異質運算（Heterogeneous Computing），例如結合 GPU、NPU、TPU 等專用加速器，在有限的功耗預算下追求極致的能源效率。   
- 總結：<br>這頁投影片為整門「電腦架構」課程奠定了核心動機：當硬體物理層面（Dennard Scaling/Moore's Law）面臨極限時，電腦架構師的角色變得比以往任何時候都更加重要。現代軟硬體工程師必須深刻理解微架構、平行運算與記憶體階層設計，才能打造出能滿足 AI 時代需求的的高效能系統。

#### slide：17 Today's Dominant Target Systems（當前主流目標系統）
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0017.jpg" width="50%">
</div>

- 本教學頁面重點內容
  - 行動裝置（Mobile: smartphone/tablet）
    - 規模：每年出貨量超過 10 億台。
    - 核心 ISA：由 ARM 指令集架構（ISA） 在單晶片系統（SoCs）中佔據主導地位。
    - 異質整合：整合了 AI/神經網路引擎（Neural Engines）與各類專用加速器（如影像、音訊、資安、感測器）。
  - 倉庫級電腦 / 雲端資料中心（Warehouse-Scale Computers, WSCs）
    - 規模：每個資料中心擁有超過 10 萬個 CPU 核心。
    - 架構組合：以 x86 架構為主，搭配快速成長的 Arm CPU 以及客製化加速器（如 Google TPU 等）。
    - 瓶頸：能源消耗與碳足跡已成為當前最主要的發展瓶頸。
  - 嵌入式與邊緣運算（Embedded and Edge）
    - 應用領域：消費性電子、汽車電子（Automotive）與物聯網（IoT）。
    - RISC-V 崛起：RISC-V ISA 在微控制器（MCU）與邊緣 AI 晶片中展現強勁的成長趨勢。
    - Edge AI 爆發：邊緣 AI（如 TinyML、裝置端生成式 AI）正在快速擴張。
- 看法與分析
  - 三種市場，三套生存法則：
    - Mobile 強調「極致能效比」；
    - WSC 追求「大規模平行與降低 TCO（總擁有成本/能源開銷）」；
    - Edge 則看重「成本、彈性與即時性」。
  - ISA 的陣營演變（x86 vs ARM vs RISC-V）：
    - 過去 x86 壟斷 PC 與伺服器，但現在 Arm 已跨入資料中心；
    - 開源的 RISC-V 則在邊緣裝置與特定領域加速器（DSA）中快速崛起，呼應了本課程選用 RISC-V 作為教材核心 ISA 的趨勢。
  - AI 驅動架構無所不在：從手機的神經網路引擎到 Edge 端運算，再到雲端的 AI 加速晶片，驗證了上一頁（Slide 16）提到的「AI/ML 正在驅動整體算力需求與異質運算發展」。
- 總結<br>本頁投影片精準歸納了現代晶片設計的戰場——沒有單一架構能通吃所有市場。現代電腦架構師必須根據目標系統（Mobile、Cloud、Edge）的約束條件，靈活結合 ISA 選型、平行化設計與異質 AI 加速器，才能打造出具備競爭力的系統。

#### slide：18 Beyond Moore's Law（超越摩爾定律？）
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0018.jpg" width="50%">
</div>

本頁投影片（Slide 18）主題為 「Beyond Moore’s Law?」（超越摩爾定律？），引用了電腦圖靈獎（Turing Award）得主 John Hennessy 與 David Patterson 的著名觀點：「電腦架構的全新黃金時代」（A New Golden Age for Computer Architecture）。
- 本教學頁面重點內容
  - 微處理器歷史發展趨勢圖（Microprocessor Trend Data）：
    - 電晶體數量（Transistors, 藍標）：持續呈指數成長（摩爾定律）。
    - 單線程效能（Single-Thread Performance, 橘標）：約在 2005–2010 年間開始平緩，成長幅度極低。
    - 時脈頻率（Frequency, 綠標） 與 典型功耗（Typical Power, 紅標）：受限於 Dennard Scaling（丹納德縮放定律）的終結，頻率與功耗在 2005 年左右即觸及天花板而無法繼續提升。
    - 邏輯核心數（Number of Logical Cores, 紫標）：為彌補單核效能停滯，核心數自 2005 年起開始急速上升（邁向多核/平行時代）。
  - 後摩爾定律時代的關鍵疑問（右上角方框）：
    - 加速器數量（Number of accelerators?）：未來的晶片該整合多少個專用加速器？
    - 平行化與專業化（Parallelization and specialization?）：如何進一步推動平行處理與針對特定領域進行硬體客製化/專業化？
- 對此頁面的看法與分析
  - 從「軟體通用」轉向「硬體專業化（DSA）」
    - 過去 40 年，軟體工程師享有「免費午餐」——只要等新 CPU 出來，程式就會自動變快。
    - 如今單核效能成長幾乎歸零，唯有透過 領域特定架構（Domain-Specific Architecture, DSA）、特定領域加速器（如 NPU/TPU/GPU） 以及 軟硬體協同設計（Hardware/Software Co-Design），才能在功耗受限的情況下持續拉高效能。
  - 為什麼是「電腦架構的黃金時代」？
    - 當最底層的物理製程（Moore's Law）無法再獨立解決效能問題時，責任便轉移到了架構師（Architects）身上。
    - 如今開放指令集（如 RISC-V）普及與敏捷晶片開發（Agile Chip Development）抬頭，讓學者與工程師能以更低的門檻創新設計專用晶片，造就了電腦架構研究最活躍的新時代。
- 總結：<br>本頁投影片給出了電腦架構發展的終極解答：「摩爾定律的放緩並非危機，而是轉機」。未來的算力提升將不再依賴單一微處理器頻率的提升，而是取決於如何靈活結合平行運算、專用加速器與開放 ISA，以回應 AI 與新世代應用的龐大算力需求。

#### slide：19 Trends in Machine Learning Hardware
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0019.jpg" width="50%">
</div>

#### slide：20 The Verticalization of Silicon
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0020.jpg" width="50%">
</div>

#### slide：21-22 Course Logistics（課程行政與基本資訊）
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0021.jpg" width="48%">
  <img src="./Lecture/SD1/SD1_page-0022.jpg" width="48%">
</div>

詳細說明了國立陽明交通大學（NYCU）資訊工程學系「電腦架構（Computer Architecture）」課程的授課資訊、參考教材與先修要求。
- 本教學頁面重點內容
  - 授課教師（Instructor）：張庭綜教授（Ting-Jung Chang，E-mail: tingchang@cs.nycu.edu.tw）。
    <br>Office Hours：每週二 16:00–17:00 於工程三館 EC707（採預約制）。
  - 上課時間與地點（Lectures）：每週二 13:20–15:10 於工程二館 EDB27。
  - 指定教科書（Text）：Computer Architecture: A Quantitative Approach, 6th Edition（由 John L. Hennessy 與 David A. Patterson 所著的電腦架構經典權威教材）。
  - 先修課程（Prerequisite）：電腦組織（Computer Organization）或同等課程。
  - 課程網頁（Course Webpage）：校內 e3 教學平台。
- 對此頁面的看法與總結
  - 定位高階且注重定量分析：採用被譽為電腦架構「聖經」的 Quantitative Approach（量化研究法）第 6 版作為教材，代表本課程並非停留在基礎的概念介紹（如大學部初階的 Computer Organization），而是著重於效能量化、複雜的微架構設計（如 Superscalar、Cache 記憶體階層與 Out-of-Order 執行）與效能優化分析。
  - 紮實的先修要求：門檻要求具備「電腦組織」的基礎知識，這是為了確保學生已掌握基本的組合語言（RISC-V/MIPS）、單週期/多週期 CPU 與基礎管線化（Pipeline）的概念，方能順利接軌後續的 4 個 Verilog 設計實驗與高階架構探討。
<br>總體而言，這是一門針對資工系中高年級或研究所設計的深度電腦架構核心課程，建議修課學生預先複習電腦組織的內容，並熟悉 Verilog 語法以因應後續的實作挑戰。

**計算機結構－計量方法 (Computer Architecture: A Quantitative Approach, 5/e)**
<br>這本由 John Hennessy 與 David Patterson 合著的《電腦架構：量化研究方法》第六版，是該領域最具影響力的經典教材，旨在透過量化分析與實務工程設計來拆解電腦系統。書中收錄了衡量效能、功耗與可靠性的核心數學公式，並提出諸如 Amdahl’s Law 與 90/10 局部性法則等設計準則，引導讀者理解硬體與軟體間的權衡。隨著 Moore’s Law 的減緩與 Dennard Scaling 的終結，本版特別強調了從通用型處理器向領域特定架構（DSA）的範式轉移，並深入探討了開源指令集 RISC-V、GPU 以及**倉庫級運算（WSC）**等現代技術。其核心目的在於教會工程師如何在物理限制與運算需求爆炸的時代，利用平行處理與新興材料重塑電腦架構的未來。
- Chapter 1 計量設計與分析的基礎
- Chapter 2 記憶體層級的設計
- Chapter 3 指令階層平行化及其開發
- Chapter 4 向量、SIMD 與 GPU 結構當中的資料階層平行化
- Chapter 5 執行緒階層平行化
- Chapter 6 開發需求階層與資料階層平行化的數位倉儲型電腦
- Appendix A 指令集原理
- Appendix B 記憶體層級的回顧
- Appendix C 管線化：基本與進階的觀念


#### slide：23 Course Logistics
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0023.jpg" width="50%">
</div>

#### slide：24 Course Logistics
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0024.jpg" width="50%">
</div>

#### slide：25 Course Structure（課程結構與成績評分機制）
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0025.jpg" width="50%">
</div>

- 本教學頁面重點內容
  - 學期評分項目與佔比（Grading Scheme）：
    - Midterm（期中考）：20%（預計於 10/27 左右舉行）。
    - Final（期末考）：30%（預計於 12/22 左右舉行）。
    - Labs（實驗作業）：50%，包含 4 個 Verilog 硬體設計實驗。
  - 不計分練習（Ungraded Problem Sets）：0%
    - 目的：旨在協助學生理解與掌握課程觀念。
    - 討論：鼓勵學生與同儕及助教/教授自由討論。
    - 備考：對於期中、期末考的準備非常有幫助。
- 對此課程結構的觀點與看法
  - 重質重實作（Hands-on Emphasis）：
    <br>實驗占比高達 50%，搭配前面的教學內容（包含需要實作 Pipeline、Reorder Buffer、Superscalar 與 Cache 等），顯示這門課程極度看重將理論轉化為 Verilog RTL 程式碼的實作能力。
  - 考試與作業並重：
    <br>期中與期末考合佔 50%，代表僅會寫 Code 還不夠，對指令集架構與微架構的理論觀念（如 Amdahl's Law、Hazards 機制等）也必須深刻理解。
  - 學習資源的合理利用：
    <br>雖然 Problem Sets 佔比為 0%，但它是連結「理論」與「筆試（50%）」的橋樑。不計分能減輕交作業的壓力，但認真完成將是考高分的關鍵。
- 總結與建議：
  <br>這是一門典型的硬核硬體設計與架構課程。建議策略為：
  - 全力攻克 Labs：提早開始撰寫與 Debug Verilog，拿到這 50% 的基本盤。
  - 活用 Problem Sets：雖然不計分，但務必親自練習並參與討論，作為期中/期末考前最佳的檢測指標。

#### slide：26 Course Logistics
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0026.jpg" width="50%">
</div>

#### slide：27 Course Logistics
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0027.jpg" width="50%">
</div>

#### slide：28 Course Logistics
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0028.jpg" width="50%">
</div>

#### slide：29 Course Logistics
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0029.jpg" width="50%">
</div>

#### slide：30 Course Logistics
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0030.jpg" width="50%">
</div>

#### slide：31 Course Logistics
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0031.jpg" width="50%">
</div>

#### slide：32 Course Logistics
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0032.jpg" width="50%">
</div>

#### slide：33 Course Logistics
<div align="left" >
  <img src="./Lecture/SD1/SD1_page-0033.jpg" width="50%">
</div>











