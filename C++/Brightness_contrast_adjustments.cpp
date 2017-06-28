#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <string>
#include <iostream>
/*Changing the contrast and brightness of an image
Image Processing
A general image processing operator is a function that 
takes one or more input images and produces an output image.
Image transforms can be seen as:
Point operators (pixel transforms)
Neighborhood (area-based) operators

Pixel Transforms
In this kind of image processing transform, each output pixel¡¯s value depends on 
only the corresponding input pixel value (plus, potentially, some globally collected information or parameters).
Examples of such operators include brightness and contrast adjustments as well as color correction and transformations.

Brightness and contrast adjustments
Two commonly used point processes are multiplication and addition with a constant:
g(x) = alpha f(x) + beta, where alpha > 0 and beta are often called gain and bias respectively

Instead of using the for loops to access each pixel, we could have simply used this command:
image.convertTo(new_image, -1, alpha, beta);
where convertTo would effectively perform new_image = alpha *image + beta
*/

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
	String path = "F:/Desktop/1.JPG";
	
	Mat src = imread(path, 1);
	Mat dst = Mat::zeros(src.size(), src.type());

	double alpha, beta;
	cin >> alpha >> beta;

	cout << "Basic Linear Transforms " << endl;
	cout << "----------------------------" << endl;
	cout << "alpha: " << alpha << ", beta: " << beta << endl;

	for (int i = 0; i < src.rows; i++)
		for (int j = 0; j < src.cols; j++)
			for (int c = 0; c < src.channels(); c++)
				//Vec3b: (B,G,R) uchar: 0~255
				//saturate_cast<T>(): Template function for accurate conversion from one primitive type to another
				dst.at<Vec3b>(i, j)[c] = saturate_cast<uchar>(alpha * src.at<Vec3b>(i, j)[c] + beta);

	namedWindow("Original", 1);
	namedWindow("New", 1);
	imshow("Original", src);
	imshow("New", dst);
	waitKey();

	destroyAllWindows();
	return 0;
}