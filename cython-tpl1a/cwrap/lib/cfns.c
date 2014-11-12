#include <stdio.h>
#include <stdlib.h>
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

double k2c(double k) {
	return k - 273.15;
}

double avg(double *a, int n) {
	int i; 
	double total = 0.0;
	for (i=0; i<n; i++) {
		total += a[i];
	}
	return total / n;
}

int dv(int a, int b, int *rem) {
	int q = a / b;
	*rem = a % b;
	return q;
}

double ddv(double a, double b) {
	double q = a / b;
	return q;
}



