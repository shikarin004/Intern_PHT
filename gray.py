import cv2
import numpy as np
path=r'/home/chanakya/Documents/Intern/Imd/5.jpg'
img=cv2.imread(path)
cv2.imshow('Ori',img)
gray_i=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',gray_i)
cv2.waitKey(0)
cv2.destroyAllWindows
# M-2
# path,0
#M-3
(row,col)=img.shape[0:2]
for i in range(row):
    for j in range(col):
        img[i,j]=sum(img[i,j])*(1/3)
cv2.imshow('Gray',img)
cv2.waitKey(0)
cv2.destroyAllWindows
