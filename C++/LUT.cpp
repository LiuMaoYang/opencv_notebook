#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <string>
#include <iostream>
/*ÏßÐÔ±ä»»£¨LUT£©
Performs a look-up table transform of an array.
*/

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
	int table[256];
	for (int i = 0; i < 256; i++) {
		if (i < 100)
			table[i] = 0;
		else if (i >= 100 && i < 200)
			table[i] = 100;
		else
			table[i] = 255;
	}

	Mat lut(1, 256, CV_8U);
	uchar* p = lut.data;
	for (int i = 0; i < 256; i++)
		p[i] = table[i];

	String path = "F:/Desktop/1.JPG";
	Mat img = imread(path, 1);
	Mat imgC;
	LUT(img, lut, imgC);

	namedWindow("first", 1);
	namedWindow("after", 1);
	imshow("first", img);
	imshow("after", imgC);
	waitKey();

	destroyAllWindows();
	return 0;
}