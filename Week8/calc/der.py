import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

## Define the Function
f = lambda x: 4*x**3 + 7*x**2 - 3*x +2 

## Set the range in X
x = np.arange(-10, 10, 0.1 )

## Take the 1st derivative
first = derivative(f, x, dx=0.1, n=1 )

## Take the 2nd derivative
second = derivative(f, x, dx=0.1, n=2)

#print(first)
#print(second)

fig, ax = plt.subplots(3,1, sharex= True)

## Plot Original Function
ax[0].plot(x, f(x))
ax[0].set_ylabel('f(x)')

## Plot f'(x)
ax[1].plot(x, first)
ax[1].set_ylabel('f\'\'(x)') 

## Plot f''(x)
ax[2].plot(x, second)
ax[2].set_ylabel('f\'\'\'(x)') 

plt.show()
