#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <string>
#include <iostream>
/*Adding (blending) two images using the linear blend operator
g(x) = (1 - a)f0(x) + af1(x), where a varying from 0 to 1
Warning Since we are adding src1 and src2, they both have to be of the same size (width and height) and type.
*/

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
	String path1 = "F:/Desktop/1.JPG";
	String path2 = "F:/Desktop/2.JPG";

	Mat src1 = imread(path1, 1);
	Mat src2 = imread(path2, 1);
	Mat dst;

	double alpha;
	cin >> alpha;
	double beta = 1.0 - alpha;
	addWeighted(src1, alpha, src2, beta, 0.0, dst);
	
	namedWindow("Linear Blend", 1);
	imshow("Linear Blend", dst);
	waitKey();

	destroyAllWindows();
	return 0;
}