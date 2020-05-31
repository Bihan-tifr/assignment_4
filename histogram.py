import matplotlib.pyplot as plt
import numpy as np

x=np.loadtxt("data.txt")

plt.title("Random numbers drawn from exponential pdf with mean=0.5")
plt.xlabel("x")
plt.ylabel("frequency")
plt.hist(x,density=True,bins=50)
plt.savefig("p4_plot.jpg")
plt.show()

