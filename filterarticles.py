#Filterarticles.py takes in a path and quickly filters out any empty images
import os
import glob

path = '/Users/shsu/how_old_recommendation/wiki_crop/'

for i in os.listdir(path):
    if len(i) < 5: 
        for j in os.listdir(path + str(i)):
            if os.path.getsize(path + str(i) + '/' + str(j)) < 2000:
                os.remove(path + str(i) + '/' + str(j))
