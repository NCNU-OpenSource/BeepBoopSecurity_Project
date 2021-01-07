# BeepBoopSecurity_Project

## 動機發想

- 最一開始我們希望可以做一個**樂高殺手**，顧名思義就是用樂高做的殺手，藏在 MOLI 的角落攻擊他人，把樂高積木射到目標的前面一點點，讓目標採到，聽起來就超好玩的。
- 但 <font color=#800000>邱呱呱 aka 王嫂</font> 覺得實用性不足，於是我們就決定幫樂高殺手招募同伴，感應器殺手跟照相機殺手就來了，他們是一支要保家衛國的隊伍，如果有人想要強行闖入你家的話，就會拍照傳給使用者，讓使用者決定要不要攻擊，這樣就不會有無辜的人受害了，我們樂高殺手是正義的化身。
-  <font color=#800000>但我們還是</font> 覺得不滿足，於是我們決定把樂高殺手再進化，因為樂高其實蠻貴的，所以我們把子彈換成橡皮筋，超聰明的！
- 試想你今天是壞人，想要闖進無辜百姓的家裡偷東西，這時突然有一個東西一直射橡皮筋，勢必會喚起小時候被爸爸拿橡皮筋修理的恐懼，保家衛國任務達成！


## 功能

- 當有可疑人士在家門口徘徊或是靠近時，會藉由telegram bot發送可疑人士的照片給屋主，使屋主能夠隨時監控家的安全
- 屋主可以針對可疑人士發動攻擊(射橡皮筋)

## 時間

### 12/18 前 

- 確定主題
- 樹莓派連接成功，設定完成
- 找齊需要的設備

### 12/23 
- 完成 telegram bot 基本設定

### 12/25 開心的聖誕節

- 東洲最棒

### 12/30

- 完成紅外線偵測的硬體架構與程式
- 完成影像辨識的硬體架構與程式
- 完成機械手臂的製作

### 1/1 開心的跨年

- 居酒屋好吃

### 1/4 

- 整合 NXT & Raspberry pi

## 整體架構

### 硬體架構
- Raspberry Pi
- LEGO MINDSTORMS NXT
- Webcam
- 紅外線感測模組

### 軟體架構
- Telegram bot
- Python Programming
- NXT Programming

## 先備條件與設備
### Raspberry Pi
- Raspberry Pi 3 

### 紅外線感測模組
- 樹莓派紅外線感測器
    - IR Infrared PIR Motion Sensor
- 杜邦線（公母、母母）
- 電阻
- 麵包板

