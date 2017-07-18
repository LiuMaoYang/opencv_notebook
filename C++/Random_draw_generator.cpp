#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;
using namespace cv;

/// Global Variables
const int DELAY = 5;
const int window_width = 900;
const int window_height = 600;

static Scalar randomColor(RNG &rng);
void Drawing_Random_lines(Mat img, char *window_name, RNG rng);
void Drawing_Random_Ellipses(Mat img, char* window_name, RNG rng);
void Drawing_Random_Circles(Mat img, char* window_name, RNG rng);
void Drawing_Random_Rectangles(Mat img, char* window_name, RNG rng);
void Drawing_Random_Polylines(Mat img, char* window_name, RNG rng);

#define random(a,b) rand()%(b-a+1)+a
int main(int argc, char** argv) {
	//RNG implements a random number generator. In this example
	//rng is a RNG element initialized with the value 0xFFFFFFFF
	RNG rng(0xFFFFFFFF);

	// Initialize a matrix filled with zeros
	Mat img = Mat::zeros(window_height, window_width, CV_8UC3);
	// Show it in a window during DELAY ms
	char window_name[] = "pic";
	imshow(window_name, img);
	waitKey(DELAY);
	
	int num;
	cin >> num;
	cout << "Generate " << num << " kinds of shape:" << endl;
	for (int i = 0; i < num; i++) {
		int idx = rng.uniform(1, 6);
		switch (idx){
		case 1:
			Drawing_Random_lines(img, window_name, rng);
			break;
		case 2:
			Drawing_Random_Ellipses(img, window_name, rng);
			break;
		case 3:
			Drawing_Random_Circles(img, window_name, rng);
			break;
		case 4:
			Drawing_Random_Rectangles(img, window_name, rng);
			break;
		case 5:
			Drawing_Random_Polylines(img, window_name, rng);
			break;
		}
	}
	
	waitKey();
	destroyAllWindows();
	return 0;
}

/// Function definitions
/**
* @function randomColor
* @brief Produces a random color given a random object
*/
static Scalar randomColor(RNG &rng) {
	int icolor = (unsigned)rng;
	return Scalar(icolor & 255, (icolor >> 8) & 255, (icolor >> 16) & 255);//R,G,B
}

void Drawing_Random_lines(Mat img, char *window_name, RNG rng) {
	int num = rng.uniform(1, 50);
	cout << "Random draw " << num << " line" << endl;
	for (int i = 0; i < num; i++) {
		Point pt1, pt2;
		pt1.x = rng.uniform(0, window_width);
		pt2.x = rng.uniform(0, window_width);
		pt1.y = rng.uniform(0, window_height);
		pt2.y = rng.uniform(0, window_height);

		line(img, pt1, pt2, randomColor(rng), rng.uniform(1, 10));
		/*if (waitKey(DELAY) >= 0)
			return -1;*/
	}
	//return 0;
	imshow(window_name, img);
}

void Drawing_Random_Ellipses(Mat img, char* window_name, RNG rng) {
	int num = rng.uniform(1, 10);
	cout << "Random draw " << num << " ellipses" << endl;
	for (int i = 0; i < num; i++) {
		Point center;
		Size axes;
		double angle;

		center.x = rng.uniform(0, window_width / 2);
		center.y = rng.uniform(0, window_height / 2);
		axes.height = rng.uniform(0, window_height / 2);
		axes.width = rng.uniform(0, window_width / 2);
		angle = rng.uniform(0, 360);
		ellipse(img, center, axes, angle, 0, 360, randomColor(rng), rng.uniform(-1, 10));
	}
	imshow(window_name, img);
}

void Drawing_Random_Rectangles(Mat img, char* window_name, RNG rng) {
	int num = rng.uniform(1, 5);
	cout << "Random draw " << num << " rectangles" << endl;
	for (int i = 0; i < num; i++) {
		Point p1, p2;
		p1.x = rng.uniform(0, window_width);
		p1.y = rng.uniform(0, window_height);
		p2.x = rng.uniform(0, window_width);
		p2.y = rng.uniform(0, window_height);
		rectangle(img, p1, p2, randomColor(rng), rng.uniform(-1, 10));
	}
	imshow(window_name, img);
}

void Drawing_Random_Polylines(Mat img, char* window_name, RNG rng) {
	cout << "Random draw " << 1 << " Polylines" << endl;
	int size1 = 2;
	int size2 = 3;
	Point pt[2][3];
	for (int i = 0; i < size1; i++)
		for (int j = 0; j < size2; j++) {
			pt[i][j].x = rng.uniform(0, window_width);
			pt[i][j].y = rng.uniform(0, window_height);
		}
	const Point* ppt[2] = { pt[0],pt[1] };
	int npt[] = { 3,3 };
	polylines(img, ppt, npt, 2, true, randomColor(rng), rng.uniform(-1, 10));
	imshow(window_name, img);
}

void Drawing_Random_Circles(Mat img, char* window_name, RNG rng) {
	int num = rng.uniform(1, 5);
	cout << "Random draw " << num << " circles" << endl;
	for (int i = 0; i < num; i++) {
		Point center;
		center.x = rng.uniform(0, window_width);
		center.y = rng.uniform(0, window_height);
		int r = rng.uniform(1, 100);
		circle(img, center, r, randomColor(rng), rng.uniform(-1, 10));
	}
	imshow(window_name, img);
}

/*void Displaying_Random_Text(Mat img, char* window_name, RNG rng) {
	int num = rng.uniform(1, 10);
	cout << "Random print " << num << " char" << endl;
	for (int i = 0; i < num; i++) {
		Point pt;
		pt.x = rng.uniform(0, window_width);
		pt.y = rng.uniform(0, window_height);
		int c = rng.uniform(33, 127);
		putText(img, (char) c, pt, rng.uniform(0.8),
			rng.uniform(0, 100)*0.05 + 0.1, randomColor(rng), rng.uniform(1, 10));
	}
}*/