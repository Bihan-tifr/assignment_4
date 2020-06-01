import matplotlib.pyplot as plt
import numpy as np

x=np.loadtxt("data.txt")
x0=np.linspace(0,5,100)
y0=2*np.exp(-2*x0)  #The exponential pdf with mean 0.5

plt.title("Random numbers drawn from exponential pdf with mean=0.5")
plt.xlabel("x")
plt.ylabel("frequency")
plt.hist(x,density=True,bins=50)
plt.plot(x0,y0,label="exponential pdf with mean 0.5")
plt.savefig("p4_plot.jpg")
plt.legend()
plt.show()

