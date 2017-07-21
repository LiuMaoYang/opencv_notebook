#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'F:/Desktop/1.JPG'
img =cv2.imread(path, 0)

'''
Morphological transformations are some simple operations 
based on the image shape. It is normally performed on binary images. 
It needs two inputs, one is our original image, 
second one is called structuring element or kernel which decides the nature of operation. 
Two basic morphological operators are Erosion and Dilation（腐蚀膨胀）.
'''

'''
Erosion 腐蚀
The basic idea of erosion is just like soil erosion only, 
it erodes away the boundaries of foreground object 
(Always try to keep foreground in white). 

So what does it do? The kernel slides through the image (as in 2D convolution). 
A pixel in the original image (either 1 or 0) will be considered 1 
only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).

All the pixels near boundary will be discarded depending upon the size of kernel. 
So the thickness or size of the foreground object decreases or simply white region decreases in the image. 
It is useful for removing small white noises, detach two connected objects etc.

cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst
iterations – number of times erosion is applied

dst(x, y) = min src(x+x', y+y')
           (x', y'):element(x',y')!=0
'''
size = 5
kernel = np.ones((size, size), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)
# cv2.imshow('erosion', erosion)
# cv2.waitKey()
# cv2.destroyAllWindows()

'''
Dilation 膨胀
It is just opposite of erosion. 
Here, a pixel element is ‘1’ if at least one pixel under the kernel is ‘1’. 
So it increases the white region in the image or size of foreground object increases. 

Normally, in cases like noise removal, erosion is followed by dilation. 
Because, erosion removes white noises, but it also shrinks our object. So we dilate it. 
Since noise is gone, they won’t come back, but our object area increases. 
It is also useful in joining broken parts of an object

dst(x, y) = max src(x+x', y+y')
           (x', y'):element(x',y')!=0
'''
dilation = cv2.dilate(img,kernel,iterations = 1)

'''
Opening
Opening is just another name of erosion followed by dilation. 
It is useful in removing noise

Closing
Closing is reverse of Opening, Dilation followed by Erosion. 
It is useful in closing small holes inside the foreground objects, or small black points on the object.

Morphological Gradient
It is the difference between dilation and erosion of an image.
The result will look like the outline of the object.

Top Hat
It is the difference between input image and Opening of the image

Black Hat
It is the difference between the closing of the input image and input image

cv2.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst
op –Type of a morphological operation that can be one of the following:
    MORPH_OPEN - an opening operation
    MORPH_CLOSE - a closing operation
    MORPH_GRADIENT - a morphological gradient
    MORPH_TOPHAT - “top hat”
    MORPH_BLACKHAT - “black hat”
    MORPH_HITMISS - “hit and miss”
    
Opening operation:
    dst = open(src, element) = dilate(erode(src, element))
Closing operation:
    dst = close(src, element) = erode(dilate(src, element))
Morphological gradient:
    dst = morph_grad(src, element) = dilate(src, element) - erode(src, element)
“Top hat”:
    dst = tophat(src, element) = src - open(src, element)
“black hat”:
    dst = tophat(src, element) = close(src, element) - src
'''
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


