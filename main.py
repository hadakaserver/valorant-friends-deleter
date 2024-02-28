import pyautogui as c
import time
import os
from colorama import Fore

ERROR = ("[" + Fore.RED + "-" + Fore.RESET +"] ")
SUCCESS = ("[" + Fore.GREEN + "+" + Fore.RESET +"] ")
INFO = ("[" + Fore.YELLOW + "+" + Fore.RESET +"] ")

print("""______    _                _       _      _      _            
|  ___|  (_)              | |     | |    | |    | |           
| |_ _ __ _  ___ _ __   __| |   __| | ___| | ___| |_ ___ _ __ 
|  _| '__| |/ _ \ '_ \ / _` |  / _` |/ _ \ |/ _ \ __/ _ \ '__|
| | | |  | |  __/ | | | (_| | | (_| |  __/ |  __/ ||  __/ |   
\_| |_|  |_|\___|_| |_|\__,_|  \__,_|\___|_|\___|\__\___|_|   
""")
print(f"{INFO}削除するフレンド数を入力してください…")
z = int(input())

print(f"{INFO}3秒後にフレンド削除処理を開始します。")
time.sleep(3)

i = 0

while i < z:
    c.moveTo(1900, 240)
    c.leftClick(1900, 240)
    c.rightClick(1900, 240)
    c.moveTo(1900, 360)
    c.leftClick(1900, 360)
    c.moveTo(800, 620)
    c.leftClick(800, 620)
    print(f"{ERROR}フレンド削除処理を行いました。")
    time.sleep(1.1)
    i += 1
    
else:
    print(f"{SUCCESS}指定された回数のフレンド削除処理を行いました。")
    os.system("pause")