# encoding: utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Histogram  
We can consider histogram as a graph or plot, which gives you an overall idea 
about the intensity distribution of an image. 

It is a plot with pixel values (ranging from 0 to 255, not always) in X-axis 
and corresponding number of pixels in the image on Y-axis.

It is just another way of understanding the image. 
By looking at the histogram of an image, you get intuition about
contrast, brightness, intensity distribution etc of that image.
'''

path = 'F:/Desktop/1.JPG'
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
Histogram Calculation in OpenCV
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
    mask- To find histogram of full image, it is given as “None”
    
hist is a 256x1 array, each value corresponds to number of pixels in that image with its corresponding pixel value
'''
hist = cv2.calcHist([gray], [0], None, [256], [0,256])
plt.plot(range(256), hist)
plt.show()

'''
Histogram Calculation in Numpy
np.bincount() is much faster than (around 10X) np.histogram()
OpenCV function is more faster than (around 40X) than np.histogram()
'''
hist, bins = np.histogram(gray.ravel(), 256, [0,256])
hist1 = np.bincount(gray.ravel(), minlength=256)
x = range(256)
plt.plot(x, hist)
plt.show()

'''
Plotting Histograms
'''
# Using Matplotlib

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(1,2,2)
plt.hist(gray.ravel(), 256, [0,256])
plt.show()
 
color = ['b', 'g', 'r']
for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

'''Application of Mask'''
mask = np.zeros(gray.shape, np.uint8)
r, c = mask.shape
mask[r/5:-r/5, c/5:-c/5] = 255
# 指定mask区域按维与
masked_img = cv2.bitwise_and(gray, gray, mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([gray], [0], None, [256], [0,256])
hist_mask = cv2.calcHist([gray], [0], mask, [256], [0,256])

plt.subplot(221), plt.imshow(gray, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0, 256])

plt.show()



