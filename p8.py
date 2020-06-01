#Area of the circle=4*area under the circular segment in first quadrant, if origin is at the center of circle.


import matplotlib.pyplot as plt
import numpy as np
def f(x):
	return np.sqrt(1-x**2)
x=np.linspace(0,1,100)
y=f(x)

N=1000
x1=np.random.rand(N)
y1=np.random.rand(N)

k=0
for i, arg in enumerate(x1):
	if(y1[i]<f(x1[i])):
		k+=1
print("Monte Carlo integral result: I={}".format(k/N)) #A=1
print("Therefore total area of the circle: A_circle=4I={}".format(4*k/N)) #Total area=4*area in first quadrant

plt.title("Monte Carlo integration to find the area of a circle of unit radius")
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(x,y,label="quarter of a circle")
plt.scatter(x1,y1,color="yellow",label="random {} points".format(N))
plt.xlabel("x")
plt.ylabel("y")
plt.show()



