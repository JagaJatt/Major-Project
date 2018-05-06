import cv2
import numpy as np
from skimage.feature import hog
from skimage import feature
from skimage import data, exposure
import os

path = 'D:\\vb Workz\\8th sem\\major proj2\\DATABASE\\'
c=0
for i in range(1,5):
    path1 = path +str(i)+'\\'
    for j in range(1,51):
        c=c+1
        print(c)
        im1=cv2.imread(path1+str(j)+'.jpg',0)
        #print(path1+str(j)+'.jpg')
        file_name = 'new'+str(j)+'.txt'
        file_path='D:\\vb Workz\\8th sem\\major proj2\\HOG_database\\'+str(i)+'\\'+file_name
        #print(file_path)
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        #print('Done')
        f=open(file_path,'w')
        (h, hogImage) = feature.hog(im1, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2, 2), transform_sqrt=True, visualise=True)
        hlist = list(h)
        hstr = str(hlist)
        hstr = hstr[1:len(hstr)-1]
        f.write(hstr)
        f.close()
        

