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
ax.bar(x - width/2, male_count, width, label='Male', color = "red")
ax.bar(x + width/2, female_count, width, label='Female', color = "blue")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('PPU Students')
ax.set_title('Students per College')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation='vertical')
ax.legend()

fig.tight_layout()

plt.show()