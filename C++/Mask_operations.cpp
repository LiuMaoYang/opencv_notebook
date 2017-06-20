#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv/cv.hpp>
#include <string>
#include <iostream>
/*filter2D 图像卷积
C++: void ocl::filter2D(const oclMat& src, oclMat& dst, int ddepth, const Mat& kernel, Point anchor = Point(-1, -1), double delta = 0.0, int borderType = BORDER_DEFAULT)
Parameters :
	src – Source image.
	dst – Destination image.The size and the number of channels is the same as src .
	ddepth – Desired depth of the destination image.If it is negative, it is the same as src.depth().It supports only the same depth as the source image depth.
	kernel – 2D array of filter coefficients.
	anchor – Anchor of the kernel that indicates the relative position of a filtered point within the kernel.The anchor resides within the kernel.The special default value(-1, -1) means that the anchor is at the kernel center.
	delta – optional value added to the filtered pixels before storing them in dst.Value ‘0’ is supported only.
	borderType – Pixel extrapolation method.For details, see borderInterpolate() .
*/

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
	String path = "F:/Desktop/1.JPG";
	Mat img = imread(path, 1);
	Mat mask = (Mat_<char>(3, 3) << 0, -1, 0,
									-1, 5, -1,
									0, -1, 0);//char换成int也没事？
	
	Mat imgA;
	filter2D(img, imgA, -1, mask);
	namedWindow("first", 1);
	namedWindow("after", 1);
	imshow("first", img);
	imshow("after", imgA);
	waitKey();

	destroyAllWindows();
	return 0;
}