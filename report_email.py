#!/usr/bin/env python3
import datetime, os
import reports
import emails

def get_fruit_info(file_dir, imap):
    fruit_info = []
    for file in os.listdir(file_dir):
        if file.split('.')[-1] == 'txt':
            fruit = {}
            with open(os.path.join(file_dir,file),'r') as f:
                for i,line in enumerate(f.readlines()):
                    fruit[imap[i]] = line.strip()
            fruit_info.append(fruit)
    return fruit_info

def get_fruit_report_parts(fruit_data):
    today = datetime.datetime.today().strftime('%B %d, %Y')
    report_title = "Processed Update on {}".format(today)
    fruit_body = ''
    for fruit in fruit_data:
        fruit_body = '{}<br></br>name: {}<br></br>weight: {}'.format(fruit_body,fruit['name'],fruit['weight'])
    return report_title, fruit_body

def main():
    user = 'student-03-32beb94feb5b'
    descriptions_dir = '/home/{}/supplier-data/descriptions/'.format(user)
    url = 'http://localhost/fruits/' # not an actual url
    imap = ['name','weight','description','image_name']
    # Get the data from the files and make a dictionary
    fruit_data = get_fruit_info(descriptions_dir, imap)
    title, paragraph = get_fruit_report_parts(fruit_data)
    # Generate the PDF report
    report_pdf = 'processed.pdf'
    reports.generate_report(report_pdf, title, paragraph)
    # Generate and send the email
    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(user)
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate_email(sender,recipient,subject,body,report_pdf)

if __name__ == '__main__':
    main()
