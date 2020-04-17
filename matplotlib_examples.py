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

size = 0.3
ax.pie(aggregated_student_count, radius=1, labels= labels, wedgeprops=dict(width=size, edgecolor='white'))

ax.set_title('University Student Distribution per College')
plt.show()