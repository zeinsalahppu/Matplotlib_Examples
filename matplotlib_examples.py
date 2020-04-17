"""
simple matplotlib Examples
"""

import matplotlib.pyplot as plt
import numpy as np

labels = ['Eng', 'IT', 'CAS', 'Sci', 'Med', 'CAP']
student_count = np.array( [[280, 170], [250, 270], [210, 290], [130, 150], [145, 165], [500, 350]] )
aggregated_student_count = student_count.sum(axis=1)
flattened_student_count = student_count.flatten()

fig, ax = plt.subplots()

# use a color map to define colors
oc_idx = np.arange(len(aggregated_student_count))*4
ic_idx = (oc_idx[: , np.newaxis] + np.array([1, 2])).flatten()
print(oc_idx)
print(ic_idx)

cmap = plt.get_cmap("tab20c")
outer_colors = cmap(oc_idx)
inner_colors = cmap(ic_idx)

size = 0.3
ax.pie(aggregated_student_count, radius=1, colors=outer_colors, labels= labels, wedgeprops=dict(width=size, edgecolor='white'))

ax.pie(flattened_student_count, radius=1-size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='white'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()
