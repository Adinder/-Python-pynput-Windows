import time
import sys
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController, Listener

# 初始化前台物理模拟控制器
mouse = MouseController()
keyboard = KeyboardController()

# 控制循环运行的状态标志位
running = True

def on_press(key):
    """全局键盘按键监听回调函数"""
    global running
    # 检测是否按下了 F12 键
    if key == Key.f12:
        print("\n[安全退出] 检测到按下 F12，正在停止脚本...")
        running = False
        return False  # 返回 False 可以自动停止当前 Listener 监听器

# 启动后台线程监听全局键盘事件
listener = Listener(on_press=on_press)
listener.start()

print("=== 物理/前台键鼠模拟脚本已启动 (pynput) ===")
print("提示：必须确保目标游戏/软件处于前台焦点状态！")
print("安全退出按键：任何时候按下 [ F12 ] 即可安全终止程序")
print("脚本将在 3 秒后开始执行，请切换到目标窗口...")
time.sleep(3)

try:
    while running:
        # 1. 模拟鼠标左键点击
        mouse.press(Button.left)
        time.sleep(0.05)
        mouse.release(Button.left)
        print("执行：[ SendInput ] 鼠标左键点击")
        
        # 将长间隔拆分为小段循环检查，确保按下 F12 后能秒级响应退出
        for _ in range(10):
            if not running: break
            time.sleep(0.1)

        if not running: break

        # 2. 模拟鼠标右键点击
        mouse.press(Button.right)
        time.sleep(0.05)
        mouse.release(Button.right)
        print("执行：[ SendInput ] 鼠标右键点击")
        
        for _ in range(10):
            if not running: break
            time.sleep(0.1)

        if not running: break

        # 3. 模拟空格键按下
        keyboard.press(Key.space)
        time.sleep(0.05)
        keyboard.release(Key.space)
        print("执行：[ SendInput ] 空格键按下")
        
        for _ in range(20):
            if not running: break
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\n[提示] 用户通过控制台 (Ctrl+C) 中断脚本。")

print("=== 脚本已完全安全退出 ===")
sys.exit()