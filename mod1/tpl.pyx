
cimport ctpl
from libc.stdlib cimport malloc, free
from cpython.pycapsule cimport *

	
#------------------ wrappers --------------------#

def divide(x, y):
	cdef int rem
	q = ctpl.divide(x, y, &rem)
	return q, rem
