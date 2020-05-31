import numpy as np
import matplotlib.pyplot as plt

x=np.random.rand(10000)
plt.hist(x,density=True,bins=50,label="histogram of random numbers")

y=np.linspace(0,1,10)
z=np.empty((10))
z.fill(1)
plt.plot(y,z,label="uniform pdf")

plt.xlabel("x")
plt.ylabel("numbers per bin,pdf")
plt.legend(loc="lower right")
plt.savefig("plot2.jpg")
plt.show()

