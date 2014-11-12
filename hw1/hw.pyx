
cimport cython
from libc.stdlib cimport malloc, free
from libc.math cimport exp, sqrt, pow, log, erf

from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free


# print("hw!")


cpdef bsort(A): 
    '''
    bubble sort in cython w/ manual
    conversion between py lists & C arrays
    '''
    cdef int *cA
    # type casting    
    cA = <int *>malloc(len(A)*cython.sizeof(int))
    
    # static type declarations    
    cdef int count, i, j
    count = len(A)
    
    # convert python list to C array
    for i in range(count):
        cA[i] = A[i]
        
    # bubble sort
    for i in range(count):
        for j in range(1, count):
            if cA[j] < cA[j-1]:
                cA[j-1], cA[j] = cA[j], cA[j-1]
    # convert C array back to python list
    for i in range(count):
        A[i] = cA[i]
    free(cA)
    return A
	
	

@cython.cdivision(True)
cdef double std_norm_cdf(double x) nogil:
    return 0.5*(1+erf(x/sqrt(2.0)))

@cython.cdivision(True)
def black_scholes(double s, double k, double t, double v,
                 double rf, double div, double pc=True):
    '''
	returns:
	pass in:
	    s : initial stock price
	    k : strike price
	    t : expiration time
	    v : volatility
	    rf : risk-free rate
	    div : dividend
		put: True if call
	    cp : +1/-1 for call/put
    '''
    cdef double d1, d2, optprice
    with nogil:
        d1 = (log(s/k)+(rf-div+0.5*pow(v,2))*t)/(v*sqrt(t))
        d2 = d1 - v*sqrt(t)
        optprice = cp*s*exp(-div*t)*std_norm_cdf(cp*d1) - \
            cp*k*exp(-rf*t)*std_norm_cdf(cp*d2)
    return optprice
	
	