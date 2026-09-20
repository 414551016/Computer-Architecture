
## 第1題：
Why did the end of Dennard scaling change how architects improve performance?
>為什麼 Dennard 縮放比例定律的終結改變了架構師提升效能的方式？
- Dennard 縮放定律的失效：過往當晶體管尺寸縮小時，功率密度保持不變，因此晶片可以在不大幅增加功耗與發熱的前提下，獲得更高的主頻（Clock Frequency）。但在 2000 年代中期，由於漏電流（Leakage Current）與靜態功耗（Static Power）急劇上升，Dennard 縮放定律終止，晶片迎來「功率牆（Power Wall）」。
- 效能提升策略的根本轉變：
  - 從單核主頻轉向平行處理：無法繼續透過提升時脈頻率來換取效能，架構師轉而發展指令級平行（ILP）、多核心（Multicore） 與 執行緒級平行（TLP）。
  - 從通用算力轉向能源效率（Energy Efficiency）：架構設計的核心指標從單純追求「最高峰值效能」轉變為「每瓦效能（Performance per Watt）」。








