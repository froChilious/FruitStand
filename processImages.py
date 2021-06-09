#!/usr/bin/env python3

import os, requests

image_dir = '/home/student/images'
url = 'http://localhost/upload' # not an actual url

def upload_all_image_files(image_dir, url, img_type = 'jpeg'):
    for i, file in enumerate(os.listdir(image_dir)):
        print(file.split('.'))
        if file.split('.')[1] == img_type:
            print(file)
            images = {}
            image_path = os.path.join(image_dir,file)
            with open(image_path,'rb') as opened:
                response = requests.post(url,files={'file': opened})

