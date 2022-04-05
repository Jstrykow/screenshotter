import smtplib
from time import sleep

smpt_server = 'smtp.poczta.onet.pl'
smtp_port = 465 # 587
smtp_acct = 'becyp71@op.pl'
smtp_password = 'SlavaUkrainie69'
emails  =  ['becyp68@op.pl','becyp69@op.pl', 'becyp70@op.pl', "becyp71@op.pl", "becyp72@op.pl"]
# tgt_accts
# as a source it is require not as save as gmail befose it ned to be login on computer

def plain_email(email, subject, contents):
    print(f"Prepare mail from {email} sent to")
    mailobj = smtplib.SMTP( 'smtp.poczta.onet.pl', 587)
    mailobj.ehlo()
    mailobj.starttls()
    mailobj.login(email, "SlavaUkrainie69")
    msg = f"Subject: {subject} \n\n {contents}"
   
    mailobj.sendmail(email, 'vskibicka@gmail.com', msg)
    print(f"plain mail from {email} sent to")
    mailobj.quit()

for email in emails:
    plain_email(email, 'Kocham', 'Ciebie!')
    sleep(3)