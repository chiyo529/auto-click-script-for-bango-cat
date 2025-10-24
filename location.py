import pyautogui
import time
print("将鼠标移动到你希望点击的位置，5秒后将显示坐标...")
print("按 Ctrl+C 退出")
try:
    while True:
        time.sleep(5)
        # 获取并打印当前鼠标光标的坐标
        print(pyautogui.position()) 
except KeyboardInterrupt:
    print("\n已退出。")