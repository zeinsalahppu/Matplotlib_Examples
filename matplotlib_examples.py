"""
simple matplotlib Examples

"""


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(2*x) - np.cos(x) + 1

def integrate(f, a, b, N):
    dx = (b-a)/N
    x = np.linspace(a+dx/2, b-dx/2, N)
    fx = f(x)
    fig, ax = plt.subplots()

    ax.plot(x, fx, color='blue', alpha=1.00)
    ax.fill_between(x, fx, 0, color='cyan', alpha=.2)



    area = np.sum(fx)*dx
    return area

print(integrate(f, -6, 6, 100))
plt.show()