#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

path1='F:/Desktop/dog.bmp'
path2='F:/Desktop/cat.bmp'
img1=cv2.imread(path1)
img2=cv2.imread(path2)

print img1.shape
print img2.shape
print ''
# (265L, 225L, 3L)
# (265L, 225L, 3L)

# generate Gaussian pyramid
pyr_down1=[img1]
pyr_down2=[img2]
img_down1 = img1
img_down2 = img2
for i in range(6):
    img_down1 = cv2.pyrDown(img_down1)
    img_down2 = cv2.pyrDown(img_down2)
    print img_down1.shape
    pyr_down1.append(img_down1)
    pyr_down2.append(img_down2)
print ''
# (133L, 113L, 3L)
# (67L, 57L, 3L)
# (34L, 29L, 3L)
# (17L, 15L, 3L)
# (9L, 8L, 3L)
# (5L, 4L, 3L)
 
pyr_up1=[]
pyr_up2=[]
for i in range(6):
    img_up1 = cv2.pyrUp(pyr_down1[i+1])
    img_up2 = cv2.pyrUp(pyr_down2[i+1])
    img_up1 = cv2.resize(img_up1, (pyr_down1[i].shape[1], pyr_down1[i].shape[0]))
    img_up2 = cv2.resize(img_up2, (pyr_down2[i].shape[1], pyr_down2[i].shape[0]))
    print img_up1.shape
    pyr_up1.append(img_up1) 
    pyr_up2.append(img_up2)
print ''
# (265L, 225L, 3L)
# (133L, 113L, 3L)
# (67L, 57L, 3L)
# (34L, 29L, 3L)
# (17L, 15L, 3L)
# (9L, 8L, 3L)

# generate Laplacian Pyramid
lp_pyr1=[]
lp_pyr2=[]
for i in range(5,-1,-1):
    lp_pyr1.append(cv2.subtract(pyr_down1[i],pyr_up1[i]))
    lp_pyr2.append(cv2.subtract(pyr_down2[i],pyr_up2[i]))
          
# Now add left and right halves of images in each level
lb=[]
lh=[]
for l1,l2 in zip(lp_pyr1,lp_pyr2):
    r,c,d=l1.shape
    lb.append(np.hstack((l1[:,0:c/2], l2[:,c/2:]))) 
    lh.append((l1+l2)/2) 
    
# now reconstruct
lbr=lb[0]
lhr=lh[0]
for i in range(1,6):
    lbr = cv2.pyrUp(lbr)
    lbr = cv2.resize(lbr, (lb[i].shape[1], lb[i].shape[0]))
    lbr = cv2.add(lbr, lb[i])
    
    lhr = cv2.pyrUp(lhr)
    lhr = cv2.resize(lhr, (lh[i].shape[1], lh[i].shape[0]))
    lhr = cv2.add(lhr, lh[i])
    print lhr.shape

cv2.imshow('1',lbr)
cv2.imshow('2',lhr)
cv2.waitKey()
cv2.destroyAllWindows()
    
 
# # title = ['Gaussian pyr_down',' Gaussian pyr_up', 'Laplacian Pyr']
# for i in range(3):
# #     plt.subplot(3,3,i+1),plt.imshow(cv2.cvtColor(pyr_down[i],cv2.COLOR_RGB2BGR))
# #     plt.subplot(3,3,i+1+3),plt.imshow(cv2.cvtColor(pyr_up[i],cv2.COLOR_RGB2BGR))
# #     plt.subplot(3,3,i+1+6),plt.imshow(cv2.cvtColor(pyr_down[i]-pyr_up[i],cv2.COLOR_RGB2BGR))
#     plt.subplot(3,3,i+1),plt.imshow(pyr_down[i],'gray')
#     plt.subplot(3,3,i+1+3),plt.imshow(pyr_up[i],'gray')
#     plt.subplot(3,3,i+1+6),plt.imshow(pyr_down[i]-pyr_up[i],'gray')
# plt.show()

