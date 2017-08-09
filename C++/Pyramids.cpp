#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>

/*
Usually we need to convert an image to a size different than its original. 
For this, there are two possible options:
	Upsize the image (zoom in) or
	Downsize it (zoom out).

Image Pyramid
An image pyramid is a collection of images - all arising from a single original image - 
that are successively downsampled until some desired stopping point is reached.
There are two common kinds of image pyramids:
	Gaussian pyramid: Used to downsample images
	Laplacian pyramid: Used to reconstruct an upsampled image from an image lower in the pyramid (with less resolution)
*/

using namespace cv;
using namespace std;

/** @function main */
int main(int argc, char** argv)
{
	Mat src, dst, org;
	char* windowsName = "Pyramids Demo";

	String path = "F:/Desktop/2.JPG";
	src = imread(path, 0);
	org = src;
	namedWindow(windowsName, CV_WINDOW_AUTOSIZE);
	//imshow(windowsName, dst);
	
	while (true){
		char c;
		cin >> c;
		resize(src, src, Size(src.cols & -2, src.rows & -2));

		if (c == 'q') break;
		if (c == 'u')
			pyrUp(src, dst, Size(src.cols * 2, src.rows * 2));
		if (c == 'd')
			pyrDown(src, dst, Size(src.cols / 2, src.rows / 2));
		if (c == 'l') {
			Mat dst1, dst2;
			pyrDown(src, dst1, Size(src.cols / 2, src.rows / 2));
			pyrUp(dst1, dst2, Size(dst1.cols * 2, dst1.rows * 2));
			subtract(src, dst2, dst);
		}
		src = dst;
		imshow(windowsName, dst);
		waitKey(5);
	}
	destroyAllWindows();
	return 0;
}