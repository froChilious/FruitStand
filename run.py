#!/usr/bin/env python3
import os, requests

def get_fruit_info(description_dir, image_dir, imap):
    fruit_info = []
    for file in os.listdir(description_dir):
        if file.split('.')[-1] == 'txt':
            fruit = {}
            with open(os.path.join(description_dir,file),'r') as f:
                for i,line in enumerate(f.readlines()):
                    if i == 1:
                        info = line.strip().split()[0]
                    else:
                        info = line.strip()
                    if i < 3:
                        fruit[imap[i]] = info
                base_file_name = file.split('.')[0]
                image_file = '{}{}'.format(base_file_name,'.jpeg')
                fruit[imap[3]] = image_file
            fruit_info.append(fruit)
    return fruit_info

def upload_descriptions(url, fruit_data):
    for fruit in fruit_data:
        try:
            response = requests.post(url,data=fruit)
        except Exception as err:
            print(err)
    
def main():    
    description_dir = '/home/student-03-32beb94feb5b/supplier-data/descriptions/'
    image_dir = '/home/student-03-32beb94feb5b/supplier-data/images/'
    url = 'http://localhost/fruits/'
    imap = ['name','weight','description','image_name']

    fruit_data = get_fruit_info(description_dir, image_dir, imap)
    upload_descriptions(url,fruit_data)

if __name__ == '__main__':
    main()