### Webcam
- SpotCam USB-CAM01 高畫質 FHD 視訊攝影機
- [PChome 購買連結](https://24h.m.pchome.com.tw/prod/DCAS4U-A900ANFN2)

### LEGO MINDSTORMS NXT 第二代
- 超音波感測器 * 1
- 馬達 * 3
- 樂高零件

## 硬體架構設計

### Raspberry Pi

#### 安裝套件

- **python package index** : 在 raspberry pi 上安裝 python 的套件管理
```python=
sudo apt-get install python-pip
```
- **telepot** : 整合所有 telegram API，方便開發者使用的 python packge，通過安裝 telepot 我們可以直接在 python 中使用 telegram API 的功能
```python=
sudo pip install telepot
```
- **GPIO** : 可以讓我們藉由程式與我們的裝置進行通訊，可以自由地控制與使用裝置

```python=
sudo pip install RPi.GPIO
```
- **DateTime** : python 的模組，主要負責日期和時間的解析、格式化和計算。
```python=
sudo pip install DateTime
```

### 紅外線感測模組

![](https://i.imgur.com/zqmtaaT.jpg)

- 紅外線感測器有三條可以外接的線，分別是 5V、資料線、GND 接地線
- 左邊的是 VCC，要接到樹莓派的 5V
- 中間的是資料線，可以接到任一 GPIO 接腳
- 右邊是 GND 接地線，必須接到樹莓派的接地線接腳上

![](https://www.raspberrypi.com.tw/wp-content/uploads/2014/09/connect-serial-to-raspberry-pi-model-b-plus.png)


- 以下是我們這次的接線
    - 5V（墨綠線）
    - Ground（紫線）
    - GPIO17（紅線）

![](https://1.bp.blogspot.com/-a61fT_GHtEc/UUU8x60ygGI/AAAAAAAACHQ/krkQR3n5GEQ/s1600/function-test_bb-blog.resize.jpg)
![](https://i.imgur.com/hBooB81.jpg)

### Webcam
- 直接買可支援 USB 的 webcam
- 將 Webcam 的 USB 接入 Raspberry Pi 即可
![](https://i.imgur.com/0umeUXd.jpg)

### LEGO MINDSTORMS NXT
#### 什麼是 NXT？

- 這很難解釋，要看你是問哪個 NXT
- [這個 NXT](https://zh.wikipedia.org/wiki/WWE_NXT)
- [那個 NXT](https://zh.wikipedia.org/wiki/%E6%A8%82%E9%AB%98Mindstorms_NXT)

#### 組裝一個機械手臂

![](https://i.imgur.com/KfIdirw.jpg)
![](https://i.imgur.com/YC4Xkg0.jpg)

#### 成品!!!

![](https://i.imgur.com/ajCazHq.jpg)

#### 最後大合體

![](https://i.imgur.com/07aorWo.jpg)
![](https://i.imgur.com/SSlxhbB.jpg)
![](https://i.imgur.com/bejrFET.jpg)
![](https://i.imgur.com/4BTY2pO.jpg)


## 軟體系統架構

- Telegram Bot
- Python Programming
- NXT Programming

### 建立 telegram bot
1. 搜尋 `BotFather`（點選有藍勾勾的那個）

     ![](https://i.imgur.com/5aSNVAU.jpg)
     
2. 下指令 : `/start`
3. 下指令 : `/newbot`
4. 幫自己的機器人取個名字 !
5. 命名 id，要以`_bot`結尾（id名不可重複）

![](https://i.imgur.com/fatqGLk.png)

6. 系統會給你一串 token（要記起來!!!以後要加在程式碼中的）

 ![](https://i.imgur.com/gEzzqDW.png)
 
  - token 要放進在 TOKEN 裡，記得不能洩漏不然會被亂改!
    
   ![](https://i.imgur.com/RHdeLZj.png)

### 指令介紹
1. `/start ` : 開始訂閱保全偵測系統

![](https://i.imgur.com/Ml9UI5o.jpg)

2. `/attack` : 對可疑人士進行攻擊

![](https://i.imgur.com/yImZqk7.png)

3. `/stop` : 停止攻擊

![](https://i.imgur.com/TBCBh3E.png)

4. `/isme` : 告訴保全機器人，你是屋主不是可疑人士!

![](https://i.imgur.com/Z1fg6QC.png)

5. `/exit` : 取消訂閱保全偵測系統

![](https://i.imgur.com/EjbvFZu.png)


### NXT Programming
#### 使用 NXT programming 設計程式以操作機械手臂
- 使用 NXT 專屬傳輸線連接電腦
- 安裝 [LEGO MINDSTORMS Educate NXT programming](https://education.lego.com/en-us/downloads/retiredproducts/nxt/software)
  ![](https://i.imgur.com/cqcOdmt.jpg)
  
- 使用內建的程式方塊設計需要的功能
- 測量距離同時判斷物體距離，再進行各項動作
  ![](https://i.imgur.com/EnmBNxI.jpg)
  
- 重置變數
  ![](https://i.imgur.com/aT3GywA.jpg)

## 最大的困難

- 機械手臂不如預期可以透過 raspberry pi 直接使用 python 控制，因為 python 目前已無在維護 NXT 可使用的藍芽套件

## 未來展望

1. telegram bot 介面可以再優化，變得更人性化(例如 : 把指令用成按鈕)
2. 攻擊變成全自動化
3. 可以設定服務開啟與關閉的時間
4. 可以結合 hey google 智慧語音

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


## 工作分配

- **107213013 資管三 陳暐婷**
    - 寫 github
    - 紅外線感測
    - 製作 PPT
- **107213024 資管三 王為棟**
    - 製作 NXT 機械手臂
    - 程式註冊為服務
- **107213048 資管三 趙洸佑**
    - 製作 NXT 機械手臂
    - NXT programming
    - 製作 PPT
- **107213051 資管三 李畇彤**
    - 寫 github
    - 製作樹莓派紅外線感測
    - 製作 PPT
- **107213055 資管三 邱品萍**
    - 建立 telegram bot
    - 樹莓派連接 WebCam
    - Python Programming
    - 寫 Github
    - 製作 PPT
    
 
