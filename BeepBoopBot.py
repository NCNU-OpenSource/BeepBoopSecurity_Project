import telepot
import RPi.GPIO as GPIO
import time
import datetime
from telepot.loop import MessageLoop
from subprocess import call
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

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
        NXT(telegramText)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='🐸', callback_data="/stop")],
                ])
        bot.sendMessage(chat_id, 'Attacking!', reply_markup=keyboard, )
    # 對 NXT 下達停止攻擊
    elif telegramText == '/stop':
        bot.sendMessage(chat_id, 'Stop Attack!')
        NXT(telegramText)
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

def NXT(command):
    f = open('124.txt','w+')
    f.write(command)
    f.close()

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
        bot.sendPhoto(singleChat, open("image.jpg", "rb"))
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Attack', callback_data='/attack')],
               ])
        bot.sendMessage(singleChat, "Some actitiy detected!", reply_markup=keyboard)        

# 針對 PIR17 進行事件偵測
# GPIO.RISING 從低電壓 -> 高電壓 (偵測到人了)
# bouncetime : 每次事件要間隔多久才會又偵測
GPIO.add_event_detect(PIR, GPIO.RISING, bouncetime = 3000)
# 當 event 發生時，做 callback(回調函式)，執行 captureWhenDetect
GPIO.add_event_callback(PIR, captureWhenDetect)

# 按了 btn 就會自己去 call
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    bot.answerCallbackQuery(query_id, query_data)
    if (query_data == '/attack'):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                       [InlineKeyboardButton(text='Stop', callback_data="/stop")],
                    ])
        bot.sendMessage(from_id, 'Attacking!', reply_markup=keyboard, )
    elif (query_data == '/stop'):
        bot.sendMessage(from_id, 'Stop!')
    NXT(query_data)

# Bot 收到訊息後執行 handle
bot.message_loop({'chat': handle, 'callback_query': on_callback_query})

while True:
    time.sleep(1)
