Prompt：請說明本教學重點內容及你的看法，最後以250字內總結
### Week 2 課堂逐字稿

## slide：1 -2
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0001.jpg" width="49%">
  <img src="./Lecture/SD2/SD2_page-0002.jpg" width="49%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：3
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0003.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：4
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0004.jpg" width="50%">
</div>

本投影片主題為 「Architecture vs. Microarchitecture」（架構與微架構的比較），明確劃分了電腦系統設計中兩個不同層次的範疇：
- 本教學重點內容
  - 架構 / 指令集架構（Architecture / Instruction Set Architecture, ISA）：指程式設計師可見的軟硬體介面與規範。內容包含：
    - 程式員可見狀態（記憶體與暫存器）
    - 運算指令及其運作方式（Operations）
    - 執行語意與中斷機制（Execution Semantics / Interrupts）
    - 輸入/輸出（Input/Output）
    - 資料類型與大小（Data Types/Sizes）
  - 微架構 / 組織（Microarchitecture / Organization）：指如何實現 ISA 的具體硬體設計與權衡。重點在於依據特定指標（速度、效能、成本、功耗）進行設計取捨。範例包括：
    - 管線深度與管線數量（Pipeline depth / number of pipelines）
    - 快取大小與矽晶圓面積（Cache size / silicon area）
    - 峰值功耗、執行順序、匯流排寬度與 ALU 寬度（Peak power, execution ordering, bus/ALU widths）
- 個人看法與分析：
  <br>這頁投影片清楚表達了電腦架構中最核心的 抽象化（Abstraction）概念。
  - 軟硬體的契約（Interface vs. Implementation）：ISA 扮演「契約」角色，確保軟體只需對應統一的規格撰寫，即可跨世代執行；而微架構則是硬體工程師在晶片實作層面的「內部藍圖」。
  - 權衡的藝術（Tradeoffs）：相同的 ISA（例如 x86 或 RISC-V）可以透過不同的微架構來實現——例如低功耗的嵌入式核心或追求極致算力的伺服器晶片，其差異就在於管線、快取與功耗等微架構參數的取捨。
- 總結：
  <br>本投影片重點在於區分「架構（ISA）」與「微架構」的界線。架構是軟硬體之間的介面與規範，定義暫存器、指令集、資料型態與中斷語意；微架構則是實現該架構的硬體組織方式，透過調整管線深度、快取容量、匯流排寬度與功耗等參數，在速度、成本與能耗之間取得最佳平衡。兩者的分離確保了軟體相容性與硬體創新的彈性。

## slide：5
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0005.jpg" width="50%">
</div>

- 本教學重點內容
  <br>本投影片重點在於區分「架構（ISA）」與「微架構」的界線。架構是軟硬體之間的介面與規範，定義暫存器、指令集、資料型態與中斷語意；微架構則是實現該架構的硬體組織方式，透過調整管線深度、快取容量、匯流排寬度與功耗等參數，在速度、成本與能耗之間取得最佳平衡。兩者的分離確保了軟體相容性與硬體創新的彈性。
  - 1955 年之前 (up to 1955)：軟體主要以數值常規函式庫（Libraries of numerical routines）為主，包含：
    - 浮點數運算（Floating point operations）
    - 超越函數（Transcendental functions）
    - 矩陣運算與方程式求解器（Matrix manipulation, equation solvers）
  - 1955–1960 年：高階語言與作業系統開始出現。
    - 高階程式語言：如 1956 年問世的 Fortran。
    - 作業系統與系統軟體：包含組譯器（Assemblers）、載入器（Loaders）、連結器（Linkers）與編譯器（Compilers），以及記錄使用量與計費的會計程式（Accounting programs）。
  - 早期電腦運作的困境（框內重點）：
    - 機器需要具備豐富經驗的操作員才能維護與執行。
    - 大多數使用者無法理解、更無法親自撰寫這些軟體程式。
    - 因此，電腦售出時必須隨機附帶大量常駐軟體（Resident software），以協助使用者操作。
- 個人看法與分析：
  <br>這頁投影片揭示了早期電腦開發中 「軟體與硬體高度綁定」與「高進入門檻」 的歷史脈絡：
  - 抽象化階層的建立：早期使用者必須直接面對底層邏輯與複雜數學演算法。Fortran 與編譯器/載入器的出現，代表電腦科學正式進入「高階抽象化」時代，大大降低了編程門檻。
  - 系統軟體的誕生動機：早期大型主機昂貴且操作複雜，需要專屬系統軟體與常駐程式來排程與管理資源，這正是現代作業系統（OS）與開發工具鏈的雛形。
