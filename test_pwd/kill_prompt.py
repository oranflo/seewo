# coding: utf-8
import win32api, win32gui, win32con

while True:
    try:
        hwnd3 = win32gui.FindWindow("#32770", "提示")
        if hwnd3:
            win32api.SendMessage(hwnd3, win32con.WM_CLOSE, None, 0) 
    except:
        pass