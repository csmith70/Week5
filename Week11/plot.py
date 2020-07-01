import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return np.cos(x) - x**2
x1 = np.arange(0,1.2,0.2)
plt.ylim(-0.5,1)
plt.plot(x1, f(x1))
plt.hlines(0,0,1)
plt.show()
#x = np.linspace(0,1,100)
#y = np.cos(x) - x**2