- 總結：
  <br>本投影片回顧 1950 年代軟體演進。1955 年前以浮點數與矩陣等數學函式庫為主；1955–60 年間則誕生了 Fortran 等高階語言，以及組譯器、編譯器與作業系統雛形。由於當時電腦操作極度複雜且非一般使用者能撰寫，機器發售時必須附帶大量常駐軟體並由專業人員操作。這段歷史展現了軟體抽象化與自動化工具如何逐步降低硬體使用門檻，奠定現代電腦系統疊層的基礎。

## slide：6
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0006.jpg" width="50%">
</div>

- 本教學重點內容
  <br>本頁投影片主題為 「Compatibility Problem at IBM」（IBM 的相容性問題），講述了 1960 年代初期 IBM 所面臨的產品線相容性危機，以及促成 IBM System/360 誕生的歷史背景：
  - 1960 年代初期的碎片化危機：IBM 當時擁有多達 4 條互不相容的電腦產品線（例如 $701 \rightarrow 7094$、 $650 \rightarrow 7074$、 $702 \rightarrow 7080$、 $1401 \rightarrow 7010$）。
  - 各系統相互獨立且封閉：每個系統家族都有各自專屬的：
    - 指令集（Instruction set）
    - I/O 系統與次級儲存媒體（磁帶、磁鼓、磁碟）
    - 軟體工具鏈（組譯器、編譯器、函式庫）
    - 目標市場（如商業計算、科學計算、即時處理等）
  - 變革動機：軟體與硬體綑綁且無法跨機器轉移，導致極高研發與維護成本，最終促成了統一架構家族 IBM 360 的誕生。
- 個人看法與分析：
  <br>這頁投影片揭示了電腦產業發展史上的重要轉折點：
  - 相容性（Compatibility）概念的崛起：IBM 360 的誕生正式確立了「指令集架構（ISA）」與「微架構實作」分離的思想。透過統一 ISA，顧客升級硬體時不再需要重寫軟體，開創了現代系列化電腦（Computer Family）的先河。
  - 商業與技術的雙重勝利：解決相容性問題不僅降低了 IBM 的軟體開發成本，更透過生態系的保護（Lock-in），大幅鞏固了 IBM 在大型主機市場的霸主地位。
- 總結：
  <br>本投影片講述 1960 年代初 IBM 擁有 4 條互不相容的電腦產品線。各系統的指令集、I/O 介面、儲存裝置及編譯器等軟體工具鏈完全獨立，針對不同市場分散發展。這種碎片化導致軟體無法跨平台重用，開發與轉移成本極高。為解決此相容性危機，IBM 推出了劃時代的 IBM 360 系列，透過統一指令集架構（ISA），實現軟體相容性與硬體規格的可擴充性，奠定了現代電腦系統架構設計的核心範式。

## slide：7
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0007.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片主題為 「IBM 360: A General-Purpose Register (GPR) Machine」（通用暫存器架構），詳細介紹了 IBM 360 的核心硬體規格與規格設計：
  - 處理器狀態（Processor State）：
    - 具有 16 個 32-bit 通用暫存器（GPR），可用於索引（Index）與基底暫存器（Base register），其中 Register 0 具備特殊屬性。
    - 具有 4 個 64-bit 浮點數暫存器。
    - 配有 程式狀態字組（Program Status Word, PSW），包含 PC（程式計數器）、狀態碼（Condition codes）與控制旗標。
  - 定址與架構：
    - 屬於 32-bit 機器但採用 24-bit 位址（且沒有任何指令直接包含 24-bit 位址）。
  - 資料格式（Data Formats）：
    - 支援 8-bit Bytes、16-bit Half words、32-bit Words 與 64-bit Double words。
    - 歷史里程碑：IBM 360 是奠定 「1 Byte = 8 bits」 標準的關鍵始祖。
- 個人看法與分析：
  <br>這頁投影片展現了電腦設計史上的重要里程碑：
  - 通用暫存器（GPR）架構的普及：IBM 360 拋棄了早期專用暫存器的限制，改用通用暫存器加上基底定址（Base-displacement addressing），為後來的現代 CPU 指令集（如 x86, ARM, RISC-V）樹立了標準樣板。
  - 規格標準化的深遠影響：投影片特別提及「1 Byte = 8 bits」。在 IBM 360 出現之前，各家電腦的字組與 Byte 長度五花八門（如 6-bit 或 9-bit），IBM 360 統一以 8-bit 為 Byte 基本單位，不僅簡化了資料處理與文字編碼，更影響了往後半個世紀的資訊工業發展。
