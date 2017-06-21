#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

path='F:/Desktop/1.JPG'
img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Splitting and Merging Image Channels
#Note: cv: RGB  plt: BGR
r,g,b=cv2.split(img)
imgPlt=cv2.merge([b,g,r])
#the operation same as
imgPlt=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

plt.subplot(1,2,1),plt.imshow(imgPlt),plt.title('RGB')
plt.subplot(1,2,2),plt.imshow(imgGray,cmap='gray'),plt.title('Gray')
plt.show()
  
cv2.namedWindow('RGB'),cv2.imshow('RGB',img)
cv2.namedWindow('Gray'),cv2.imshow('Gray',imgGray)
cv2.waitKey(),cv2.destroyAllWindows()

# Accessing and Modifying pixel values
print img.item(1,1,1)#157
img.itemset((1,1,1),100)
print img.item(1,1,1)#100

# Accessing Image Properties
print img.shape #(396L, 687L, 3L)
print img.size #816156 (total number of pixels)
print img.dtype #uint8

#ROI
ROI=img[130:200,80:190]
imgAdd=img
imgAdd[290:290+ROI.shape[0],190:190+ROI.shape[1]]=ROI
cv2.namedWindow('AddROI'),cv2.imshow('AddROI',imgAdd)
cv2.waitKey(),cv2.destroyAllWindows()

#Padding
img1=imgPlt
r,c=img1.shape[0],img1.shape[1]
step=int(raw_input())
top=int(r/step)
bottom=int(r/step)
left=int(c/step)
right=int(c/step)

# cv2.BORDER_REPLICATE - Last element is replicated throughout:
# aaaaaa|abcdefgh|hhhhhhh
replicate = cv2.copyMakeBorder(img1,top,bottom,left,right,cv2.BORDER_REPLICATE)
# cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements: 
# fedcba|abcdefgh|hgfedcb
reflect = cv2.copyMakeBorder(img1,top,bottom,left,right,cv2.BORDER_REFLECT)
# cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight change: 
# gfedcb|abcdefgh|gfedcba
reflect101 = cv2.copyMakeBorder(img1,top,bottom,left,right,cv2.BORDER_REFLECT_101)
# cv2.BORDER_WRAP - Can’t explain, it will look like this : 
# cdefgh|abcdefgh|abcdefg
wrap = cv2.copyMakeBorder(img1,top,bottom,left,right,cv2.BORDER_WRAP)
# cv2.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next
# argument.
constant= cv2.copyMakeBorder(img1,top,bottom,left,right,cv2.BORDER_CONSTANT,value=[255,0,0])

plt.subplot(231),plt.imshow(img1,cmap='gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()


