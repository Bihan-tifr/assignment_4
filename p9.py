import matplotlib.pyplot as plt
import numpy as np

def f(x):
	if(3<=x<=7):
		return 1/4
	else:
		return 0
N=500
x=3
xl=[]
xf=[]
step=range(N)
stepl=[]
for i in step:
	x1=np.random.rand()*7  #Gives a random value, x1, between 0 and 7
	r=np.random.rand()	#Random value,r between 0 and 1
	xf.append(x1)           # All the x1 values are stored in list
	if(f(x1)/f(x)>r):
		x=x1
		stepl.append(i)
		xl.append(x)
l=np.arange(3,8,1)
y=[]
for i in range(len(l)):
	y.append(f(l[i]))

fig, ax =plt.subplots(2)

fig.suptitle("Markov chain and Implementation of Metropolis algorithm")

ax[0].plot(stepl,xl,label="Markov chain")
ax[0].scatter(step,xf,color="yellow")
ax[0].set_xlabel("step")
ax[0].set_ylabel("x")
ax[0].legend(loc="lower right")



ax[1].hist(xl,density=True,bins=10,label="Histogram")
ax[1].plot(l,y,label="uniform deviate")
ax[1].set_xlim(1,9)
ax[1].set_xlabel("x")
ax[1].set_ylabel("f(x)")
ax[1].legend(loc="lower left")
plt.show()
