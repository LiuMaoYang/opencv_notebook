#encoding:utf-8
import cv2
import numpy as np

path1='F:/Desktop/1.JPG'
path2='F:/Desktop/2.JPG'
img1=cv2.imread(path1)
img2=cv2.imread(path2)

#ROI adding
img11=img1.copy()
img11[1:1+img2.shape[0],1:1+img2.shape[1]]=img2
cv2.imshow('add',img11)

# Image Blending
# Both images should be of same depth and type,
# or second image can just be a scalar value.
# dst = alpha * img1 + beta * img2 + gamma
img22=cv2.resize(img2,(img1.shape[1],img1.shape[0]),interpolation=cv2.INTER_NEAREST)
dst=cv2.addWeighted(img1,0.5,img22,0.3,0)
cv2.imshow('blend',dst)

cv2.waitKey()
cv2.destroyAllWindows()