- 總結：
  <br>本投影片介紹 IBM 360 的硬體規格。其採用通用暫存器（GPR）架構，配備 16 個 32-bit 通用暫存器、4 個 64-bit 浮點數暫存器與 PSW，並採用 32-bit 機器架構搭配 24-bit 位址系統。此外，IBM 360 定義了 8-bit Byte、16-bit Half word、32-bit Word 及 64-bit Double word 等資料格式。這項設計奠定了現代電腦將 1 Byte 定義為 8 bits 的行業標準，為後世 CPU 指令集與資料格式劃下了深遠的基石。

## slide：8
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0008.jpg" width="50%">
</div>

- 本教學重點內容
  <br>本頁投影片主題為 「IBM 360: Initial Implementations」（IBM 360 初期的硬體實作與對照），展示了相同指令集架構（ISA）如何透過不同的微架構來實體化，並強調了 ISA 作為軟硬體介面的重大意義：
  - 不同型號（Model 30 vs. Model 70）的微架構差異：
    - 記憶體容量（Storage）：Model 30 為 $8\text{K} - 64\text{KB}$；Model 70 達到 $256\text{K} - 512\text{KB}$。
    - 資料通道（Datapath）：Model 30 僅為 8-bit；Model 70 達到 64-bit。
    - 電路延遲（Circuit Delay）：Model 30 為 $30\text{ nsec/level}$；Model 70 為 $5\text{ nsec/level}$。
    - 內部儲存與控制（Local / Control Store）：Model 30 使用主記憶體與唯讀控制記憶體（Read-only $1\mu\text{sec}$）；Model 70 則使用電晶體暫存器與傳統硬連線電路。
  - 關鍵創新與里程碑：
    - 隱藏技術差異：IBM 360 ISA 完全隱藏了低階與高階機型之間的底層硬體實作差異。
    - 第一個真正的軟硬體可移植介面：IBM 360 是電腦史上第一個設計為可移植軟硬體介面的 ISA，且其架構經過微幅修改後沿用至今（如現代 IBM Z 系列主機）。
- 個人看法與分析：
  <br>這頁投影片為前面提及的「Architecture vs. Microarchitecture」提供了最經典的歷史實體範例：
  - 商業與效能的彈性平衡：Model 30 定位為低成本入門機（8-bit datapath），而 Model 70 則是高效能旗艦機（64-bit datapath）。兩者硬體規格懸殊，但因為共享相同的 ISA，軟體無需修改即可雙向執行。
  - 奠定現代電腦工業基石：這項「ISA 相容性」設計使得軟體資產得以長期累積與資產保護，徹底改變了整個資訊產業的商業模式。
- 總結：
  <br>本頁重點比較 IBM 360 的 Model 30 與 Model 70 實作。兩者在資料通道（8-bit vs 64-bit）、記憶體容量及電路速度上存在巨大差異，但共享相同的 ISA。IBM 360 成功隱藏了底層硬體細節，成為電腦史上首個實現軟硬體介面可移植性的重大里程碑，其架構至今仍被沿用。

## slide：9
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0009.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片主題為 「IBM 360: Over 50 years later... The zSeries z16 Microprocessor」，展現了 IBM 360 架構經過半個多世紀的演進，在現代旗艦微處理器（IBM z16）上的承襲與技術突破：
  - 製程與算力：採用三星 7nm 製程，時脈高達 5.2 GHz，在 $530\text{ mm}^2$ 的晶片面積內整合了 225 億個電晶體。
  - 位址架構演進：支援 64-bit 虛擬定址（展示了從最早 S/360 的 24-bit，到 S/370 的 31-bit 擴充，再到現代 64-bit 的演進歷程）。
  - 核心與多層級快取：每顆晶片包含 8 個核心，配有龐大的快取體系： $128\text{ KB}$ L1、 $32\text{ MB}$ L2、 $256\text{ MB}$ L3 以及高達 $2048\text{ MB}$ ($2\text{ GB}$) 的 L4 快取。
  - AI 算力整合：硬體直接整合 片上 AI 加速器（On-chip AI accelerator），以滿足企業級即時推論的需求。
- 個人看法與分析：
  <br>這頁投影片為 IBM 360 系列的傳奇歷程畫下了精采的現代腳註：
  - 向上相容性（Backward Compatibility）的極致典範：IBM 360 於 1960 年代設計的架構核心，經歷了 24-bit $\rightarrow$ 31-bit $\rightarrow$ 64-bit 的定址擴展，至今已過半個世紀，現代 z16 依然能執行數十年前寫成的企業軟體。這種跨世代的相容性，是資訊工程史上維護軟體資產最成功的範例。
  - 微架構與時俱進：雖然指令集（ISA）承襲歷史脈絡，但底層微架構完全採用了最頂級的現代技術（如 7nm、5.2GHz、極大化 L4 快取與晶片內建 AI 加速器），體現了「ISA 保持穩定，微架構持續突破」的電腦架構核心哲學。
