#Canny Edge detection
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('/home/chanakya/Documents/Intern/Imd/5.jpg')
print('Original_d:',img.shape)
scale_p=40
width=int(img.shape[1]*scale_p/100)
height=int(img.shape[0]*scale_p/100)
dim=(width,height)
img=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print('resized Dimensions:',img.shape)
cv2.imshow("Resized image",img)
cv2.waitKey(0)
edges=cv2.Canny(img,100,200)
cv2.imshow('canny',edges)
cv2.waitKey(0)
