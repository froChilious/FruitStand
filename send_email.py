from email.message import EmailMessage
import os, mimetypes
import smtplib

def generate_email(sender, recipient, subject, body, attachment = None):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    if attachment is not None:
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
    return message

def send_email(message):
    try:
        mail_server = smtplib.SMTP('localhost')
        mail_server.set_debuglevel(1)
        mail_server.send_message(message)
        return True
    except Exception as err:
        print(f'ERROR: Unable to send email: {err}')
        return False

        