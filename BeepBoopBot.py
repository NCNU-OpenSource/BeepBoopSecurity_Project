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

# Save who need to notify
notifyTarget = list()

# BeepBoop Token
bot = telepot.Bot('1434178925:AAEC-3dYZ42QwSFEbir0_QfowlPrQ9shMRc')

def handle(msg):
    chat_id = msg['chat']['id']
    telegramText = msg['text']

    print('Message received from ' + str(chat_id))

    # 判斷指令為何，會對應到甚麼樣的動作
    if telegramText == '/start':
        bot.sendMessage(chat_id, 'Welcome to BeepBoop Notification')
        # When get start push in notify list
        if chat_id not in notifyTarget:
            notifyTarget.append(chat_id)
            print("Current notify list: " + str(notifyTarget))
    elif telegramText == '/attack':
        bot.sendMessage(chat_id, 'Attack!')
    elif telegramText == '/My':
        bot.sendMessage(chat_id, 'Welcome to home!')
    elif telegramText == '/exit':
        notifyTarget.remove(chat_id)
        bot.sendMessage(chat_id, 'Good Bye~')

# Callback function for PIR signal raise up
def captureWhenDetect(channel):
    print("Event call back")
    # Capture photo from webcam using shell
    call(["fswebcam", "image.jpg"])
    # Send message to everyone who subscribe ( 所有按過 start 的人)
    for singleChat in notifyTarget:
        bot.sendMessage(singleChat, "Some activity detected!")
        # 以 binary 進行讀取
        bot.sendPhoto(singleChat, open("image.jpg", "rb"))
# Registe event for PIR get signal rising (針對 PIR17 做事件偵測)
# GPIO.RISING 從 0 -> 1
# bouncetime : 每次事件要間隔多久才會又偵測
GPIO.add_event_detect(PIR, GPIO.RISING, bouncetime = 3000)
# 當 event 發生時，做 callback，執行captureWhenDetect
GPIO.add_event_callback(PIR, captureWhenDetect)

# Registe bot message handler
bot.message_loop(handle)

while True:
    time.sleep(1)