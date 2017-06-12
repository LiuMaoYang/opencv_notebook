#encoding:utf-8
import cv2
import numpy as np
import copy as cp
# path='F:/Desktop/1.JPG'
def nothing(x):
    pass

def colorSet():
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    color=r,g,b
    return color

def drawG(event,x,y,flags,param):
    d=cv2.getTrackbarPos(draw,'image')
    s=cv2.getTrackbarPos(so_or_ho,'image')
    th=cv2.getTrackbarPos('thickness','image')
    color=colorSet()
    
    global ix,iy,drawing,img
    if event==cv2.EVENT_LBUTTONDOWN:
        ix,iy=x,y
        drawing=True
    elif event==cv2.EVENT_LBUTTONUP and drawing:
        drawing=False
        if d==0:
            cv2.line(img,(ix,iy),(x,y),color,th)           
        elif d==1:
            r=int(np.linalg.norm(np.array((ix,iy))-np.array((x,y))))
            center=(int(float(ix+x)/2), int(float(iy+y)/2))
            if s==0:            
                cv2.circle(img,center,r,color,-1)
            else:
                cv2.circle(img,center,r,color,th)
        elif d==2:
            lr=int(np.linalg.norm(np.array((ix,iy))-np.array((x,y))))
            center=int(float(ix+x)/2),int(float(iy+y)/2)
            if s==0:
                cv2.ellipse(img,center,(lr,lr/2),0,0,360,color,-1)
            else:
                cv2.ellipse(img,center,(lr,lr/2),0,0,360,color,th)
        elif d==3:
            if s==0:
                cv2.rectangle(img,(ix,iy),(x,y),color,-1)
            else:
                cv2.rectangle(img,(ix,iy),(x,y),color,th)
            
ix,iy=-1,-1
drawing=False   
# Create a black image, a window
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create so_or_ho for Solid/Hollow functionality
so_or_ho='0 : Solid \n 1 : Hollow'
cv2.createTrackbar(so_or_ho,'image',0,1,nothing)

# create draw for different graphics
draw='0:line \n 1:circle \n 2:ellipse \n 3:rectangle'
cv2.createTrackbar(draw,'image',0,3,nothing)

# create thickness for different graphics
cv2.createTrackbar('thickness','image',0,50,nothing)

#allowed just one setMouseCallback, and put out of while(1)
cv2.setMouseCallback('image',drawG)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break   
   
cv2.destroyAllWindows()


