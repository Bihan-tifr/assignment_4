import matplotlib.pyplot as plt
import numpy as np

def log_L(par,x,y,sigma):
	a,b,c=par
	model=a*x**2+b*x+c
	sigma2=sigma**2
	
	return 0.5*np.sum(np.log(2*np.pi*sigma2)+(y-model)**2/(2*sigma2))  #returns -ln(Likelihood)
def log_prior(par):
	a,b,c=par
	if -500<a<500 and -500<b<500 and -500.0<c<500.0 :                    #our prior probability distribution
		return 0.0
	return -np.inf
def log_post(par,x,y,sigma):
	lp=log_prior(par)
	if not np.isfinite(lp):						#Posterior probability distribution
		return -np.inf
	return lp-log_L(par,x,y,sigma)

from scipy.optimize import minimize

data=np.loadtxt("data10.txt",delimiter='&')	#loading data from file and storing it to x,y and sigma.
x=data[:,1]
y=data[:,2]
sigma=data[:,3]
print(x,y,sigma)

guess=(1.0,2.0,1.0)				#Our initial guess for parameters
soln=minimize(log_L,guess,args=(x,y,sigma)) 

nwalkers, ndim = 50,3

pos=soln.x+ 1e-4*np.random.randn(nwalkers, ndim)	#initializing markov chain

import emcee

sampler=emcee.EnsembleSampler(nwalkers,ndim,log_post,args=(x,y,sigma))
sampler.run_mcmc(pos,4000)						#Getting markov chains with 4000 steps
samples=sampler.get_chain()
p_data=sampler.get_chain(discard=200,thin=10,flat=True)			#flattening data

fig, ax=plt.subplots(3)
fig.suptitle("Markov chains")
ax[0].plot(samples[:,:,0])
ax[0].set_ylabel("a")
ax[1].plot(samples[:,:,1])
ax[1].set_ylabel("b")							#plot of markov chains, three parameters vs steps
ax[2].plot(samples[:,:,2])
ax[2].set_xlabel("steps")
ax[2].set_ylabel("c")
plt.savefig("Markov_chain.jpg")
plt.show()


import corner

medians=np.median(p_data,axis=0)
a_true,b_true,c_true=medians			#finding out parameter values for best fit

la=["a","b","c"]
figu=corner.corner(p_data,labels=la,truths=[a_true,b_true,c_true])
figu.savefig("corner.jpg")						#corner plots showing parameter variation

figa=plt.figure()

x0=np.linspace(40,300,1000)
y_best=a_true*x0**2+b_true*x0+c_true					#Best fit for our model!
pts=np.random.randint(len(p_data), size=200)
for j in pts:
	s=p_data[j]
	a,b,c=s[:3]
	y_rand=a*x0**2+b*x0+c						#plotting random 200 models about the best fit model
	plt.plot(x0,y_rand,'y')						
plt.errorbar(x,y,yerr=sigma,fmt=".k",capsize=3,label="data with errorbars")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x0,y_best,"g",label="best fit")				#plotting the best fit model
plt.legend()
plt.savefig("p10.jpg")
plt.show()





































