"""
simple matplotlib Examples

"""


import numpy as np
import matplotlib.pyplot as plt

x = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
y = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]

fig, ax = plt.subplots()

ax.set(xlabel='Temperature',
       ylabel='Ice Cream Sales',
       title='Temperature/Ice Cream Correlation')

ax.scatter(x, y)
plt.show()

