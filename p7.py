#Please See the attached .ods file. V1,V2 for two observations are calculated there. We found, V1=29.492,V2=1.417. We start from this point.
from scipy import stats
import numpy as np

v1=29.492
v2=1.417

#What is the probability of V>=v1,v2?

s1=1.0-stats.chi2.cdf(v1,10.0) 
s2=1.0-stats.chi2.cdf(v2,10.0)
s=np.array([s1,s2])
u=100*s #percentage
print(100*s1,100*s2)

for i in range(2):
	x=u[i]
	print("Observation {} is".format(i+1))
	if( x<=1 or x>=99):
		print("Not sufficiently random")
	if(1<x<5 or 95<x<99):
		print("Suspect")
	if(5<=x<10 or 90<x<=95):
		print("Almost suspect")
	if(10<=x<=90):
		print("Sufficiently random")	

