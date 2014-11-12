
#include <math.h>
#include <stdio.h>
#include <ctype.h>


int divide(int a, int b, int *remainder) {
	int q = a / b;
	*remainder = a % b;
	return q;
}