- 總結：
  <br>本頁展示了 IBM 360 架構歷經半世紀演進至現代 IBM z16 處理器的成果。z16 採用 7nm 製程與 5.2GHz 時脈，整合 225 億個電晶體、8 核心、高達 2GB 的 L4 快取及片上 AI 加速器，並將定址能力由早期的 24-bit 擴展至 64-bit。這項成就證明了優異的指令集架構（ISA）能在維持軟體相容性的同時，藉由微架構的不斷革新適應現代高算力與 AI 需求。

## slide：10
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0010.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片主題為 「Instruction Set Architecture (ISA) 在電腦系統堆疊中的定位」，透過階層堆疊圖（Computer Systems Stack）揭示了 ISA 在軟硬體之間的關鍵紐帶角色：
  - 電腦系統堆疊（The Computer Systems Stack）：
    - 軟體層（Software Layers）：Application $\rightarrow$ Algorithm $\rightarrow$ Programming Language $\rightarrow$ Operating System/Virtual Machines $\rightarrow$ Compiler。
    - 指令集架構（ISA）：位於堆疊的核心交界處（黃色標示區），向上對接編譯器與作業系統，向下對接硬體實作。
    - 硬體實作層（Hardware Layers）：Microarchitecture $\rightarrow$ Register-Transfer Level (RTL) $\rightarrow$ Gate Level $\rightarrow$ Circuits $\rightarrow$ Devices $\rightarrow$ Physics / Technology。 
  - 軟硬體分界（Abstraction Boundary）：
    - 右圖將系統分為上層的軟體世界（Application、OS、Compiler、Firmware）與下層的硬體實作（Processor/Mem、I/O System、Datapath & Control、Digital Design、Circuit Design、Layout & Fab）。
    - ISA 作為兩者之間的抽象化介面，定義了處理器的功能介面，使上層軟體與底層晶片設計能獨立發展與創新。
- 個人看法與分析：
  <br>這頁投影片為前面數頁講述的歷史案例（如 IBM 360 的誕生與演進）提供了系統性的理論框架：
  - 抽象化階層（Abstraction Layer）的重要性：電腦系統極其複雜，無法單一步驟跨越從物理元件到應用程式的巨幅鴻溝。ISA 是軟體與硬體的「劃時代契約」，只要 ISA 保持穩定，軟體開發者就不必關心底層採用的是 7nm 三星製程還是管線設計，而硬體工程師也能自由對微架構進行優化。
  - 跨領域設計（Hardware-Software Co-design）：理解這個堆疊有助於系統架構師明確定位問題所在——效能優化可以發生在編譯器層、微架構層乃至電路層，而 ISA 則保證了跨層級的相容性。
- 總結：
  <br>本頁展示了電腦系統堆疊結構，說明 ISA 位於軟體（演算法、程式語言、OS、編譯器）與硬體（微架構、RTL、邏輯閘、電路及物理元件）之間的核心交界。ISA 作為抽象化介面，隔開了軟體開發與硬體晶片實作，使軟體無需關心底層電路即可執行，硬體亦可在不破壞相容性的前提下優化微架構，是現代電腦系統設計最重要的分層基石。

## slide：11
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0011.jpg" width="50%">
</div>

- 本教學重點內容
  <br>本頁投影片主題為 「Instruction Set Architecture (ISA) 的功能抽象定義」，進一步闡明了 ISA 作為功能抽象（Functional Abstraction）與「心智模型（Mental Model）」的具體含義：
  - ISA 所定義的範疇（What it is）：
    - 系統能執行哪些運算操作（What operations can be performed）。
    - 如何命名儲存空間位置（How to name storage locations，如暫存器與記憶體定址）。
    - 指令的位元格式與編碼（The format / bit pattern of the instructions）。
  - ISA 通常不定義的範疇（What it is NOT）：
    - 運算執行的時序（Timing of the operations）。
    - 運算所消耗的功耗（Power used by operations）。
    - 運算與儲存元件在硬體上具體如何實現（How operations/storage are implemented）。
  - 核心特點：同一個 ISA 可以有多種不同的硬體實作方式（Many implementations possible for a given ISA）。
- 個人看法與分析：
  <br>這頁投影片精準揭示了電腦工程中 「介面（Interface）與實作（Implementation）分離」 的核心哲學：
  - 黑盒化（Black-box Design）的效益：ISA 提供了軟體設計者一個清晰的功能模型，使軟體無須關注電路延遲、時脈週期或功耗細節即可運作。
  - 市場競爭與創新空間：正因為 ISA 不限制「時序」與「實現方式」，硬體廠商才能在相同的 ISA 規範下，透過管線化、亂序執行、多核架構等微架構創新來競爭效能與能效比（例如 Intel 與 AMD 在 x86 ISA 下的競爭）。
