#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'F:/Desktop/1.JPG'
img =cv2.imread(path, 0)

'''
Sobel kernel
Gx = [-1 0 1        Gy = [1  2  1
      -2 0 2              0  0  0
      -1 0 1]            -1 -2 -1]
cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) → dst

     
Laplacian
[0  1  0
 1 -4  1
 0  1  0]
 cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]) → dst
'''
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()

'''
Canny Edge Detection

1. Noise Reduction
Since edge detection is susceptible to noise in the image, 
first step is to remove the noise in the image with a 5x5 Gaussian filter. 
cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) → dst
blur = cv2.GaussianBlur(img, (size, size), 0)

2. Finding Intensity Gradient of the Image
Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction 
to get first derivative in horizontal direction (Gx) and vertical direction (Gy). 
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    
From these two images, we can find edge gradient and direction for each pixel as follows:
    Edge_Gradient(G) = sqrt(Gx^2 + Gy^2)
    Angle = arctan(Gy / Gx)

Gradient direction is always perpendicular(垂直) to edges. 
It is rounded to one of four angles representing vertical, horizontal and two diagonal directions.

3. Non-maximum Suppression(非极大值抑制)
After getting gradient magnitude and direction, a full scan of image is done to remove any unwanted pixels 
which may not constitute the edge. For this, at every pixel, pixel is checked 
if it is a local maximum in its neighborhood in the direction of gradient

4. Hysteresis Thresholding(滞后阈值)
This stage decides which are all edges are really edges and which are not. 
For this, we need two threshold values, minVal and maxVal. Any edges with intensity gradient 
more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so discarded. 

Those who lie between these two thresholds are classified edges or non-edges based on their connectivity. 
If they are connected to “sure-edge” pixels, they are considered to be part of edges.
Otherwise, they are also discarded. 

cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) → edges
'''

edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()


