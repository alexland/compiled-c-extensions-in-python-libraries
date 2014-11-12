#!/usr/local/bin/python3


import numpy as NP


def dm(M):
	'''
	returns: mxm matrix of pairwise Euclidean distances,
		for all points in M
	pass in: mxn matrix in which rows are data points, 
		cols are features
	'''
	m, n = M.shape
	dm = NP.zeros(shape=(m, m))
	for idx_col in range(n):
		col = M[:,idx_col].reshape(-1, 1)
		del_col = col - col.reshape(1, -1)
		dm += del_col ** del_col
	return NP.sqrt(dm)