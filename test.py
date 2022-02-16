# # Change the line below depending on whether you want the whole window
# # or just the client area. 
# #result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
# result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
# print(result)

# bmpinfo = saveBitMap.GetInfo()
# bmpstr = saveBitMap.GetBitmapBits(True)

# im = Image.frombuffer(
#     'RGB',
#     (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
#     bmpstr, 'raw', 'BGRX', 0, 1)

# win32gui.DeleteObject(saveBitMap.GetHandle())
# saveDC.DeleteDC()
# mfcDC.DeleteDC()
# win32gui.ReleaseDC(hwnd, hwndDC)

# if result == 1:
#     #PrintWindow Succeeded
#     im.save("test.png")
    
# import win32gui
# import win32ui
# import win32con
# from ctypes import windll
# import numpy as np
# from PIL import Image

# # w = 1920 # set this
# # h = 1080 # set this
# bmpfilenamename = "out.bmp" #set this

# hwnd = win32gui.FindWindow(None, "War Thunder")

# left, top, right, bot = win32gui.GetClientRect(hwnd)
# # left, top, right, bot = win32gui.GetWindowRect(hwnd)
# w = right - left
# h = bot - top

# wDC = win32gui.GetWindowDC(hwnd)
# dcObj=win32ui.CreateDCFromHandle(wDC)
# cDC=dcObj.CreateCompatibleDC()

# dataBitMap = win32ui.CreateBitmap()
# dataBitMap.CreateCompatibleBitmap(dcObj, w, h)

# # cDC.SelectObject(dataBitMap)

# # cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
# # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

# # image = np.array(dataBitMap)

# # # Free Resources
# # dcObj.DeleteDC()
# # cDC.DeleteDC()
# # win32gui.ReleaseDC(hwnd, wDC)
# # win32gui.DeleteObject(dataBitMap.GetHandle())

# cDC.SelectObject(dataBitMap)

# # Change the line below depending on whether you want the whole window
# # or just the client area. 
# #result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
# result = windll.user32.PrintWindow(hwnd, cDC.GetSafeHdc(), 0)
# print(result)

# bmpinfo = dataBitMap.GetInfo()
# bmpstr = dataBitMap.GetBitmapBits(True)

# im = Image.frombuffer(
#     'RGB',
#     (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
#     bmpstr, 'raw', 'BGRX', 0, 1)

# win32gui.DeleteObject(dataBitMap.GetHandle())
# cDC.DeleteDC()
# dcObj.DeleteDC()
# win32gui.ReleaseDC(hwnd, wDC)

# if result == 1:
#     #PrintWindow Succeeded
#     im.save("test.png")

import cv2
import numpy as np
from PIL import ImageGrab
import win32gui

# Detect the window with Tetris game
windows_list = []
toplist = []
def enum_win(hwnd, result):
    win_text = win32gui.GetWindowText(hwnd)
    windows_list.append((hwnd, win_text))
win32gui.EnumWindows(enum_win, toplist)
print(windows_list)
# Game handle
# game_hwnd = 0
# for (hwnd, win_text) in windows_list:
#     if "War Thunder" in win_text:
#         game_hwnd = hwnd
        
# # while True:
# position = win32gui.GetWindowRect(game_hwnd)
# # Take screenshot
# screenshot = ImageGrab.grab(position)
# screenshot = np.array(screenshot)
# screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
# # cv2.imshow("Screen", screenshot)
# cv2.imwrite('image.png',screenshot)