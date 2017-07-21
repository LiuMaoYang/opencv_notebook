#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'F:/Desktop/1.JPG'
img =cv2.imread(path)
imgPlt = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

'''
2D Convolution ( Image Filtering )
As for one-dimensional signals, images also can be filtered with various 
low-pass filters (LPF), high-pass filters (HPF),etc. 
A LPF helps in removing noise, or blurring the image. 
A HPF filters helps in finding edges in an image

cv2.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) → dst
ddepth –
desired depth of the destination image; if it is negative, it will be the same as src.depth(); 
'''
size = 5
# kernel = np.ones((size, size), np.float32)/np.power(size, 2)
# dst = cv2.filter2D(img, -1, kernel)
# plt.subplot(121),plt.imshow(imgPlt),plt.title('original'.title())
# plt.subplot(122),plt.imshow(cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)),plt.title('averaging'.title())
# plt.show()

'''
Image Blurring (Image Smoothing)
Image blurring is achieved by convolving the image with a low-pass filter kernel. 
It is useful for removing noise. It actually removes high frequency content (e.g: noise, edges) 
from the image resulting in edges being blurred when this is filter is applied.
'''

'''Averaging'''
blur1 = cv2.blur(img, (size, size))

'''
Gaussian Filtering
cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) → dst
sigmaX – Gaussian kernel standard deviation in X direction.
sigmaY – Gaussian kernel standard deviation in Y direction; if sigmaY is zero, it is set to be equal to sigmaX,
if both sigmas are zeros, they are computed from ksize.width and ksize.height
    sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8
'''
blur2 = cv2.GaussianBlur(img, (size, size), 0)

'''Median Filtering'''
blur3 = cv2.medianBlur(img, size) 

'''
Bilateral Filtering
cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) → dst
d – Diameter of each pixel neighborhood that is used during filtering. 
    If it is non-positive, it is computed from sigmaSpace .
    
The bilateral filter also uses a Gaussian filter in the space domain, 
but it also uses one more (multiplicative) Gaussian filter component 
which is a function of pixel intensity differences

spatial neighbors
    d(i,j,k,l) = exp(-((i-k)^2 + (j-l)^2) / 2*sigmaSpace^2)
intensity neighbors
    r(i,j,k,l) = exp(-||f(i,j) - f(k,l)||^2 / 2*sigmaColor^2)
w(i,j,k,l) = d*r
g(i,j) = sum(f(k,l)*w(i,j,k,l)) / sum(w(i,j,k,l))
'''
blur4 = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(231),plt.imshow(imgPlt),plt.title('original'.title())
plt.subplot(233),plt.imshow(cv2.cvtColor(blur1, cv2.COLOR_RGB2BGR)),plt.title('averaging'.title())
plt.subplot(234),plt.imshow(cv2.cvtColor(blur1, cv2.COLOR_RGB2BGR)),plt.title('Gaussian Filtering'.title())
plt.subplot(235),plt.imshow(cv2.cvtColor(blur1, cv2.COLOR_RGB2BGR)),plt.title('Median Filtering'.title())
plt.subplot(236),plt.imshow(cv2.cvtColor(blur1, cv2.COLOR_RGB2BGR)),plt.title('Bilateral Filtering'.title())
plt.show()








