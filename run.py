#!/usr/bin/env python3
import os, requests

description_dir = '/home/student-01-d1a9ac6f5b91/supplier-data/descriptions/'
image_dir = '/home/student-01-d1a9ac6f5b91/supplier-data/descriptions/'

url = 'http://localhost/fruits/'
imap = ['name','weight','description','image_name']

def get_fruit_info(file_dir, image_dir, imap):
    fruit_info = []
    for file in os.listdir(file_dir):
        if file.split('.')[-1] == 'txt':
            fruit = {}
            with open(os.path.join(file_dir,file),'r') as f:
                for i,line in enumerate(f.readlines()):
                    if i == 1:
                        info = line.strip().split()[0]
                    else:
                        info = line.strip()
                    if i < 3:
                        fruit[imap[i]] = info
                image_file = os.path.join(image_dir,'{}{}'.format(file.split('.')[0],'.jpeg'))
                fruit[imap[3]] = image_file
            fruit_info.append(fruit)
    return fruit_info

def upload_descriptions(url, fruit_data):
    for fruit in fruit_data:
        try:
            response = requests.post(url,data=fruit)
        except Exception as err:
            print(err)
    

fruit_data = get_fruit_info(description_dir, image_dir, imap)
print(fruit_data[0])
upload_descriptions(url,fruit_data)
