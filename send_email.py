from email.message import EmailMessage
import os, mimetypes
import smtplib

import smtplib
fromMy = 'jhoovis@att.net' # fun-fact: from is a keyword in python, you can't use it as variable, did abyone check if this code even works?
to  = 'jhoovis@yahoo.com'
subj='TheSubject'
date='2/1/2010'
message_text='Hello Or any thing you want to send'

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromMy, to, subj, date, message_text )

username = str('jhoovis@yahoo.com')  
password = str('1fr0Ch1l10us')  

try :
    server = smtplib.SMTP("smtp.mail.yahoo.com",587)
    server.login(username,password)
    server.sendmail(fromMy, to,msg)
    server.quit()    
    print 'ok the email has sent '
except :
    print 'can\'t send the Email'


message = EmailMessage()
try:
    mail_server = smtplib.SMTP('localhost')
except ConnectionRefusedError:
    print('Unable to connect to localhost.')

recipient = 'jhoovis@att.net'
sender = 'frochilious@gmail.com'
body = """
hey there,

I'm learning to send emails from python, good times!

Thanks for listening,
fro
"""

def create_email(sender, recipient, subject, body, attachment = ''):
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    if attachment != '':
        try:
            attachment_path = attachment
            attachment_file = os.path.basename(attachment_path)
            mime_type,_ = mimetypes.guess_type(attachment_path)
            mime_type, mime_subtype = mime_type.split('/',1)
            with open(attachment, 'rb') as ap:
                message.add_attachment( ap.read(),
                                        maintype=mime_type,
                                        subtype=mime_subtype,
                                        filename=os.path.basename(attachment_path)
                                        )
        except Exception as err:
            print(f'ERROR: Unable to attach the file {attachment} with error msg:\n{err}.')
    