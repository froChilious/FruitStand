from email.message import EmailMessage
import os, mimetypes
import smtplib

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
    