"""
simple matplotlib Examples

"""

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 100)
f_sin = 3 * np.sin(theta)
f_2 = np.sin(2 * theta) - np.cos(theta)

ax = plt.subplot(projection='polar')

ax.set_title('Some functions in Polar Projection')

ax.plot(theta, f_sin, '--', label="3$sin(x)$")
ax.plot(theta, f_2, 'r', label="$sin(2x)-cos(x)$")
ax.legend(loc='best')

plt.show()
