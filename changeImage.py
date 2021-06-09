#! /usr/bin/env python3

from PIL import Image
import glob, os

im_dir = '/home/student/supplier-data/images'

def change_images(dir, from_ext, to_ext):

    for infile in glob.glob(os.path.join(dir,'/*.{}'.from_ext):
        try:
            with Image.open(infile) as im:
                file,ext = os.path.splitext(infile)
                filen = file.split('/')[-1]
                new_file = '{}.jpeg'.format(file)
                #print(new_file)
                im.rotate(180).resize((640,480)).save(new_file,format=to_ext)
                print ('Image {}.tiff has been processed to {}.jpeg'.format(file,new_file))
        except Exception as e:
            print(f'Unable to process the picture {file+ext} with Error: {e}.')

