#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Simple Thresholding
It's must be a grayscale image
cv2.threshold(src, thresh, maxval, type[, dst]) �?retval, dst
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
    plt.xticks([]),plt.yticks([]) #去掉x, y轴的标记
plt.show()

'''
Adaptive Thresholding
the algorithm calculate the threshold for a small regions of the image
cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) �?dst
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
ͼ���ֵ��----otsu�������䷽�������㷨��
������Ŀ��֮�����䷽��Խ��,˵������ͼ���2���ֵĲ��Խ��
������Ŀ����Ϊ�����򲿷ֱ������ΪĿ�궼�ᵼ��2���ֲ���С
���,ʹ��䷽�����ķָ���ζ�Ŵ�ָ�����С��
����ͼ��I(x,y),ǰ��(��Ŀ��)�ͱ����ķָ���ֵ����T,
����ǰ�������ص���ռ����ͼ��ı�����Ϊ��0,��ƽ���ҶȦ�0;
�������ص���ռ����ͼ��ı���Ϊ��1,��ƽ���Ҷ�Ϊ��1��
ͼ�����ƽ���Ҷȼ�Ϊ��,��䷽���Ϊg��
����ͼ��ı����ϰ�,����ͼ��Ĵ�СΪM��N,
ͼ�������صĻҶ�ֵС����ֵT�����ظ�������N0,���ػҶȴ�����ֵT�����ظ�������N1,����:
��������������0=N0/ M��N (1)
��������������1=N1/ M��N (2)
������������N0+N1=M��N (3)
��������������0+��1=1 (4)
��������������=��0*��0+��1*��1 (5)
������������g=��0(��0-��)^2+��1(��1-��)^2 (6)
��ʽ(5)����ʽ(6),�õ��ȼ۹�ʽ: g=��0��1(��0-��1)^2 (7)
���ñ����ķ����õ�ʹ��䷽��������ֵT,��Ϊ����
'''
