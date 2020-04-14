"""
simple matplotlib Examples

"""

import matplotlib.pyplot as plt

days = list(range(1, 8))
temperature = [10, 14, 16, 20, 20, 14, 17]

fig, ax = plt.subplots() # one axis

# plt.xlabel('Days)')
# plt.ylabel('Temperature')
# plt.title('Temperature of the Week')

ax.set(xlabel='Days', ylabel='Temperature',
       title='Temperature of the Week')


ax.plot(days, temperature,
         days, temperature, "or")

plt.show()
