#include <stdio.h>
#include <math.h>


int gcd(int x, int y) {
	int g = y;
	while (x > 0) {
		g = x;
		x = y % x;
		y = g;
	}
	return g;
}

double avg(double *a, int n) {
	int i;
	double total = 0.0;
	for (i=0; i<n; i++) {
		total += a[i];
	}
	return total/n;
}





