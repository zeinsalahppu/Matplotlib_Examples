"""
simple matplotlib Examples
"""

import matplotlib.pyplot as plt
import numpy as np

labels = ['Eng', 'IT', 'CAS', 'Sci', 'Med', 'CAP']
male_count = [280, 250, 210, 130, 145, 500]
female_count = [170, 270, 290, 150, 165, 350]

x = np.arange(len(labels))
width = 0.25

fig, ax = plt.subplots()

ax.bar(x, male_count, width, label='Male', color = "red")
ax.bar(x, female_count, width, bottom=male_count, label='Female', color = "blue")

ax.set_ylabel('PPU Students')
ax.set_title('Students per College')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation='vertical')
ax.legend()

fig.tight_layout()

plt.show()