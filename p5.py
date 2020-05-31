import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
n=10000
np.random.seed(0)
x1=np.random.rand(n)
np.random.seed(2)
x2=np.random.rand(n)

y1=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
y2=np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)

plt.title("Random Numbers drawn from gaussian pdf obtained using box muller method")
plt.hist(y1,density=True,bins=100,label="histogram")
sns.distplot(np.random.normal(size=10000), hist=False,label="Normal pdf")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("p5.jpg")
plt.show()



