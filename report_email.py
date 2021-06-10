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
        fruit_body = '{}{}<br></br>{}<br></br><br></br>'.format(fruit_body,fruit['name'],fruit['weight'])
    return report_title, fruit_body

def main():
    descriptions_dir = '/home/student/supplier-data/descriptions/'
    url = 'http://localhost/fruits/' # not an actual url
    imap = ['name','weight','description','image_name']

    fruit_data = get_fruit_info(descriptions_dir, imap)
    title, paragraph = get_fruit_report_parts(fruit_data)

    reports.generate_report('processed.pdf', title, paragraph)

if __name__ == '__main__':
    main()