- 總結：
  <br>本頁強調 ISA 是處理器的功能抽象（心智模型）。它定義指令格式、操作類型與儲存命名，但不包含時序、功耗及硬體具體實現方式。這種設計使單一 ISA 能擁有高低效能、不同功耗等的多種硬體實作。總結來說，ISA 是軟硬體的介面契約，劃清了功能規範與硬體實作的界線，讓軟體生態得以延續，同時為硬體微架構的效能優化留出彈性空間。

## slide：12
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0012.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片主題為 「Different Instruction Set Architecture」（三大主要指令集架構），對比了當今資訊產業中三大主流 ISA 的特點與應用領域：
  - ARM：
    - 由 ARM 公司開發的指令集家族。
    - 廣泛應用於行動裝置與低功耗設備（Mobile & Low-power devices）。
    - 現已積極擴展至桌面電腦、資料中心與雲端伺服器市場。
  - x86：
    - 由 Intel（與 AMD）開發的指令集家族。
    - 主要用於通用計算系統（桌上型電腦與伺服器）。
  - RISC-V：
    - 源自加州大學柏克萊分校（UC-Berkeley）的開放標準指令集（Open standard ISA）。
    - 主要應用於嵌入式系統，並在 AI 加速器與研究晶片中獲得早期採用。
- 個人看法與分析：
  <br>這頁投影片展示了現代指令集架構在 商業模式 與 技術場景 上的三足鼎立生態：
  - 商業模式的差異：x86 代表傳統封閉且高度壟斷的架構；ARM 採用智慧財產權（IP）授權模式；而 RISC-V 則透過開放授權打破了授權費門檻，鼓勵廣大開源社群與客製化晶片的創新。
  - 動態競爭與領域轉移：過去 ARM 守著低功耗行動市場、x86 獨霸高效能 PC/伺服器、RISC-V 用於嵌入式。然而隨著微架構進步與專用計算需求，ARM 已侵入伺服器與桌面領域，RISC-V 也迅速拓展至 AI 加速與領域特定架構（DSA），體現了 ISA 生態系的多元與活力。
- 總結：
  <br>本頁介紹 ARM、x86 與 RISC-V 三大指令集架構。x86 主導傳統 PC 及伺服器市場；ARM 在行動與低功耗領域佔據優勢並向桌面與雲端擴展；開放標準的 RISC-V 則在嵌入式與 AI 加速晶片中展露頭角。三大 ISA 代表了專有封閉、IP 授權及開源共享不同的商業模式。這證明了只要符合軟軟體介面規範，相同的計算需求能透過多元的指令集生態系來達成。

## slide：13
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0013.jpg" width="50%">
</div>

- 本教學重點內容
  <br>本頁投影片主題為 「Same Architecture/Different Microarchitecture」（相同架構，不同微架構），對比了 Intel 旗下的兩款產品（Intel Xeon 與 Intel Atom），展現如何在同一指令集架構（x86 ISA）下，透過完全不同的微架構設計來滿足截然不同的市場需求：
  - Intel Xeon（針對高效能伺服器/工作站）：
    - 指令集：x86 instruction set。
    - 核心數與功耗：32+ 個核心、功耗達 200W+。
    - 執行機制：每週期/每核心可解碼 6 個指令（Decode 6 instructions/cycle/core），採用亂序執行（Out-of-order）。
  - Intel Atom（針對低功耗嵌入式/行動設備）：
    - 指令集：x86 instruction set。
    - 核心數與功耗：僅 1–8 個核心、功耗僅約 2W。
    - 執行機制：每週期/每核心僅解碼 2 個指令，採用簡單的順序執行（In-order）。
    - 快取與時脈：僅配有數十 KB L1 及 < 2 MB L2 快取，時脈為 1.6 GHz。
- 個人看法與分析：
  <br>這頁投影片為本系列教學的核心概念（ISA vs. Microarchitecture）提供了極具說服力的實證：
  - 軟體生態的絕對保護：Xeon 與 Atom 兩者功耗相差百倍（200W+ vs. 2W）、微架構完全不同（亂序 vs. 順序執行），但因為共享相同的 x86 ISA，同一個可執行檔無需重新編譯即可在兩者上執行。
  - 微架構取捨（Tradeoffs）的極致體現：這驗證了「ISA 決定功能，微架構決定效能與功耗」的原則。硬體設計師能根據極端不同的成本與能效預算，自由選擇流水線深度、解碼寬度與快取規模。
