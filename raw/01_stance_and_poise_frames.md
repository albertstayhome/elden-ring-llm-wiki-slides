# Raw Clipping 01: 失衡值 (Stance) 與玩家韌性 (Poise) 筆記

> 整理來源：
> - Illusory Wall / Elden Ring Motion Values Sheet (Google Sheets)
> - Elden Ring Wiki (Fextralife) - Poise / Stance 頁面
> - Bandai Namco Patch Notes 1.07 & 1.10
> - 收集日期：2026-11-11

---

### (§1.1) Boss 失衡條 (Stance / Poise Damage) 怎麼算？
從 Google Sheet 數據表跟影片拆解抄下來的幾個常見 Boss 數據：
- Margit (惡兆妖鬼)、Malenia (女武神)、Maliketh (黑劍)：失衡上限都是 **80**
- Starscourge Radahn (碎星)：**120**
- Elden Beast (艾爾登之獸)：**150**

【重點機制 - 回復倒數計時】
打中 Boss 之後會啟動一個隱形計時器，如果在時間內沒有再削韌，Boss 的失衡條就會開始回血：
- 80 韌性的 Boss：大約 **5.0 秒**沒打到就會開始回
- 120 以上韌性的 Boss：大約 **6.0 秒**
- 一旦開始恢復，回復速度是每秒回復 **13** 點（超快，幾秒就回滿了）
- 玩家實用小技巧：飛刀 (Throwing Dagger / Kukri) 雖然只有 1 點削韌，但只要丟中就可以直接把那 5~6 秒的倒數重置！（打女武神跟黑劍超好用）

---

### (§1.2) 常用武器與戰技的削韌值 (Poise Damage)
記幾個我這輪比較常用、或是攻略影片常推的數值（以 60 FPS 實測數據為主）：
- Moonveil 名刀月隱「居合重擊 (Transient Moonlight R2)」：**30** 削韌（配刀氣貼臉才有 30，光刀氣只有一半左右，所以連砍 3 發剛好讓 80 韌的 Boss 處決）
- Lion's Claw 獅子斬戰技：**36** 削韌（兩下多一點，配跳劈可以直接處決 80 韌 Boss）
- Double-Handed Charged R2 (雙持蓄力重擊 / 大劍類)：約 **36~40** 削韌
- 魔法 Rock Sling 岩石球：一顆 11，三顆全中總共 **33** 削韌（法師前期破韌神器）

---

### (§1.3) 玩家自己的韌性 (Poise) 門檻：Patch 1.07 vs 1.10+
網路上很多舊攻略還在講「56 韌」或「61 韌」，但查了一下更新日誌早就改過了：
- Patch 1.07 開始調過 PvP/PvE 韌性，到了 **Patch 1.10+**（包含現在 1.12 DLC 版本）PvE 最實用的斷點剩兩個：
  1. **51 Poise**：PvE 黃金基本線，可以扛住小兵／多數 Boss 的「一下輕攻擊」不被斷招（喝水或揮重武器時超重要）
  2. **101 Poise**：高階門檻，PvE 可以扛兩下輕攻擊或部分中等衝擊力招式
- 如果配裝只有 49 或 50 韌性，跟 10 韌性體感上幾乎沒差（一樣一刀就被敲斷），寧願換一件輕一點的衣服或配大山羊護符湊到 51！
