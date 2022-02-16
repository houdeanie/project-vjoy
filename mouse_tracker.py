import pyautogui

width, height  = pyautogui.size()
mid_x = width//2
mid_y = height//2

running = True
while running:
    x, y = pyautogui.position()
    dev_x = x - mid_x
    dev_y = mid_y - y
    print("deviation: ", "x ", dev_x, "y ", dev_y)