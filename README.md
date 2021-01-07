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

### Python Programming
```python=
import telepot
import RPi.GPIO as GPIO
import time
import datetime
from telepot.loop import MessageLoop
from subprocess import call

PIR = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

# 儲存誰有訂閱通知
notifyTarget = list()

# BeepBoopBot Token
bot = telepot.Bot('1434178925:AAEC-3dYZ42QwSFEbir0_QfowlPrQ9shMRc')

checkisme = False

def handle(msg):
    global checkisme
    chat_id = msg['chat']['id']
    telegramText = msg['text']
    print('Message received from ' + str(chat_id))
    # 開始連線，向 bot 訂閱通知
    if telegramText == '/start':
        bot.sendMessage(chat_id, 'Welcome to BeepBoop Notification')
        # 把所有向 bot 訂閱的 chat_id 都加入發送清單
        if chat_id not in notifyTarget:
            notifyTarget.append(chat_id)
            print("Current notify list: " + str(notifyTarget))
    # 對 NXT 傳送攻擊指令
    elif telegramText == '/attack':
        bot.sendMessage(chat_id, 'Attack!')
        f = open('124.txt','w+')
        f.write('/attack')
        f.close()
    # 對 NXT 下達停止攻擊
    elif telegramText == '/stop':
        bot.sendMessage(chat_id, 'Stop Attack!')
        f = open('124.txt','w+')
        f.write('/stop')
        f.close()
    # 告訴 bot 短時間內如果偵測到不需要通知 ( 因為是屋主 )
    elif telegramText == '/isme':
        bot.sendMessage(chat_id, 'Welcome home!')
        checkisme = True
        for singleChat in notifyTarget:
            bot.sendMessage(singleChat, 'Stop detecting for 30 second, Safe and Sound')
    # 結束連線
    elif telegramText == '/exit':
        notifyTarget.remove(chat_id)
        bot.sendMessage(chat_id, 'Good Bye~')

# 當偵測到人執行通知與拍照
def captureWhenDetect(channel):
    global checkisme
    # 檢查目前偵測到的可疑人士，是否為屋主
    if (checkisme == True):
        checkisme = False
        # 停止拍照與通知屋主
        time.sleep(30)
        # 向所有訂閱 bot 的人都發送「繼續偵測」的訊息
        for singleChat in notifyTarget:
            bot.sendMessage(singleChat, "Continue detected!")
        return
    print("Event call back")
    # 使用 shell 進行 webcam 拍照
    call(["fswebcam", "image.jpg"])
    # 向所有訂閱 bot 的人都發送「偵測到可疑人士」的訊息 & 照片
    for singleChat in notifyTarget:
        bot.sendMessage(singleChat, "Some activity detected!")
        bot.sendPhoto(singleChat, open("image.jpg", "rb"))

# 針對 PIR17 進行事件偵測
# GPIO.RISING 從低電壓 -> 高電壓 (偵測到人了)
# bouncetime : 每次事件要間隔多久才會又偵測
GPIO.add_event_detect(PIR, GPIO.RISING, bouncetime = 3000)
# 當 event 發生時，做 callback(回調函式)，執行 captureWhenDetect
GPIO.add_event_callback(PIR, captureWhenDetect)

# Bot 收到訊息後執行 handle
bot.message_loop(handle)

while True:
    time.sleep(1)
```
- NXT 連接 telegram bot
```python=
import pyautogui
import os 
import shutil
import time
import paramiko

def ssh_scp_get(ip, port, user, password, remote_file, local_file): 
    ssh = paramiko.SSHClient() # 建立SSH
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 允許連接不在known_hosts文件上的主機
    ssh.connect(ip, 22, 'username', password) # 進行ssh連接 
    a = ssh.exec_command('date') # 執行命令
    stdin, stdout, stderr = a  
    print(stdout.read())
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport()) # 建立SFTP服務
    sftp = ssh.open_sftp() # 在ssh server 上啟用 sftp session
    sftp.get(remote_file, local_file) # 複製遠端檔案
    
ip = str(input("請輸入IP位置:"))
password = 'password'
remote_file = "Remote file path" # 遠端的資料路徑
local_file = "local file path " # 本地要放置的路徑

print("ready")
time.sleep(5)
print("go")
turn = 0

while True:
    ssh_scp_get(ip,22,"pi",password,remote_file,local_file) 
    if not os.path.isfile(local_file):
        continue
    shutil.copyfile(local_file, r"Other New file path") # 複製新的文件
    f = open(r"New file path", "r") 
    mes = f.readline()
    if (mes == "/attack" and turn == 0):
        pyautogui.click(1808, 795, button='left')
        turn += 1
    elif (mes == "/stop" and turn == 1):
        pyautogui.click(1872, 850, button='left')
        turn -= 1
    else:
        time.sleep(2)
```
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
    
