#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>

using namespace cv;
using namespace std;

char* windowsName = "Threshold Demo";
char* TrackbarType = "Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted";
char* TrackbarValue = "Value";
char* TrackbarMaxValue = "MaxValue";

int type_value = 2;
int threshold_value = 100;
int max_value = 200;
int max_type_value = 4;
int max_threshold_value = 255;

Mat src, dst;
void Threshold_Demo(int, void*);

/** @function main */
int main(int argc, char** argv)
{
	String path = "F:/Desktop/2.JPG";
	src = imread(path, 0);
	namedWindow(windowsName,CV_WINDOW_AUTOSIZE);
	
	createTrackbar(TrackbarType, windowsName, &type_value, max_type_value, Threshold_Demo);
	createTrackbar(TrackbarValue, windowsName, &threshold_value, max_threshold_value, Threshold_Demo);
	createTrackbar(TrackbarMaxValue, windowsName, &max_value, max_threshold_value, Threshold_Demo);
	Threshold_Demo(0, 0);

	while (1){
		int c;
		c=waitKey(5);
		if ((char)c == 27)
			break;
	}

	destroyAllWindows();
	return 0;
}

void Threshold_Demo(int, void*) {
	/* 0: Binary                     src(i,j)>thre? maxV:0
	1: Binary Inverted               src(i,j)>thre? 0:maxV
	2: Threshold Truncated           src(i,j)>thre? thre:src(i,j)
	3: Threshold to Zero             src(i,j)>thre? src(i,j):0
	4: Threshold to Zero Inverted    src(i,j)>thre? 0:src(i,j)
	*/
	threshold(src, dst, threshold_value, max_value, type_value);
	imshow(windowsName, dst);
}