- 總結：
  <br>本頁以 Intel Xeon 與 Atom 為例，說明相同 ISA（x86）如何實作成截然不同的微架構。Xeon 採用 32+ 核、亂序執行與巨型快取，功耗達 200W+，追求極致算力；Atom 則以 1-8 核、順序執行與微型快取控制在 2W，主打低功耗。這證明了 ISA 劃清了軟體相容性與硬體實作的邊界，使同一套軟體能跨越伺服器與行動裝置，同時給予硬體設計極大的效能與能耗取捨彈性。

## slide：14
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0014.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片主題為 「Different Architecture / Different Microarchitecture」（不同架構，不同微架構），將兩款分別代表不同 ISA 與微架構設計頂峰的現代旗艦處理器（Intel Xeon 與 Apple M2 Ultra）進行對比：
  - Intel Xeon（x86 架構領域）：
    - 指令集與核心數：採用 x86 指令集，擁有 32+ 個核心。
    - 功耗與頻率：功耗達 200W+，時脈介於 2.0–3.5 GHz。
    - 微架構設計：每週期/每核心解碼 6 個指令（Decode 6），採用亂序執行（Out-of-order），配有數十 MB 的共享 L3 快取。
  - Apple M2 Ultra（ARM 架構領域）：
    - 指令集與核心數：採用 ARM 指令集，最高達 24 個核心。
    - 功耗與頻率：功耗控制在 ~90–100 W，峰值頻率約 3.5 GHz。
    - 微架構設計：每週期/每核心可解碼高達 8+ 個指令（Decode 8+），採用超寬幅亂序執行，並跨集群配置大型共享快取。
- 個人看法與分析：
  <br>這頁投影片展現了現代高階 CPU 設計中 「指令集特性（RISC vs. CISC）」與「能效比（Efficiency）」 的深刻差異：
  - ARM 指令集在超寬解碼（Wide Decode）的優勢：M2 Ultra 的每核心解碼寬度達到 8+ 指令/週期，高於 Xeon 的 6 指令/週期。這是因為 ARM 的定長指令格式相比於 x86 的變長指令格式，在硬體平行解碼（Parallel Decoding）上更具優勢。
  - 能效比（Perf-per-Watt）的巨幅提升：M2 Ultra 在提供頂級算力的同時，功耗僅需 90–100W（約為 Xeon 的一半）。這說明了優秀的微架構設計配合簡化指令集，能在大幅降低熱設計功耗（TDP）的同時維持極高的執行效能。
- 總結：
  <br>本頁比較 Intel Xeon（x86）與 Apple M2 Ultra（ARM）兩款完全不同 ISA 與微架構的頂級晶片。Xeon 具 32+ 核心、Decode 6 及 200W+ 功耗；M2 Ultra 則以 24 核心、Decode 8+ 與 90-100W 功耗展現高能效。這證明微架構創新與不同的 ISA 特性相結合，能在極端不同的能耗預算下實現頂級計算效能。

## slide：15
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0015.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片主題為 「Key ISA Decisions」（指令集架構設計的關鍵決策），探討架構師在制定 ISA 時必須確定的核心要素：
  - 操作數（Operands）：
    - 數量（How many?）：指令包含多少個運算元（例如單運算元、雙運算元或三運算元）。
    - 位置（Location?）：運算元儲存在何處（如暫存器、記憶體或立即數）。
    - 定址模式（Addressing mode?）：如何計算與存取記憶體位址。
    - 資料類型（Types?）：支援哪些型態（如整數、浮點數、字元等）。
  - 操作種類（Operations）：包含指令的類型（如算術、邏輯、控制流）與數量。
  - 指令格式（Instruction format）：包含指令的位元長度與欄位編碼定義。
- 個人看法與分析：
  <br>這頁投影片揭示了 ISA 設計中 「軟硬體折衷（Hardware-Software Tradeoffs）」 的核心思考：
  - 編譯器與硬體複雜度的平衡：操作數的選擇直接決定了編譯器產出程式碼的長度與硬體的解碼難度。例如，三運算元（RISC 常用）可保持暫存器獨立，簡化硬體，但可能增加指令數；雙運算元（x86 常用）則需覆蓋暫存器，增加編譯約束。
  - 架構設計的長遠性：定址模式與資料類型的決策一旦確定，將深遠影響未來數十年的晶片升級與軟體生態（如前面提到的 24-bit 延伸至 64-bit 位址歷程）。
- 總結：
  <br>本頁強調 ISA 設計的三大關鍵決策：操作數（數量、位置、定址模式與類型）、操作種類及指令格式編碼。這些決策定義了編譯器與硬體之間的溝通語言。合適的 ISA 決策能兼顧編譯器產出效率與硬體解碼難度，在硬體複雜度與軟體彈性之間取得最佳平衡，是奠定整個電腦系統效能與相容性的基石。

