#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
"""
pyramids can be used to accelerate coarse-to-fine search algorithms, 
to look for objects or patterns at different scales, 
and to perform multi-resolution blending operations
There are two kinds of Image Pyramids. 
1) Gaussian Pyramid and 2) Laplacian Pyramids
"""

path='F:/Desktop/1.JPG'
img=cv2.imread(path)
img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
print img.shape
# (396L, 687L, 3L)

pyr_down=[img]
img_down = img
for i in range(3):
    img_down = cv2.pyrDown(img_down)
    print img_down.shape
    pyr_down.append(img_down)
# (198L, 344L, 3L)
# (99L, 172L, 3L)
# (50L, 86L, 3L)
print ''

pyr_up=[]
for i in range(3):
    img_up = cv2.pyrUp(pyr_down[i+1])
    img_up = cv2.resize(img_up, (pyr_down[i].shape[1], pyr_down[i].shape[0]))
    print img_up.shape
    pyr_up.append(img_up) 
# (396L, 687L, 3L)
# (198L, 344L, 3L)
# (99L, 172L, 3L)

# title = ['Gaussian pyr_down',' Gaussian pyr_up', 'Laplacian Pyr']
for i in range(3):
#     plt.subplot(3,3,i+1),plt.imshow(cv2.cvtColor(pyr_down[i],cv2.COLOR_RGB2BGR))
#     plt.subplot(3,3,i+1+3),plt.imshow(cv2.cvtColor(pyr_up[i],cv2.COLOR_RGB2BGR))
#     plt.subplot(3,3,i+1+6),plt.imshow(cv2.cvtColor(pyr_down[i]-pyr_up[i],cv2.COLOR_RGB2BGR))
    plt.subplot(3,3,i+1),plt.imshow(pyr_down[i],'gray')
    plt.subplot(3,3,i+1+3),plt.imshow(pyr_up[i],'gray')
    plt.subplot(3,3,i+1+6),plt.imshow(pyr_down[i]-pyr_up[i],'gray')
plt.show()

