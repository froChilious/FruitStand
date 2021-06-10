
import os, requests

files = r'C:\Users\jhoov\Projects\FruitStand'
url = 'http://34.16.135.157/fruits' # not an actual url
imap = ['name','weight','description','image_name']

def upload_descriptions(file_dir, url, fieldmap):
    for file in os.listdir(file_dir):
        if file.split('.')[-1] == 'txt':
            print(file)
            fruit_info = {}
            with open(os.path.join(file_dir,file),'r') as f:
                for i,line in enumerate(f.readlines()):
                    fruit_info[imap[i]] = line.strip()
            response = requests.post(url,data=fruit_info)
            #print(response.raise_for_status())
            #print(f'{response.request.url}?{response.request.body}')

#upload_descriptions(files, url, imap)
