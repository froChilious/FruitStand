#! /usr/bin/env python3

from PIL import Image
import glob, os

#im_dir = '/home/student/supplier-data/images'

def change_images(dir, from_ext, to_ext, resize=(600,400)):
    '''
    Search the given path for all image files with the from_ext and
    convert them to the to_ext format while also re-sizing the image 
    to 640x480. Write them back out to the same directory.
    '''
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
                im.rotate(0).resize(resize).save(new_file,format=to_ext)
                print ('Image {} has been processed to {}'.format(old_file,new_file))
        except Exception as e:
            print(f'Unable to process the picture {file+ext} with Error: {e}.')

#change_images(tiff_dir,'tiff','jpeg')
