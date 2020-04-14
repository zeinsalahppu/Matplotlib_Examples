"""
simple matplotlib Examples

"""


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

f_sin = 3*np.sin(x)
f_poly = np.sin(2*x) - np.cos(x)

fig, ax = plt.subplots()

startx, endx = -2 * np.pi - 0.1, 2*np.pi + 0.1
starty, endy = -4.0, 4.0
ax.axis([startx, endx, starty, endy])

ax.set(xlabel='x-axis',
       ylabel='y-axis',
       title='Some periodic functions')

ax.plot(x, f_sin, '--', x, f_poly, 'or')
plt.show()

