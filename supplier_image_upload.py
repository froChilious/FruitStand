#!/usr/bin/env python3
import os, requests

def supplier_image_upload(image_dir, url, img_type = 'jpeg'):
    for i, file in enumerate(os.listdir(image_dir)):
        if file.split('.')[-1] == img_type:
            image_path = os.path.join(image_dir,file)
            with open(image_path,'rb') as opened:
                response = requests.post(url,files={'file': opened})

def main():
    image_dir = '/home/student-03-32beb94feb5b/images/'
    url = 'http://localhost/upload/' # not an actual url

    supplier_image_upload(image_dir, url)

if __name__ == '__main__':
    main()
