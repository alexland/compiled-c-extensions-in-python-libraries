#!/usr/local/bin/python
# encoding: utf-8

import os
import sys
import numpy as NP
from matplotlib import pyplot as PLT

# conjugate gradient

NP.set_printoptions(precision=3, suppress=True, linewidth=120)


def jacobian(x):
	#return NP.array([.4*x[0],2*x[1]])
	return NP.array([x[0], .4*x[1], 1.2*x[2]])


def hessian(x):
	#return NP.array([[.2,0],[0,1]])
	return NP.array( [[1, 0, 0],[0, 0.4, 0],[0, 0, 1.2]] )


def conjugate_gradient(x0) :
	i, k = 0, 0
	r = -jacobian(x0)
	p = r
	betaTop = NP.dot(r.T,r)
	beta0 = betaTop
	iMax = 3
	epsilon = 10**(-2)
	jMax = 5
	# restart every nDim iterations
	nRestart = NP.shape(x0)[0]
	x = x0
	while i < iMax and betaTop > epsilon**2*beta0:
		j = 0
		dp = NP.dot(, p)
		alpha = (epsilon+1)**2
		# Newton-Raphson iteration
		while j < jMax and alpha**2 * dp > epsilon**2:
			# line search
			alpha = -NP.dot(jacobian(x).T, p) / ( NP.dot(p.T,
						NP.dot(hessian(x),p)) )
			print("N-R {0} {1} {2}".format(x, alpha, p))
			x += alpha * p
			j += 1
		print(x)
		# now construct beta
		r = -jacobian(x)
		print("r: {0}".format(r))
		betaBottom = betaTop
		betaTop = NP.dot(r.T, r)
		beta = betaTop / betaBottom
		print("beta: {0}".format(beta))
		# update estimate
		p = r + beta * p
		print("p: {0}".format(p))
		print("----")
		k += 1
		if (k == nRestart) or (NP.dot(r.T, p) <= 0) :
			p = r
			k = 0
			print("restarting")
		i += 1
	print(x)



x0 = NP.array([-2, 2, -2])

conjugate_gradient(x0)


#------------------ Plotting -------------------#

fig = PLT.figure()

ax1 = fig.add_subplot(111)

ax1.plot()

PLT.show()


