import pyautogui
import os 
import shutil
import time
import paramiko

def ssh_scp_get(ip, port, user, password, remote_file, local_file): 
    ssh = paramiko.SSHClient() # 建立SSH
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, 'username', password) # 進行ssh連接 
    a = ssh.exec_command('date')
    stdin, stdout, stderr = a 
    #print(stdout.read())
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport()) # 建立安全文件傳送協議
    sftp = ssh.open_sftp() # 執行這個服務
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
