"""
simple matplotlib Examples
"""

import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

labels = ['Eng', 'IT', 'CAS', 'Sci', 'Med', 'CAP']
student_count = np.array( [[280, 170], [250, 270], [210, 290], [130, 150], [145, 165], [500, 350]] )
aggregated_student_count = student_count.sum(axis=1)
flattened_student_count = student_count.flatten()

fig, ax = plt.subplots()

# combined the color maps "tab20c" and "tab20b"
combined_colors = np.vstack((plt.get_cmap("tab20c").colors, plt.get_cmap("tab20b").colors))
cmap= matplotlib.colors.ListedColormap(combined_colors)

# use the combined color map to define colors
oc_idx = np.arange(len(aggregated_student_count))*4
ic_idx = (oc_idx[: , np.newaxis] + np.array([1, 3])).flatten()
outer_colors = cmap(oc_idx)
inner_colors = cmap(ic_idx)

size = 0.3
ax.pie(aggregated_student_count, radius=1, colors=outer_colors, labels= labels, wedgeprops=dict(width=size, edgecolor='white'))
ax.pie(flattened_student_count, radius=1-size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='white'))

ax.set_title('University Students Distribution per College')

plt.show()
