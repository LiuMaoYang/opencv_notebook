#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <highgui.h>
#include <stdlib.h>
#include <stdio.h>

/*
Morphological Operations
In short: A set of operations that process images based on shapes.
Morphological operations apply a structuring element to an input image and generate an output image.
The most basic morphological operations are two: Erosion(腐蚀) and Dilation（膨胀）.
They have a wide array of uses, i.e. :
Removing noise
Isolation of individual elements and joining disparate elements in an image.
Finding of intensity bumps or holes in an image

Theta(f, t) = 1, if f >=t
0, else
c = f 异或 s 
• dilation: dilate(f, s) = Theta(c, 1);
• erosion: erode(f, s) = Theta(c, S);
• majority: maj(f, s) = Theta(c, S / 2);
• opening: open(f, s) = dilate(erode(f, s), s);
• closing: close(f, s) = erode(dilate(f, s), s)
*/

using namespace cv;

// Global variables
Mat img, erosion_dst, dilation_dst, morphology_dst;

int erosion_elem = 0;
int erosion_size = 0;
int dilation_elem = 0;
int dilation_size = 0;
int morph_elem = 0;
int morph_size = 0;
int morph_operator = 0;
int const max_operator = 4;
int const max_elem = 2;
int const max_kernel_size = 21;

void Erosion(int, void*);
void Dilation(int, void*);
void Morphology_Operations(int, void*);

int main() {
	String path = "F:/Desktop/2.JPG";
	Mat img = imread(path);

	namedWindow("Erosion Demo", CV_WINDOW_AUTOSIZE);
	namedWindow("Dilation Demo", CV_WINDOW_AUTOSIZE);
	namedWindow("Morphology Operations Demo", CV_WINDOW_AUTOSIZE);

	cvMoveWindow("Dilation Demo", img.cols, 0); //Moves window to the specified position
	cvMoveWindow("Morphology Operations Demo", 0, img.rows);

	// Create Erosion Trackbar
	/* C++: int createTrackbar(const string& trackbarname, const string& winname,
				int* value, int count, TrackbarCallback onChange=0, void* userdata=0)
	*/
	createTrackbar("Element:\n 0: Rect - 1: Cross - 2: Ellipse", "Erosion Demo",
		&erosion_elem, max_elem, Erosion);
	createTrackbar("Kernel size:\n 2n+1", "Erosion Demo",
		&erosion_size, max_kernel_size, Erosion);

	createTrackbar("Element:\n 0: Rect - 1: Cross - 2: Ellipse", "Dilation Demo",
		&dilation_elem, max_elem, Dilation);
	createTrackbar("Kernel size:\n 2n+1", "Dilation Demo",
		&dilation_size, max_kernel_size, Dilation);

	createTrackbar("Operator:\n 0: Opening - 1: Closing \n 2: Gradient - 3: Top Hat - 4: Black Hat",
		"Morphology Operations Demo", &morph_operator, max_operator, Morphology_Operations);
	createTrackbar("Element:\n 0: Rect - 1: Cross - 2: Ellipse", "Morphology Operations Demo",
		&morph_elem, max_elem, Morphology_Operations);
	createTrackbar("Kernel size:\n 2n+1", "Morphology Operations Demo",
		&morph_size, max_kernel_size, Morphology_Operations);

	Erosion(0, 0);
	Dilation(0, 0);
	Morphology_Operations(0, 0);

	waitKey(0);
	return 0;
}

/*
Erosion
This operation is the sister of dilation. What this does is to compute a local minimum over the area of the kernel.

As the kernel B is scanned over the image, we compute the minimal pixel value overlapped by B and
replace the image pixel under the anchor point with that minimal value.
*/
void Erosion(int, void*) {
	// Mat getStructuringElement(int shape, Size ksize, Point anchor=Point(-1,-1))
	int type;
	if (erosion_elem == 0) { type = MORPH_RECT; }
	else if (erosion_elem == 1) { type = MORPH_RECT; }
	else if (erosion_elem == 2) { type = MORPH_RECT; }

	Size ksize = { 2 * erosion_size + 1, 2 * erosion_size + 1 };
	Mat element = getStructuringElement(type, ksize, Point(erosion_size, erosion_size));

	erode(img, erosion_dst, element);
	imshow("Erosion Demo", erosion_dst);
}

/*
Dilation
This operations consists of convoluting an image A with some kernel (B),
which can have any shape or size, usually a square or circle.

The kernel B has a defined anchor point, usually being the center of the kernel.

As the kernel B is scanned over the image, we compute the maximal pixel value
overlapped by B and replace the image pixel in the anchor point position with that maximal value.
As you can deduce, this maximizing operation causes bright regions within an image to “grow”
(therefore the name dilation).
*/
void Dilation(int, void*) {
	int type;
	if (dilation_elem == 0) { type = MORPH_RECT; }
	else if (dilation_elem == 1) { type = MORPH_RECT; }
	else if (dilation_elem == 2) { type = MORPH_RECT; }

	Size ksize = { 2 * dilation_size + 1, 2 * dilation_size + 1 };
	Mat element = getStructuringElement(type, ksize, Point(dilation_size, dilation_size));

	erode(img, dilation_dst, element);
	imshow("Dilation Demo", dilation_dst);
}

void Morphology_Operations(int, void*) {
	int type;
	if (morph_elem == 0) { type = MORPH_RECT; }
	else if (morph_elem == 1) { type = MORPH_RECT; }
	else if (morph_elem == 2) { type = MORPH_RECT; }

	int operation;
	if (morph_operator == 0) { operation = MORPH_OPEN; }
	else if (morph_operator == 1) { operation = MORPH_CLOSE; }
	else if (morph_operator == 2) { operation = MORPH_GRADIENT; }
	else if (morph_operator == 3) { operation = MORPH_TOPHAT; }
	else if (morph_operator == 4) { operation = MORPH_BLACKHAT; }

	Size ksize = { 2 * morph_size + 1, 2 * morph_size + 1 };
	Mat element = getStructuringElement(type, ksize, Point(morph_size, morph_size));

	morphologyEx(img, morphology_dst, operation, element);
	imshow("Morphology Operations Demo", morphology_dst);
}