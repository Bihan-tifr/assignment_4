import matplotlib.pyplot as plt
import numpy as np
def lcg(n,x0,a,c,m):
	uu=[]
	xn=x0
	for i in range(n):
		xn=(a*xn+c)%m
		uu.append(xn/m)
	return uu

n=10000
a=1103515245
c=12345
m=2**32
x=np.linspace(0,1,10)
y=np.empty((10))
y.fill(1)
s=lcg(n,0,a,c,m)
plt.hist(s,density=True,bins=50,label="linear congruential numbers")
plt.plot(x,y,label="uniform pdf")
plt.xlabel("x")
plt.ylabel("numbers in each bin,pdf")
plt.legend(loc="lower right")
plt.savefig("plot1.jpg")
plt.show()

