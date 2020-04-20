"""
simple matplotlib Examples

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
f_sin = 3 * np.sin(x)
f_2 = np.sin(2 * x) - np.cos(x)

fig, ax = plt.subplots()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

ax.set_xticks([-2.0 * np.pi, -1.5 * np.pi, -1.0 * np.pi, -0.5 * np.pi,
                0.5 * np.pi, 1.0 * np.pi, 1.5 * np.pi, 2.0 * np.pi])
ax.set_xticklabels([r'$-2\pi$', '', r'$-\pi$', '', '', r'$\pi$', '', r'$2\pi$'])

ax.set_yticks([-3, -1, +1, 3])

ax.set_title('Some periodic functions')

ax.plot(x, f_sin, '--', label="3$sin(x)$")
ax.plot(x, f_2, 'r', label="$sin(2x)-cos(x)$")
# ax.legend(loc='best')

pnt = 2.3, 3*np.sin(2.3)
ax.annotate("3$sin(x)$", xy= pnt,
            xytext=(4.5, 3),
            color="blue",
            arrowprops=dict(arrowstyle="->", color="blue",
                       connectionstyle="angle3,angleA=0,angleB=-90"))

pnt = 4.2, np.sin(2* 4.2) - np.cos(4.2)
ax.annotate("$sin(2x)-cos(x)$", xy= pnt,
            xytext=(5.5, 2),
            color="red",
            arrowprops=dict(arrowstyle="->", color="red",
                       connectionstyle="angle3,angleA=0,angleB=-90"))

plt.show()
