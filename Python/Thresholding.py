#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Simple Thresholding
It's must be a grayscale image
cv2.threshold(src, thresh, maxval, type[, dst]) 鈫?retval, dst
'''
path='F:/Desktop/1.JPG'
img = cv2.imread(path,0)
maxVal = np.max(np.array(img))
thresh = maxVal/2

ret1, img1 = cv2.threshold(img, thresh, maxVal, cv2.THRESH_BINARY) # dst(x, y) = src(x, y)> thresh? maxVal : 0
ret2, img2 = cv2.threshold(img, thresh, maxVal, cv2.THRESH_BINARY_INV) # dst(x, y) = src(x, y)> thresh? 0 : maxVal
ret3, img3 = cv2.threshold(img, thresh, maxVal, cv2.THRESH_TRUNC) # dst(x, y) = src(x, y)> thresh? thresh : src(x, y)
ret4, img4 = cv2.threshold(img, thresh, maxVal, cv2.THRESH_TOZERO) # dst(x, y) = src(x, y)> thresh? src(x, y) : 0
ret5, img5 = cv2.threshold(img, thresh, maxVal, cv2.THRESH_TOZERO_INV) # dst(x, y) = src(x, y)> thresh? 0 : src(x, y)
ret6, img6 = cv2.threshold(img, thresh, maxVal, cv2.THRESH_OTSU)
  
  
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV','THRESH_OTSU']
imgs = [img, img1, img2, img3, img4, img5, img5, img6]
  
for i in range(7):
    plt.subplot(2,4,i+1)
    plt.imshow(imgs[i], 'gray')
    plt.title(titles[i].title())
    plt.xticks([]),plt.yticks([]) #鍘绘帀x, y杞寸殑鏍囪
plt.show()

'''
Adaptive Thresholding
the algorithm calculate the threshold for a small regions of the image
cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) 鈫?dst
Thresholding type that must be either THRESH_BINARY or THRESH_BINARY_INV 
Block Size: decides the size of neighbourhood area: 3, 5, 7, and so on.
C: It is just a constant which is subtracted from the mean or weighted mean calculated
'''
img2 = cv2.adaptiveThreshold(img, maxVal, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
img3 = cv2.adaptiveThreshold(img, maxVal, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
titles = ['Original Image', 'Global Thresholding (v = maxVal/2)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, img1, img2, img3]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i].title())
    plt.xticks([]),plt.yticks([])
plt.show()

'''
图像二值化----otsu（最大类间方差法、大津算法）
背景和目标之间的类间方差越大,说明构成图像的2部分的差别越大
当部分目标错分为背景或部分背景错分为目标都会导致2部分差别变小
因此,使类间方差最大的分割意味着错分概率最小。
对于图像I(x,y),前景(即目标)和背景的分割阈值记作T,
属于前景的像素点数占整幅图像的比例记为ω0,其平均灰度μ0;
背景像素点数占整幅图像的比例为ω1,其平均灰度为μ1。
图像的总平均灰度记为μ,类间方差记为g。
假设图像的背景较暗,并且图像的大小为M×N,
图像中像素的灰度值小于阈值T的像素个数记作N0,像素灰度大于阈值T的像素个数记作N1,则有:
　　　　　　ω0=N0/ M×N (1)
　　　　　　ω1=N1/ M×N (2)
　　　　　　N0+N1=M×N (3)
　　　　　　ω0+ω1=1 (4)
　　　　　　μ=ω0*μ0+ω1*μ1 (5)
　　　　　　g=ω0(μ0-μ)^2+ω1(μ1-μ)^2 (6)
将式(5)代入式(6),得到等价公式: g=ω0ω1(μ0-μ1)^2 (7)
采用遍历的方法得到使类间方差最大的阈值T,即为所求
'''