## slide：16
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0016.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片主題為 「ISA Classification: Operands」（指令集架構分類：操作數），介紹處理器如何根據操作數（Operands）的來源與儲存位置來對 ISA 進行分類：
  - 操作數來源類型（Operands may be from）：
    - 堆疊（Stack）：操作數隱式地位於堆疊頂端（Stack Architecture）。
    - 累加器（Accumulator）：操作數隱式地使用專用的累加暫存器（Accumulator Architecture）。
    - 暫存器（Register）：操作數顯式地位於通用暫存器中（Register-Register / Load-Store Architecture）。
    - 暫存器與記憶體（Register and Memory）：操作數可混合來自暫存器與主記憶體（Register-Memory Architecture）。
  - 核心問題：Where do operands come from and where do results go?（操作數來自何處？計算結果又將存往何處？）。
- 個人看法與分析：
  <br>這頁投影片探討了電腦架構演進史上的關鍵轉折點：
  - 從隱式到顯式操作數的演進：早期的堆疊（Stack）與累加器（Accumulator）架構為了節省珍貴的硬體門陣列與指令長度，大量採用隱式（Implicit）操作數。然而，現代 CPU（如 x86 與 RISC 架構）幾乎全面轉向暫存器（Register）與記憶體（Memory）模型，以提供更高程度的指令平行度（ILP）與編譯器最佳化空間。
  - 記憶體存取策略的劃分：
    - Register-Memory（如 x86）：允許算術指令直接對記憶體進行操作，可減少指令數量，但增加了硬體解碼與流水線控制的複雜度。
    - Register-Register / Load-Store（如 ARM, RISC-V）：強制所有算術指令僅能對暫存器操作，記憶體存取一律經由 Load/Store 指令，極大地簡化了硬體設計並提升運行時脈。
- 總結：
  <br>本頁強調 ISA 的分類核心在於定義運算元與結果的儲存位置（堆疊、累加器、暫存器或記憶體）。這一架構決策直接影響了指令集的編碼長度、編譯器生成程式碼的複雜度，以及硬體內部的資料流（Datapath）設計。

## slide：17
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0017.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片主題為 「Machine Models of ISA」（指令集架構的機器模型分類），介紹了四種主要的 ISA 機器模型及其運算元（Operands）存取機制與顯式命名數量（Number Explicitly Named Operands）：
  - Stack（堆疊模型）：
    - 機制：運算元隱式地位於堆疊頂端（Top of Stack, TOS），運算結果寫回堆疊。
    - 顯式命名運算元數：0 個（指令無需指定暫存器位址，如 ADD）。
  - Accumulator（累加器模型）：
    - 機制：一個運算元隱式來自專用的累加暫存器，另一個運算元可來自記憶體或暫存器，計算結果寫回累加器。
    - 顯式命名運算元數：1 個（僅需指定另一個運算元位址，如 ADD mem）。
  - Register-Memory（暫存器-記憶體模型）：
    - 機制：算術與邏輯指令可以直接混合存取暫存器與記憶體運算元。
    - 顯式命名運算元數：2 或 3 個（例如 x86 的 ADD EAX, [EBX]）。
  - Register-Register / Load-Store（暫存器-暫存器 / 載入-儲存模型）：
    - 機制：算術指令僅能存取通用暫存器，記憶體存取必須透過專用的 Load/Store 指令進行。
    - 顯式命名運算元數：2 或 3 個（例如 RISC 架構的 ADD R1, R2, R3）。
- 個人看法與分析：
  <br>這頁投影片清楚呈現了電腦系統架構從早期至現代的演變脈絡：
  - 程式碼密度（Code Density）與硬體複雜度的取捨：
    - Stack 與 Accumulator：顯式運算元少（0 或 1），指令長度短、程式碼密度高，適合早期記憶體極度昂貴的時代，但執行時產生嚴重的資料依賴，難以進行流水線平行化（Pipelining）。
    - Register-Register (Load-Store)：雖然指令需要 2 到 3 個顯式運算元位址，增加了程式碼長度，但讓編譯器能靈活調度大量的通用暫存器，極大地簡化了流水線控制與亂序執行（Out-of-Order Execution）硬體，成為現代 RISC 架構（如 ARM、RISC-V）的主流。
  - x86 與 RISC 的實作分岐：Register-Memory 模型（如 x86）提供了靈活的記憶體直接運算，但硬體內部往往需要將其拆解為微指令（Micro-ops）再以類似 Load-Store 的流水線執行；而純粹的 Load-Store 模型（如 RISC-V）則維持了指令執行的單純性與高時脈潛能。
