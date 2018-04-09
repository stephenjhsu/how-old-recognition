#resize takes in all the images and resizes them to a standard size
import os
from PIL import Image
from PIL import ImageOps

def imageResize(basename,imageName):
    """
    resize image
    basename : eg. /home/username/XYZFolder
    image name : xyz.jpg
    New folder in the working directory will be created with '_resized' as suffix
    """
    new_width  = 128
    new_height = 128
    try:  
        img = Image.open(basename+"/"+imageName) # image extension *.png,*.jpg
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(basename+'_resized/'+imageName)
    except:
        os.mkdir(basename+'_resized/')
        img = Image.open(basename+"/"+imageName) # image extension *.png,*.jpg
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(basename+'_resized/'+imageName)

def resizer(folderPath):
    """
    to resize all files present in a folder
    resizer('/home/username/XYZFolder')
    """
    for subdir, dirs, files in os.walk(folderPath):
        for fileName in files:
            try:
                #  print os.path.join(subdir, file)
                filepath = subdir + os.sep + fileName
                #  print filepath
                if filepath.endswith(".jpg" or ".jpeg" or ".png" or ".gif"):
                    imageResize(subdir,fileName)
            except:
                print traceback.print_exc()

 
# to resize all images in given folder, run this 
resizer('/Users/shsu/how_old_recommendation/wiki_crop/')