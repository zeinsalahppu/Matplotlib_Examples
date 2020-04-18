"""
simple matplotlib Examples

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
f_sin = 3 * np.sin(x)
f_2 = np.sin(2 * x) - np.cos(x)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)

fig.suptitle('Some periodic functions')

axs[0].set_title('f(x)=3$sin(x)$')
axs[0].plot(x, f_sin, '--', label="3$sin(x)$")

axs[1].set_title('f(x)=sin(2x)-cos(x)$')
axs[1].plot(x, f_2, 'r', label="$sin(2x)-cos(x)$")

plt.show()

