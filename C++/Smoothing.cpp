#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>
/*
*/

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
	String path = "F:/Desktop/2.JPG";
	Mat img = imread(path);
	Mat dst;
	int kernel_size = 5;
	Size kernel = { kernel_size,kernel_size };

	blur(img, dst, kernel);
	imshow("blur", dst);

	GaussianBlur(img, dst, kernel, 0);
	imshow("GaussianBlur", dst);

	medianBlur(img, dst, kernel_size);
	imshow("medianBlur", dst);

	bilateralFilter(img, dst, 9, 75, 75);
	imshow("bilateralFilter", dst);

	waitKey();
	destroyAllWindows();
	return 0;
}

