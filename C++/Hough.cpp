#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

/*
Hough Line Transform
The Hough Line Transform is a transform used to detect straight lines.
To apply the Transform, first an edge detection pre-processing is desirable.

y = -tan(theta) * x + r / sin(theta)
r = x * cos(theta) + y * sin(theta)
*/

using namespace cv;

Mat src, dst, cdst;

char* windowName = "Hough Demo";
char* type_name = "type";
char* thre_name = "threshold";

int type = 2;
int thre = 100;

int const max_type = 2;
int const max_thre = 255;

void op(int, void*);
int main() {
	String path = "F:/Desktop/2.JPG";
	src = imread(path, 1);
	namedWindow(windowName, CV_WINDOW_AUTOSIZE);

	createTrackbar(type_name, windowName, &type, max_type, op);
	createTrackbar(thre_name, windowName, &thre, max_thre, op);
	
	op(0, 0);
	while (1){
		int c;
		c = waitKey(5);
		if ((char)c == 27)
			break;
	}

	destroyAllWindows();
	return 0;
}

void op(int, void*) {
	//Canny(src, dst, 50, 200);
	cvtColor(src, dst, CV_GRAY2BGR);
	GaussianBlur(dst, cdst, Size(9, 9), 2, 2);

	if (type == 0) {
		/* Standard Hough Line Transform
		void HoughLines(InputArray image, OutputArray lines, double rho, double theta,
		int threshold, double srn=0, double stn=0 )
		rho : The resolution of the parameter r in pixels. We use 1 pixel.
		theta: The resolution of the parameter \theta in radians. We use 1 degree (CV_PI/180)
		threshold: The minimum number of intersections to “detect” a line
		*/
		vector<Vec2f> lines;
		HoughLines(cdst, lines, 1, CV_PI / 180, thre);

		//display the result by drawing the lines
		for (int i = 0; i < lines.size(); i++) {
			float rho = lines[i][0], theta = lines[i][1];
			Point pt1, pt2;
			double a = cos(theta), b = sin(theta);
			double x0 = rho * a, y0 = rho * b;

			pt1.x = cvRound(x0 + 1000 * (-b));
			pt1.y = cvRound(y0 + 1000 * (a));
			pt2.x = cvRound(x0 - 1000 * (-b));
			pt2.y = cvRound(y0 - 1000 * (a));

			line(src, pt1, pt2, Scalar(0, 255, 0), 3);
		}
	}
	else if (type == 1) {
		//Probabilistic Hough Line Transform
		vector<Vec4i> lines;
		HoughLinesP(cdst, lines, 1, CV_PI / 180, thre);

		for (int i = 0; i < lines.size(); i++) {
			line(src, Point(lines[i][0], lines[i][1]), Point(lines[i][2], lines[i][3]), Scalar(0, 0, 255), 3);
		}
	}
	else if (type == 1) {
		vector<Vec3f> circles;
		HoughCircles(cdst, circles, CV_HOUGH_GRADIENT, cdst.rows / 8, thre);

		for (size_t i = 0; i < circles.size(); i++)
		{
			Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
			int radius = cvRound(circles[i][2]);
			// circle center
			circle(src, center, 3, Scalar(0, 255, 0), -1, 8, 0);
			// circle outline
			circle(src, center, radius, Scalar(0, 0, 255), 3, 8, 0);
		}
	}

	imshow(windowName, src);
}
