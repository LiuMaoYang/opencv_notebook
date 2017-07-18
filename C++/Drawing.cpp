#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <string>
#include <iostream>
/*Use Point to define 2D points in an image.
Use Scalar and why it is useful
Draw a line by using the OpenCV function line
Draw an ellipse by using the OpenCV function ellipse
Draw a rectangle by using the OpenCV function rectangle
Draw a circle by using the OpenCV function circle
Draw a filled polygon by using the OpenCV function fillPoly
*/

using namespace std;
using namespace cv;

void myEllipse(Mat img, double angle, Scalar color);
void myFilledCircle(Mat img, Scalar color);
void myPolygon(Mat img, Scalar color1, Scalar color2);

#define w 400
int main(int argc, char** argv) {
	//Create black empty images
	Mat atom_image = Mat::zeros(w, w, CV_8UC3);
	Mat rook_image = Mat::zeros(w, w, CV_8UC3);

	//BGR color
	Scalar blue = {255, 0, 0};//Scalar: short vector
	Scalar green = { 0, 255, 0 };
	Scalar red = { 0, 0, 255 };
	Scalar white = { 255, 255, 255 };
	Scalar yellow = { 0, 255, 255 };
	Scalar black = { 0, 0, 0 };

	for (int i=1; i <= 4; i++) {
		myEllipse(atom_image, 45 * i, blue);
	}
	myFilledCircle(atom_image, red);

	myPolygon(rook_image, white, green);
	rectangle(rook_image, Point(0, 6 * w / 8), Point(w, w), yellow, -1);
	line(rook_image, Point(0, 7 * w / 8), Point(w, 7 * w / 8), black);
	for (int i = 1; i < 4; i++) {
		line(rook_image, Point(i*w / 4, 6 * w / 8), Point(i*w / 4, 7 * w / 8), black);
	}
	//imshow("atom", atom_image);
	imshow("root", rook_image);
	waitKey();
	destroyAllWindows();
	return 0;
}

void myEllipse(Mat img, double angle, Scalar color) {
	ellipse(img, Point(w / 2, w / 2), Size(w / 4, w / 16), angle, 0, 360, color);
}

void myFilledCircle(Mat img, Scalar color) {
	circle(img, Point(w / 2, w / 2), w / 32, color, -1);
	//thickness = -1, the circle will be drawn filled
}

void myPolygon(Mat img, Scalar color1, Scalar color2) {
	Point rook_points[1][20];
	rook_points[0][0] = Point(w / 4, 7 * w / 8);
	rook_points[0][1] = Point(3 * w / 4, 7 * w / 8);
	rook_points[0][2] = Point(3 * w / 4, 13 * w / 16);
	rook_points[0][3] = Point(11 * w / 16, 13 * w / 16);
	rook_points[0][4] = Point(19 * w / 32, 3 * w / 8);
	rook_points[0][5] = Point(3 * w / 4, 3 * w / 8);
	rook_points[0][6] = Point(3 * w / 4, w / 8);
	rook_points[0][7] = Point(26 * w / 40, w / 8);
	rook_points[0][8] = Point(26 * w / 40, w / 4);
	rook_points[0][9] = Point(22 * w / 40, w / 4);
	rook_points[0][10] = Point(22 * w / 40, w / 8);
	rook_points[0][11] = Point(18 * w / 40, w / 8);
	rook_points[0][12] = Point(18 * w / 40, w / 4);
	rook_points[0][13] = Point(14 * w / 40, w / 4);
	rook_points[0][14] = Point(14 * w / 40, w / 8);
	rook_points[0][15] = Point(w / 4, w / 8);
	rook_points[0][16] = Point(w / 4, 3 * w / 8);
	rook_points[0][17] = Point(13 * w / 32, 3 * w / 8);
	rook_points[0][18] = Point(5 * w / 16, 13 * w / 16);
	rook_points[0][19] = Point(w / 4, 13 * w / 16);

	const Point* ppt[1] = { rook_points[0] };
	int npt[] = { 20 };

	//The vertices of the polygon are the set of points in ppt
	//The total number of vertices to be drawn are npt
	fillPoly(img, ppt, npt, 2, color1);
	polylines(img, ppt, npt, 1, 1, color2);
}