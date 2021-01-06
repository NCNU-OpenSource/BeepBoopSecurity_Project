# BeepBoopSecurity_Project

## 動機發想

- 最一開始我們希望可以做一個**樂高殺手**，顧名思義就是用樂高做的殺手，藏在 MOLI 的角落攻擊他人，把樂高積木射到目標的前面一點點，讓目標採到，聽起來就超好玩的。
- 但 <font color=#800000>邱呱呱 aka 王嫂</font> 覺得實用性不足，於是我們就決定幫樂高殺手招募同伴，感應器殺手跟照相機殺手就來了，他們是一支要保家衛國的隊伍，如果有人想要強行闖入你家的話，就會拍照傳給使用者，讓使用者決定要不要攻擊，這樣就不會有無辜的人受害了，我們樂高殺手是正義的化身。
-  <font color=#800000>邱呱呱 aka 王嫂</font> 還是覺得不滿足，於是我們決定把樂高殺手再進化，因為樂高其實蠻貴的，所以我們把子彈換成橡皮筋，超聰明的！
- 試想你今天是壞人，想要闖進無辜百姓的家裡偷東西，這時突然有一個東西一直射橡皮筋，勢必會喚起小時候被爸爸拿橡皮筋修理的恐懼，保家衛國任務達成！


## 功能

- 感應器感應到有人經過之後，就會拍照傳送給使用者，由使用者決定要不要發射橡皮筋。


## 時間

### 12/18 前 

- 確定主題
- 樹莓派連接成功，設定完成
- 找齊需要的設備


### 12/25 開心的聖誕節

- 東洲最棒


### 12/30

- 完成紅外線偵測及影像辨識
- 機械手臂製作完成

### 1/1 開心的跨年

- 居酒屋好吃

### 1/4 

- 整合 NXT & Raspberry pi

## 所需設備

- Raspberry Pi 3
- 紅外線感測器
- 杜邦線（公母、母母）
- 電阻
- 麵包板
- WebCamera
    - SpotCam USB-CAM01 高畫質 FHD 視訊攝影機
    - [PChome 購買連結](https://24h.m.pchome.com.tw/prod/DCAS4U-A900ANFN2)
- NXT 第二代

## Raspberry Pi
### 接線方式

![](https://www.raspberrypi.com.tw/wp-content/uploads/2014/09/connect-serial-to-raspberry-pi-model-b-plus.png)
- 5V（墨綠線）
- Ground（紫線）
- GPIO17（紅線）

![](https://i.imgur.com/0umeUXd.jpg)

### 安裝套件

- **python package index**
```python=
sudo apt-get install python-pip
```
- **telepot**
```python=
sudo pip install telepot
```
- **GPIO**
```python=
sudo pip install RPi.GPIO
```
- **DateTime**
```python=
sudo pip install DateTime
```

## Telegram Bot
### 系統架構

- Python
- Telegram

### 建立
1. 搜尋 `BotFather`（點選有藍勾勾的那個）

     ![](https://i.imgur.com/5aSNVAU.jpg)
     
2. `/start`
3. `/newbot`
4. 替機器人取個名字
5. 命名 id，以`_bot`結尾（id名不可重複）

![](https://i.imgur.com/fatqGLk.png)

6. 系統會給你一串 API（要加在程式碼中的）

 ![](https://i.imgur.com/gEzzqDW.png)
 
  - API改在TOKEN那 不能洩漏不然會被亂改
    
   ![](https://i.imgur.com/RHdeLZj.png)


### 指令介紹
1. start 

![](https://i.imgur.com/Ml9UI5o.jpg)

2. attack


## LEGO MINDSTORMS NXT

### 什麼是 NXT？

- 這很難解釋，要看你是問哪個 NXT
- [這個 NXT](https://zh.wikipedia.org/wiki/WWE_NXT)
- [那個 NXT](https://zh.wikipedia.org/wiki/%E6%A8%82%E9%AB%98Mindstorms_NXT)

### 先備條件

- 建立樂高殺手（硬體部分）
    - 超音波感測器 * 1
    - 馬達 * 3
    - 樂高零件
- 需要技能
    - 會使用 NXT programming 的程式設計軟體
    - <font color = 'red'>保持童心</font>

### 步驟

1. **組裝一個機械手臂**
![](https://i.imgur.com/KfIdirw.jpg)
![](https://i.imgur.com/YC4Xkg0.jpg)

2. **使用 NXT programming 設計程式以操作機械手臂**
    - 使用 NXT 專屬傳輸線連接電腦
    - 安裝 [LEGO MINDSTORMS Educate NXT programming](https://education.lego.com/en-us/downloads/retiredproducts/nxt/software)
    ![](https://i.imgur.com/cqcOdmt.jpg)
    - 使用內建的程式方塊設計需要的功能（類似 Scratch）
    - 測量距離同時判斷物體距離，再進行各項動作
    ![](https://i.imgur.com/EnmBNxI.jpg)

    - 重置變數
    ![](https://i.imgur.com/aT3GywA.jpg)

3. **編寫python程式**
    - 引用套件pyautogui、os、shutil、time、paramiko
    
    - 開啟NXT programming 按鍵座標偵測
    
    - 開始寫程式，要知道PI的IP位置。

### 成品

![](https://i.imgur.com/ajCazHq.jpg)


## 未來展望

- 可以結合 hey google

## 參考資料


### 樹莓派紅外線感測安裝

- [樹莓派 Raspberry Pi 之人體紅外線感測器實作](http://hophd.com/raspberry-pi-sensor-infrared/)
- [[PIR] 簡易人體紅外線感應 (PIR) 模組測試電路](https://ruten-proteus.blogspot.com/2013/03/PIR-testing.html)
- [Home Notification using Telegram and Raspberry Pi](https://tutorial.cytron.io/2019/03/14/home-notification-using-telegram-raspberry-pi/)

### 紅外線感測送出提醒到 Telegram Bot
- [Home Notification using Telegram and Raspberry Pi](https://tutorial.cytron.io/2019/03/14/home-notification-using-telegram-raspberry-pi/)

### WebCam 連上樹莓派
- [Home Security using Raspberry Pi + Web Cam + PIR Sensor and Telegram Bot](https://www.techtalks.lk/blog/2017/9/home-security-using-raspberry-pi--web-cam--pir-sensor-and-telegram-bot)
- [在 Raspberry Pi 中使用 USB 網路攝影機（Webcam）照相](https://blog.gtwang.org/iot/raspberry-pi-usb-webcam/)

### NXT 射橡皮筋手臂設計

- [橡皮筋槍+電子發射系統](http://yushesnxt.blogspot.com/2015/01/2015129.html)
### Python ssh
- [paramiko](https://blog.csdn.net/yaningli/article/details/78223361)


## 工作分配

- **107213013 資管三 陳暐婷**
    - 寫 github
    - 樹莓派連接 WebCam
    - NXT 藍芽連線
- **107213024 資管三 王為棟**
    - 製作 NXT 機械手臂
    - NXT 藍芽連線
- **107213048 資管三 趙洸佑**
    - 製作 NXT 機械手臂
    - NXT programming
- **107213051 資管三 李畇彤 aka 茄仔🍆**
    - 寫 github
    - 製作樹莓派紅外線感測
- **107213055 資管三 邱品萍 aka 王嫂**
    - 建立 telegram bot
    - 樹莓派連接 WebCam
