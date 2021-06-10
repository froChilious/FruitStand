#! /usr/bin/env python3

from PIL import Image
import glob, os

im_dir = '/home/student/supplier-data/images'
tiff_dir = r'C:\Users\jhoov\Projects\PIL'

def change_images(dir, from_ext, to_ext):
    full_image_path = os.path.join(dir,'*.{}'.format(from_ext))
    print(full_image_path)
    for infile in glob.glob(full_image_path):
        try:
            with Image.open(infile).convert('RGB') as im:
                file,ext = os.path.splitext(infile)
                filen = file.split('/')[-1]
                old_file = '{}.{}'.format(file,from_ext)
                new_file = '{}.{}'.format(file,to_ext)
                #print(new_file)
                im.rotate(180).resize((640,480)).save(new_file,format=to_ext)
                print ('Image {} has been processed to {}'.format(old_file,new_file))
        except Exception as e:
            print(f'Unable to process the picture {file+ext} with Error: {e}.')

change_images(tiff_dir,'jpg','tiff')
