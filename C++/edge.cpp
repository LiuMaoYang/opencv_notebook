#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <highgui.h>
#include <stdlib.h>
#include <stdio.h>
/*
You can easily notice that in an edge, the pixel intensity changes in a notorious way. 
A good way to express changes is by using derivatives. 
A high change in gradient indicates a major change in the image.
*/

using namespace cv;

// Global variables
Mat src, threE, threC, dstX, dstY, dst, dstCanny;

char* window_name = "Edge Demo";
char* canny_window_name = "Canny Edge Demo";

char* type_name = "Operation: \n 0: Sobel - 1: Scharr - 2: Laplacian";
char* blur_size = "blur_size";
char* kernel_size = "kernel_size";

char* low_value = "lower threshold";
char* upper_value = "upper threshold";

int ddepth = CV_16S;

int type = 0;
int bsize = 1;
int ksize = 1;
int low_thre = 100;
int upper_thre = 200;
int const max_type = 3;
int const max_size = 5;
int const max_value = 255;

void edge(int, void*);
void canny_op(int, void*);
int main() {
	String path = "F:/Desktop/2.JPG";
	src = imread(path, 0);
	namedWindow(window_name, CV_WINDOW_AUTOSIZE);
	namedWindow(canny_window_name, CV_WINDOW_AUTOSIZE);

	createTrackbar(type_name, window_name, &type, max_type, edge);
	createTrackbar(blur_size, window_name, &bsize, max_size, edge);
	createTrackbar(kernel_size, window_name, &ksize, max_size, edge);

	createTrackbar(blur_size, canny_window_name, &bsize, max_size, canny_op);
	createTrackbar(low_value, canny_window_name, &low_thre, max_value, canny_op);
	createTrackbar(upper_value, canny_window_name, &upper_thre, max_value, canny_op);
	edge(0, 0);
	canny_op(0, 0);

	while (1){
		int c;
		c = waitKey(5);
		if ((char)c == 27)
			break;
	}

	destroyAllWindows();
	return 0;
}

void edge(int, void*) {
	GaussianBlur(src, threE, Size(2 * bsize + 1, 2 * bsize + 1), 0);

	/*void Sobel(InputArray src, OutputArray dst, int ddepth, int dx, int dy, 
			int ksize=3, double scale=1, double delta=0, int borderType=BORDER_DEFAULT )
	  void Scharr(InputArray src, OutputArray dst, int ddepth, int dx, int dy, 
			double scale=1, double delta=0, int borderType=BORDER_DEFAULT )
	  void Laplacian(InputArray src, OutputArray dst, int ddepth, int ksize=1, 
			double scale=1, double delta=0, int borderType=BORDER_DEFAULT )*/
	
	// Gradient X-  Scharr( src_gray, grad_x, ddepth, 1, 0, scale, delta, BORDER_DEFAULT );
	// Gradient Y-  Scharr( src_gray, grad_x, ddepth, 0, 1, scale, delta, BORDER_DEFAULT );
	if (type == 0) {
		Sobel(threE, dstX, ddepth, 1, 0, 2 * ksize + 1);
		Sobel(threE, dstY, ddepth, 0, 1, 2 * ksize + 1);
		addWeighted(dstX, 0.5, dstY, 0.5, 0, dst);
	}
	else if (type == 1) {
		Scharr(threE, dstX, ddepth, 1, 0);
		Scharr(threE, dstY, ddepth, 0, 1);
		addWeighted(dstX, 0.5, dstY, 0.5, 0, dst);
	}	
	else if (type == 2) 
		Laplacian(threE, dst, ddepth, 2 * ksize + 1);

	convertScaleAbs(dst, dst);
	imshow(window_name, dst);
}

void canny_op(int, void*) {
	/*
	1. Filter out any noise. The Gaussian filter is used for this purpose. 

    2. Find the intensity gradient of the image. For this, we follow a procedure analogous to Sobel:
	  a. Apply a pair of convolution masks (in x and y directions)

	  b. Find the gradient strength and direction with
		G = sqrt(Gx^2 + Gy^2)
		theta = arctan(Gy / Gx)

		The direction is rounded to one of four possible angles (namely 0, 45, 90 or 135)

	3. Non-maximum suppression is applied. 
		This removes pixels that are not considered to be part of an edge. 
		Hence, only thin lines (candidate edges) will remain.

	4. Hysteresis: The final step. Canny does use two thresholds (upper and lower):

		a. If a pixel gradient is higher than the upper threshold, the pixel is accepted as an edge
		b. If a pixel gradient value is below the lower threshold, then it is rejected.
		c. If the pixel gradient is between the two thresholds, then it will be accepted only if it is connected to a pixel that is above the upper threshold.
		
	  Canny recommended a upper:lower ratio between 2:1 and 3:1.
	*/
	GaussianBlur(src, threC, Size(2 * bsize + 1, 2 * bsize + 1), 0);

	Canny(threC, dstCanny, low_thre, upper_thre);
	imshow(canny_window_name, dstCanny);
}