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
  - 核心與多層級快取：每顆晶片包含 8 個核心，配有龐大的快取體系：$128\text{ KB}$ L1、 $32\text{ MB}$ L2、 $256\text{ MB}$ L3 以及高達 $2048\text{ MB}$ ($2\text{ GB}$) 的 L4 快取。
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
- 個人看法與分析：
- 總結：

## slide：12
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0012.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：13
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0013.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：14
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0014.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：15
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0015.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：16
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0016.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：17
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0017.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

## slide：18
<div align="left" >
  <img src="./Lecture/SD2/SD2_page-0018.jpg" width="50%">
</div>

- 本教學重點內容
- 個人看法與分析：
- 總結：

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

















