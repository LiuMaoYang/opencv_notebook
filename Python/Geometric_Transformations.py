#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sympy.physics.quantum.spin import Rotation

path = 'F:/Desktop/1.JPG'
img =cv2.imread(path)
imgPlt = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

'''
Scaling
x' = sx * x 
y' = sy * y
M = [sx 0 0     [x'  = M * [x   
     0 sy 0      y'         y
     0 0  1]     1]         1]

cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) → dst

dsize –output image size; if it equals zero, it is computed as:
    dsize = Size(round(fx*src.cols), round(fy*src.rows))
Either dsize or both fx and fy must be non-zero.

fx –scale factor along the horizontal axis; when it equals 0, it is computed as
    (double)dsize.width/src.cols

fy –scale factor along the vertical axis; when it equals 0, it is computed as
    (double)dsize.height/src.rows

interpolation –
interpolation method:

INTER_NEAREST - a nearest-neighbor interpolation
INTER_LINEAR - a bilinear interpolation (used by default)
INTER_AREA - resampling using pixel area relation.
            It may be a preferred method for image decimation, as it gives moire’-free results. 
            But when the image is zoomed, it is similar to the INTER_NEAREST method.
INTER_CUBIC - a bicubic interpolation over 4x4 pixel neighborhood
INTER_LANCZOS4 - a Lanczos interpolation over 8x8 pixel neighborhood
'''
plt.subplot(2,3,1),plt.imshow(imgPlt),plt.title('Origin')
method = [cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_AREA, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4]
title = ['INTER_NEAREST', 'INTER_LINEAR', 'INTER_AREA', 'INTER_CUBIC', 'INTER_LANCZOS4']
for i in range(5):
    res = cv2.resize(img, None, fx=2, fy=2, interpolation = method[i])
    res = cv2.cvtColor(res, cv2.COLOR_RGB2BGR)
    plt.subplot(2,3,i+2),plt.imshow(res),plt.title(title[i].title())
plt.show()

'''
Translation
If you know the shift in (x,y) direction, let it be (tx, ty), 
you can create the transformation matrix M as follows:
x' = x + tx
y' = y + ty
M = [1 0 tx     [x'  = M * [x   
     0 1 ty      y'         y
     0 1 ty]     1]         1]
     
cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) → dst
Remember width = number of columns, and height = number of rows
'''
tx,ty=50,100
M = np.float32([[1,0,tx],[0,1,ty]])  
rows, cols = img.shape[0], img.shape[1]
dst = cv2.warpAffine(img, M, (cols+tx, rows+ty))
dst = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)
plt.subplot(121), plt.imshow(imgPlt), plt.title('Origin')  
plt.subplot(122), plt.imshow(dst), plt.title('Translation')  
plt.show()

'''
Rotation
x' = x * cosa - y * sina
y' = x * sina + x * cosa
M = [cosa  -sina
     sina   cosa]
     
cv2.getRotationMatrix2D(center, angle, scale) → retval
center – Center of the rotation in the source image.
angle – Rotation angle in degrees. Positive values mean counter-clockwise rotation 
        (the coordinate origin is assumed to be the top-left corner).
scale – Isotropic scale factor.
'''
rows, cols = img.shape[0], img.shape[1]
angle = 90
angle_pi = np.pi/(180/angle)
newRows, rewCols = cols + rows * np.cos(angle_pi), rows + cols * np.cos(angle_pi)
print rows, cols, newRows, rewCols
M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 2)
dst = cv2.warpAffine(img, M, (int(rewCols), int(newRows)))
dst = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)
plt.subplot(121), plt.imshow(imgPlt), plt.title('Origin')  
plt.subplot(122), plt.imshow(dst), plt.title('Translation')  
plt.show()

'''
To find the transformation matrix, we need three points from input image 
and their corresponding locations in output image. 
Then cv2.getAffineTransform will create a 2x3 matrix which is to be passed to cv2.warpAffine
'''
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)
dst = cv2.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

'''
Perspective Transformation
To find this transformation matrix, you need 4 points on the input image and corresponding points
on the output image. Among these 4 points, 3 of them should not be collinear. 
Then transformation matrix can be found by the function cv2.getPerspectiveTransform. 
Then apply cv2.warpPerspective with this 3x3 transformation matrix
f' = H f
x' = (h00x + h01y + h02) / (h20x + h21y + h22)
y' = (h10x + h11y + h12) / (h20x + h21y + h22)
'''
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
dst = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()