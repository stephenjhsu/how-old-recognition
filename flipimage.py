import numpy as np
import os
from PIL import Image
from PIL import ImageOps
import glob

# path of file
path = '/Users/shsu/how_old_recommendation/wiki_crop/wikitemp/'
floc = '/Users/shsu/how_old_recommendation/wiki_crop//dump/'


def read_files_from_path(path, floc): 
    """
    read_files_from_path takes in:
    Input:
        path: string of the path of the folder of images 
    Output:
        the flipped images of the inputted folder of images
    """
    try:
        os.mkdir(floc)
    except:
        pass
    my_sub_dir = glob.glob(path + '*/*.jpg')
    for j in my_sub_dir:
        img = Image.open(j)
        mirror_img = ImageOps.mirror(img)
        inx = j.split('/')
        try:
            os.mkdir(floc + '1' + inx[-2])
        except:
            pass
        mirror_img.save(floc + '1' + '/'.join(inx[-2:]))

read_files_from_path(path, floc)
