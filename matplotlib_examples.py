"""
simple matplotlib Examples

"""

import matplotlib.pyplot as plt

days = list(range(1, 8))
temperature = [10, 14, 16, 20, 20, 14, 17]

plt.plot(days, temperature,
         days, temperature, "or")

plt.show()
