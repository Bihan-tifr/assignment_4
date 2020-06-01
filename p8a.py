#Volume of a 10d sphere using Monte Carlo Integration

import matplotlib.pyplot as plt
import numpy as np
import math as m
def f(x):
	s=0
	for i in range(len(x)):
		s+=x[i]**2
	if(s>1):
		return 0
	else:
		return 1

N=100000
k=0
for i in range(N):
	x=np.random.rand(10) #To find a random number array of size 10, all elements between 0 and 1
	k+=f(x)
I=k/N*2**10 

#Volume of 10d sphere, 2**10 is volume of 10 d cube, where N random points reside. Among these N numbers, k number of points are inside 10d sphere as well 

V=(np.pi**(5))/m.factorial(5) #Analytical result of 10d sphere volume

	
print("Volume of 10d sphere by Monte Carlo method: {}".format(I))
print("Actual volume of 10d sphere:{} ".format(V))
