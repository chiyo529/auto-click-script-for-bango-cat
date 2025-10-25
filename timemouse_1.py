import pyautogui
import time

# --- 脚本设置 ---
# 【新】设置您希望点击的 X, Y 坐标
CLICK_X = 1800
CLICK_Y = 520
CLICK_X_1 = 1885
CLICK_Y_1 = 490
CLICK_X_2 = 1717
CLICK_Y_2 = 490
CLICK_X_3 = 100
CLICK_Y_3 = 1048

delay_before_start = 3      # 脚本开始前的准备时间（秒）
run_duration_minutes = 240     # 您希望脚本运行的总时长（分钟）
run_duration_seconds = run_duration_minutes * 60 # 转换为秒

click_duration = 0.2      # 鼠标按下 和 弹起 之间的间隔（秒）
delay_between_clicks = 0.2 # 两次点击间的延迟（秒）
delay_between_clicks_2 = 1800

# --- 准备 ---
print(f"!!! 警告：pyautogui.PAUSE 已设为 0（默认值 0.1）!!!")
print(f"!!! 警告：最小化所有窗口!!!")
pyautogui.PAUSE = 0 # 仍然需要这个来覆盖默认的 0.1s 暂停

print(f"脚本将在 {delay_before_start} 秒后开始...")
print(f"脚本将持续运行 {run_duration_minutes} 分钟。")
print(f"所有的点击将发生在坐标: (X={CLICK_X}, Y={CLICK_Y}) 和 (X={CLICK_X_1}, Y={CLICK_Y_1})")
print("（请记住，随时可以将鼠标移至屏幕角落来强制停止脚本）")
time.sleep(delay_before_start)
print("--------------------")
print("模拟开始！")

# 记录开始时间
start_time = time.time()
end_time_target = start_time + run_duration_seconds 
click_count = 0  

try:
    while time.time() < end_time_target:
        
        # 【核心修改】在指定坐标执行点击
        pyautogui.mouseDown(x=CLICK_X, y=CLICK_Y)
        time.sleep(click_duration)
        pyautogui.mouseUp(x=CLICK_X, y=CLICK_Y)
        time.sleep(delay_between_clicks)
        pyautogui.mouseDown(x=CLICK_X_1, y=CLICK_Y_1)
        time.sleep(click_duration)
        pyautogui.mouseUp(x=CLICK_X_1, y=CLICK_Y_1)
        time.sleep(delay_between_clicks)
        pyautogui.mouseDown(x=CLICK_X_2, y=CLICK_Y_2)
        time.sleep(click_duration)
        pyautogui.mouseUp(x=CLICK_X_2, y=CLICK_Y_2)
        time.sleep(delay_between_clicks)
        pyautogui.mouseDown(x=CLICK_X_3, y=CLICK_Y_3)
        time.sleep(click_duration)
        pyautogui.mouseUp(x=CLICK_X_3, y=CLICK_Y_3)
        time.sleep(delay_between_clicks)
        
        click_count += 4

except pyautogui.FailSafeException:
    print("安全保护启动！脚本已被强制停止。")

finally:
    # 记录实际结束时间
    end_time_actual = time.time()
    
    # --- 统计输出 ---
    print("--------------------")
    if end_time_actual < end_time_target:
        print("模拟被手动停止！")
    else:
        print("模拟完成（已达到设定的时间）！")
    
    total_duration = end_time_actual - start_time
    
    print(f"\n--- 运行时间统计 ---")
    print(f"实际运行时间: {total_duration / 3600:.2f} 小时 ({total_duration:.0f} 秒)")
    print(f"总共模拟点击次数: {click_count}")
    
    if total_duration > 0:
        clicks_per_second = click_count / total_duration
        print(f"平均每秒点击次数 (CPS): {clicks_per_second:.2f}")