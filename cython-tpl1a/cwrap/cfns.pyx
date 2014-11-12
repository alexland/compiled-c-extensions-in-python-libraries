
# TODO: type index (idx) in tesselate fn

cimport cython
import numpy as NP
cimport numpy as NP
from libc.stdlib cimport malloc, free


DTYPE = NP.float
ctypedef NP.float_t DTYPE_t

#   - making a wrapped c function on python types w/ cython syntax, "factorial"
#   - c function that takes an ndarray array and returns a scalar, "array_sum"
#   - c function that takes an ndarray and returns an ndarray "tesselation"


cdef extern from "lib/cfns.h":
	# an extern Cython block--a declaration block to tell Cython
	# which C-constructs we wish to use from a specific C header file
	# imports definitions from a c header file
	# corresponding source file (cfunc.c) must be added to
	# extension definition in setup.py for proper compiling & linking
	int gcd(int, int)
	double k2c(double)
	double avg(double *, int) nogil
	int dv(int, int, int *)
	double ddv(double, double)
	
	
def cgcd(unsigned int x, unsigned int y):
	return gcd(x, y)
	
	
def ck2c(float k):
	return k2c(k)

# @cython.profile(True)
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def cavg(double[:] a):
	'''
	returns: scalar
	pass in: memoryview of a 1D array of doubles,
	either NumPy or array.array
	'''
	cdef:
		int sz
		double result
	sz = a.size
	with nogil:
		# type cast a pointer to a different type
		# using <double *> &a, if necessary
		# to ensure that avg() receives a pointer
		# of the correct type
		result = avg(<double *> &a[0], sz)
	return result


def cdv(a, b):
	'''
	shows how to handle a pointer argument; 
	'''
	cdef int rem0
	q = dv(a, b, &rem0)
	return q, rem0

def cddv(double a, double b):
	'''
	'''
	return ddv(a, b)
	 


# def factorial(int x):
# 	# basic ex of cython fn, which defines python-like
# 	# operations & control flow on defined c types
# 	cdef int m = x
# 	cdef int i
# 	if x <= 1:
# 		return 1
# 	else:
# 		for i in range(1, x):
# 			m = m * i
# 		return m
#
# # decorator turns off bounds-checking for speed
# @cython.boundscheck(False)
# def array_sum(double[:, ::1] A):
# 	# function passed an ndarray returns a scalar
# 	cdef int m = A.shape[0]
# 	cdef int n = A.shape[1]
# 	cdef unsigned int i, j, k
# 	cdef double result = 0
# 	for i in range(m):
# 		for k in range(n):
# 			result += A[i, k]
# 	return result
#
#
# @cython.boundscheck(False)
# def tessellate(double[:, ::1] A):
# 	# example of array function that returns a new ndarray
# 	# turns indices of an m by n array into an 2mn by 12 array of triangle
# 	# faces, as per the STL file format
# 	cdef int m = A.shape[0]
# 	cdef int n = A.shape[1]
# 	cdef int i, j, k, idx
# 	cdef double i_ = 0
# 	cdef double k_ = 0
#
# 	cdef double[:, ::1] results = NP.zeros([2 * m * n, 12])
#
# 	for i in range(m - 1):
# 		for k in range(n - 1):
# 			idx = <unsigned int> i * n + k
# 			results[idx, 3] = i_
# 			results[idx, 4] = k_ + 1
# 			results[idx, 5] = A[i, k + 1]
#
# 			results[idx, 6] = i_
# 			results[idx, 7] = k_
# 			results[idx, 8] = A[i, k]
#
# 			results[idx, 9] = i_ + 1
# 			results[idx, 10] = k_ + 1
# 			results[idx, 11] = A[i + 1, k + 1]
#
# 			results[idx + 1, 3] = i_
# 			results[idx + 1, 4] = k_
# 			results[idx + 1, 5] = A[i, k]
#
# 			results[idx + 1, 6] = i_ + 1
# 			results[idx + 1, 7] = k_
# 			results[idx + 1, 8] = A[i + 1, k]
#
# 			results[idx + 1, 9] = i_ + 1
# 			results[idx + 1, 10] = k_ + 1
# 			results[idx + 1, 11] = A[i + 1, k + 1]
#
# 			i_ += 1
# 			k_ += 1
#
# 	return results
