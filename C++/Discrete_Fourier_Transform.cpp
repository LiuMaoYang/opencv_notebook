#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>
/*
H(k) = 1/N * sum(h(x) * exp(-jwx))
w = 2 * pi * k / N
*/

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
	String path = "F:/Desktop/1.JPG";
	Mat img = imread(path, 0);

	/*
	expand input image to optimal size
	it usually makes sense to pad the input data with zeros to get a bit 
	larger array that can be transformed much faster than the original one
	getOptimalDFTSize is used to padded a array to 2^p * 3^q * 5^r
	*/
	Mat padded;
	int m = getOptimalDFTSize(img.rows);
	int n = getOptimalDFTSize(img.cols);
	//top=1, bottom=1, left=1, right=1 mean that 1 pixel-wide border needs to be built.
	copyMakeBorder(img, padded, 0, m - img.rows, 0, n - img.cols, 
					BORDER_CONSTANT, Scalar::all(0));
	
	/*
	Make place for both the complex and the real values. 
	The result of a Fourier Transform is complex. This implies that for each image value the result is 
	two image values (one per component). Moreover, the frequency domains range is much larger than its spatial counterpart. 
	Therefore, we store these usually at least in a float format. 
	Therefore we¡¯ll convert our input image to this type and expand it with another channel to hold the complex values:
	*/
	Mat planes[] = { Mat_<float>(padded), Mat::zeros(padded.size(), CV_32F) };
	cout << planes[0].size() << planes[1].size() << endl;

	Mat complexI;
	merge(planes, 2, complexI); // Add to the expanded another plane with zeros

	dft(complexI, complexI); // this way the result may fit in the source matrix

	// compute the magnitude and switch to logarithmic scale
	// => log(1 + sqrt(Re(DFT(I))^2 + Im(DFT(I))^2))
	split(complexI, planes); // planes[0] = Re(DFT(I), planes[1] = Im(DFT(I))
	magnitude(planes[0], planes[1], planes[0]); // planes[0] = magnitude
	Mat magI = planes[0]; // M = sqrt(Re^2 + Im^2)

	/*
	Switch to a logarithmic scale. It turns out that the dynamic range of 
	the Fourier coefficients is too large to be displayed on the screen. 
	We have some small and some high changing values that we can¡¯t observe like this. 
	Therefore the high values will all turn out as white points, while the small ones as black.
	*/
	// switch to logarithmic scale
	magI += Scalar::all(1); 
	log(magI, magI); // M1 = log(1+M)

	// crop the spectrum, if it has an odd number of rows or columns
	magI = magI(Rect(0, 0, magI.cols & -2, magI.rows & -2)); // x & -2 return even num <= x

	// rearrange the quadrants of Fourier image  so that the origin is at the image center
	int cx = magI.cols / 2;
	int cy = magI.rows / 2;

	Mat q0(magI, Rect(0, 0, cx, cy));   // Top-Left - Create a ROI per quadrant
	Mat q1(magI, Rect(cx, 0, cx, cy));  // Top-Right
	Mat q2(magI, Rect(0, cy, cx, cy));  // Bottom-Left
	Mat q3(magI, Rect(cx, cy, cx, cy)); // Bottom-Right

	Mat tmp; // swap quadrants (Top-Left with Bottom-Right)
	q0.copyTo(tmp);
	q3.copyTo(q0);
	tmp.copyTo(q3);

	q1.copyTo(tmp); // swap quadrant (Top-Right with Bottom-Left)
	q2.copyTo(q1);
	tmp.copyTo(q2);

	// Transform the matrix with float values into a
	// viewable image form (float between values 0 and 1).
	normalize(magI, magI, 0, 1, CV_MINMAX);

	imshow("Input", img);
	imshow("spectrum magnitude", magI);

	waitKey();
	destroyAllWindows();
	return 0;
}

