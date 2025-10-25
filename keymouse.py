import pyautogui
import time
import random  # <--- 新增：导入 random 模块

# --- 脚本设置 ---
CLICK_X = 1800
CLICK_Y = 520
CLICK_X_1 = 1885
CLICK_Y_1 = 490
CLICK_X_2 = 1717
CLICK_Y_2 = 490
CLICK_X_3 = 100
CLICK_Y_3 = 1048

delay_before_start = 3
run_duration_minutes = 240
run_duration_seconds = run_duration_minutes * 60

click_duration = 0.2
delay_between_clicks = 0.3
delay_between_clicks_2 = 1800  # 30分钟的长循环等待

# <--- 新增：定义一组“安全”的按键列表 ---
# 这些按键通常不会在游戏中或应用中触发严重的操作
# 'f13' 到 'f24' 是非常好的选择，因为它们在标准键盘上不存在
SAFE_KEYS = ['f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20',
             'f21', 'f22', 'f23', 'f24']

# --- 准备 ---
print(f"!!! 警告：pyautogui.PAUSE 已设为 0（默认值 0.1）!!!")
print(f"!!! 警告：最小化所有窗口!!!")
pyautogui.PAUSE = 0

print(f"脚本将在 {delay_before_start} 秒后开始...")
print(f"脚本将持续运行 {run_duration_minutes} 分钟。")
print(f"点击坐标: (X={CLICK_X}, Y={CLICK_Y}), ... (共4个)")
print(f"每次点击循环后，将等待 30 分钟，期间伴随随机按键。")
print("（请记住，随时可以将鼠标移至屏幕角落来强制停止脚本）")

# <--- 修改：使用 pyautogui.sleep() 保证安全机制有效 ---
pyautogui.sleep(delay_before_start)
print("--------------------")
print("模拟开始！")

start_time = time.time()
end_time_target = start_time + run_duration_seconds
click_count = 0

# ... (脚本前面的设置部分保持不变) ...

try:
    while time.time() < end_time_target:
        
        # --- 1. 鼠标点击部分 (已修改为使用 pyautogui.sleep) ---
        #print(f"[{time.ctime()}] 执行 4 次点击...")
        #pyautogui.mouseDown(x=CLICK_X, y=CLICK_Y)
        #pyautogui.sleep(click_duration)
        #pyautogui.mouseUp(x=CLICK_X, y=CLICK_Y)
        #pyautogui.sleep(delay_between_clicks)
        
        pyautogui.mouseDown(x=CLICK_X_1, y=CLICK_Y_1)
        pyautogui.sleep(click_duration)
        pyautogui.mouseUp(x=CLICK_X_1, y=CLICK_Y_1)
        pyautogui.sleep(delay_between_clicks)
        
        pyautogui.mouseDown(x=CLICK_X_2, y=CLICK_Y_2)
        pyautogui.sleep(click_duration)
        pyautogui.mouseUp(x=CLICK_X_2, y=CLICK_Y_2)
        pyautogui.sleep(delay_between_clicks)
        
        pyautogui.mouseDown(x=CLICK_X_3, y=CLICK_Y_3)
        pyautogui.sleep(click_duration)
        pyautogui.mouseUp(x=CLICK_X_3, y=CLICK_Y_3)
        
        
        

        # --- 2. 智能等待 30 分钟 (带随机按键) ---
        
        wait_loop_start_time = time.time()
        wait_loop_end_target = wait_loop_start_time + delay_between_clicks_2
        
        print(f"    -> 开始 30 分钟的长等待 (直到 {time.ctime(wait_loop_end_target)})...")
        while True:
            current_time = time.time()
            
            if current_time >= wait_loop_end_target:
                print("    -> 30 分钟等待结束。")
                break 
                
            if current_time >= end_time_target:
                print("    -> 总运行时间已到，提前结束长等待。")
                break 
            
            random_wait_interval = random.uniform(0.3, 1.5)
            
            time_remaining_in_wait = wait_loop_end_target - current_time
            time_remaining_in_script = end_time_target - current_time
            
            sleep_duration = min(random_wait_interval, 
                                 time_remaining_in_wait, 
                                 time_remaining_in_script)

            if sleep_duration <= 0:
                break
            
            pyautogui.sleep(sleep_duration) 
            
            if time.time() >= wait_loop_end_target or time.time() >= end_time_target:
                break
                
            # --- 【这里是修改的部分】 ---
            # 执行随机按键（按下 -> 0.1s -> 弹起）
            random_key = random.choice(SAFE_KEYS)
            
            
            pyautogui.keyDown(random_key)
            pyautogui.sleep(0.1)  # <--- 你要求的 0.1s 间隔
            pyautogui.keyUp(random_key)
            # --- 【修改结束】 ---
            
        if time.time() >= end_time_target:
            print("    -> 总运行时间已到，结束主循环。")
            break 

except pyautogui.FailSafeException:
    print("安全保护启动！脚本已被强制停止。")

finally:
    # --- (这部分和之前一样，无需改动) ---
    end_time_actual = time.time()
    
    print("--------------------")
    if end_time_actual < end_time_target - 1:
        print("模拟被手动停止！")
    else:
        print("模拟完成（已达到设定的时间）！")
    
    total_duration = end_time_actual - start_time
    
    print(f"\n--- 运行时间统计 ---")
    print(f"实际运行时间: {total_duration / 3600:.2f} 小时 ({total_duration:.0f} 秒)")