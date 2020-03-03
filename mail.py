import os, smtplib, ssl, getpass
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders as Encoders
import getpass
import json
from decrypt import *
import os
port = 465

with open(r'auth/key_user.txt', 'r') as readfile:
    key_user = json.load(readfile)
with open(r'auth/user.txt', 'r') as readfile:
    user = json.load(readfile)
with open(r'auth/key_password.txt', 'r') as readfile:
    key_panda = json.load(readfile)
with open(r'auth/password.txt', 'r') as readfile:
    panda = json.load(readfile)

def send_mail(username, password, from_addr, to_addrs, msg):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port,context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr, to_addrs, msg.as_string())


def mailto(email_address):
    username = decrypt(eval(user),eval(key_user)).decode("utf-8")
    password  = decrypt(eval(panda),eval(key_panda)).decode("utf-8") 
    fromaddr = username
    Body =   """<!DOCTYPE html>
                <html>
                <head>
                <style>
                body {
                        color: red;
                }
                h4 {
                        color: #1E162F;
                        font-size: 20px;
                }
                h5 {
                        color: rgb(0,0,255);
                        font-size: 15px;
                }
                
                p {
                        color: rgb(0,0,255)
                }
                </style>
                </head>
                <body>
                 <h4> Decoded </h4>
                 
                </body>
                </html>
                """
    
    
    Body += u'<h5> Hi {name},</h5>'.format(name=email_address.split('@')[0])           

    msg = MIMEMultipart()
    Mail_Body=MIMEText(Body, 'html')
    msg.attach(Mail_Body)
    msg['From'] = username
    msg['To'] = email_address
    msg['Subject'] = "Decoded"
    
    send_mail(username=username, password=password, from_addr=fromaddr, to_addrs=email_address, msg=msg)
