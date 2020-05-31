import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return np.sqrt(2/np.pi)*np.exp(-x**2/2)
def g(x):
	return 1.5*np.exp(-x)

n=500

x=np.linspace(0,10,n)
dist=f(x) #Our favourite distribution

env=g(x) #Envelope. We will generate random numbers below this curve.

np.random.seed(0)
x1=np.random.rand(n)  #gives thousand random numbers between 0 and 1
q=-np.log(x1)
p=np.random.rand(n)*g(q)

p_bad=p[p>f(q)]
q_bad=q[p>f(q)]

p_good=p[p<f(q)]
q_good=q[p<f(q)]



fig, ax= plt.subplots(2,2)
fig.suptitle("Implementation of rejection method with {} random points".format(n))

ax[0,0].scatter(q,p,color='yellow',label="random numbers")
ax[0,1].scatter(q_bad,p_bad,color="red",label="bad points")
ax[0,1].scatter(q_good,p_good,color="green",label="good points")
ax[1,0].scatter(q_good,p_good,color="green",label="good points")
ax[1,1].hist(q_good,density=True,bins=20,label="Histogram")
for i in range(2):
	for j in range(2):
	
		ax[i,j].plot(x,dist,label="The distribution")
		ax[i,j].plot(x,env,label="Envelope")
		ax[i,j].set(xlabel="x",ylabel="frequency")   #frequency of occurence of x
		ax[i,j].legend()
		ax[i,j].label_outer()

plt.savefig("p6_plot.jpg")
plt.show()


