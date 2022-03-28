from email import message_from_binary_file
import smtplib
import time


smpt_server = 'smtp.gmail.com'
smtp_port = 465
smtp_acct = 'becyp2137@gmail.com'
smtp_password = 'SlavaUkrainie69'
tgt_accts = ['becyp2137@gmail.com', 'becyp69@op.pl']

# as a source it is require not as save as gmail befose it ned to be login on computer

def plain_email(subject, contents):
    mailobj = smtplib.SMTP('smtp.gmail.com',587)
    mailobj.ehlo()
    mailobj.starttls()
    mailobj.login('becyp2137@gmail.com','SlavaUkrainie69')
    msg = f"Subject: {subject} \n\n {contents}"
    print(msg)
    mailobj.sendmail(smtp_acct, smtp_acct, msg)
    mailobj.quit()


plain_email('Widomosc tekstowa', 'Atak o swicie')
