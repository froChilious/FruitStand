
import os, requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.raise_for_status())
files = r'C:\Users\jhoov\Projects\FruitStand'
url = 'http://34.16.135.157/fruits' # not an actual url
imap = ['name','weight','description','image_name']

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

def upload_descriptions(url, fruit_data):
    for fruit in fruit_data:
        try:
            response = requests.post(url,data=fruit)
        except Exception as err:
            print(err)
    

fruit_data = get_fruit_info(files, imap)
upload_descriptions(url,fruit_data)