- 總結：
  <br>本頁對比了 Stack、Accumulator、Register-Memory 與 Register-Register（Load-Store）四種 ISA 機器模型。顯式運算元數量從 0 個演進至 2-3 個，反映了電腦架構從追求高程式碼密度，轉向追求高流水線平行度與編譯器最佳化彈性的歷史趨勢。

## slide：18
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0018.jpg" width="50%">
</div>

- 本教學重點內容：
  <br>本頁投影片主題為 「Summary: Machine Model」（機器模型總結），透過計算等式 $C = A + B$ 在四種不同 ISA 機器模型下的程式碼實作，呈現運算元存取方式對指令序列與指令數量的影響：
  - Stack（堆疊模型）：
    - 程式碼序列：Push A $\rightarrow$ Push B $\rightarrow$ Add $\rightarrow$ Pop C。
    - 特點：指令最長（4 條指令），但每條指令均不需要顯式指定運算元暫存器位址，程式碼密度極高。
  - Accumulator（累加器模型）：
    - 程式碼序列：Load A $\rightarrow$ Add [B] $\rightarrow$ Store C。
    - 特點：需 3 條指令，隱式使用累加暫存器，指令中只需指定一個記憶體位址。
  - Register-Memory（暫存器-記憶體模型）：
    - 程式碼序列：Load R1, [A] $\rightarrow$ Add R3, R1, [B] $\rightarrow$ Store R3, [C]。
    - 特點：需 3 條指令，允許算術指令直接操作記憶體（如 [B]），減少了獨立的載入指令。
  - Register-Register / Load-Store（暫存器-暫存器 / 載入-儲存模型）：
    - 程式碼序列：Load R1, [A] $\rightarrow$ Load R2, [B] $\rightarrow$ Add R3, R1, R2 $\rightarrow$ Store R3, [C]。
    - 特點：需 4 條指令，將記憶體存取與 ALU 算術運算徹底解耦，算術指令只針對暫存器操作。
- 個人看法與分析：
  <br>這頁總結投影片清楚展示了電腦架構設計中 「指令數量（Instruction Count）」與「硬體設計複雜度（Hardware Complexity）」 的關鍵權衡（Tradeoff）：
  - 指令數量 vs. 單指令複雜度：
    - Register-Memory 雖然只需 3 條指令（指令數少），但 Add 指令內部需同時處理記憶體位址計算、記憶體讀取與算術運算，使得流水線（Pipeline）控制非常複雜。
    - Load-Store 模型雖然需要 4 條指令（指令數較多），但每條指令的功能極其專一且定長，非常利於硬體實現高時脈的硬體流水線與多指令發射（Superscalar）。
  - 現代處理器的主流趨勢：
    - 雖然 Stack 與 Accumulator 在早期的記憶體受限環境下非常有優勢，但現代通用 CPU（如 ARM、RISC-V 及 x86 內部的微指令）幾乎全面採用 Load-Store 或微結構上的 Register-Register 模式，以爭取最高的執行平行度（ILP）與極致的時脈頻率。
- 總結：
  <br>本頁以 $C = A + B$ 為例，對比了 Stack、Accumulator、Register-Memory 與 Load-Store 四種模型在執行同一運算時的程式碼差異。Load-Store 模型雖然指令數較多，但因成功分離了記憶體存取與算術運算，降低了硬體設計難度，成為現代高效能微架構（如 ARM、RISC-V）的首選架構。

## slide：19
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0019.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：20
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0020.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：21
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0021.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：22
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0022.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：23
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0023.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：24
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0024.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：25
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0025.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：26
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0026.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：27
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0027.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：28
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0028.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：29
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0029.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：30
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0030.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：31
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0031.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：32
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0032.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：33
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0033.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：34
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0034.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：35
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0035.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：36
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0036.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：37
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0037.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：38
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0038.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：39
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0039.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：40
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0040.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：41
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0041.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：42
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0042.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：43
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0043.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：44
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0044.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：45
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0045.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：46
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0046.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：47
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0047.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：48
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0048.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：49
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0049.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：50
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0050.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：51
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0051.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：52
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0052.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：53
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0053.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：54
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0054.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：55
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0055.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：56
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0056.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：57
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0057.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：58
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0058.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：59
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0059.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：60
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0060.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：61
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0061.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：62
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0062.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：63
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0063.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：64
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0064.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：65
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0065.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：66
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0066.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：67
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0067.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：68
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0068.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：69
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0069.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：70
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0070.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：71
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0071.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：72
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0072.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：73
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0073.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：74
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0074.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：75
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0075.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：76
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0076.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：77
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0077.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：78
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0078.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：79
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0079.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

















