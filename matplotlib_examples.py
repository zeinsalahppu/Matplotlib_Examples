"""
simple matplotlib Examples

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
f_sin = 3 * np.sin(x)
f_2 = np.sin(2 * x) - np.cos(x)

fig = plt.figure(1)
fig.suptitle('Some plots')

ax1 = plt.subplot(2, 2, 1)
ax1.set_title('f(x)=3$sin(x)$')
ax1.plot(x, f_sin, '--', label="3$sin(x)$")

ax2 = plt.subplot(2, 2, 2)
ax2.set_title('f(x)=sin(2x)-cos(x)$')
ax2.plot(x, f_2, 'r', label="$sin(2x)-cos(x)$")


labels = ['Eng', 'IT', 'CAS', 'Sci', 'Med', 'CAP']
student_count = np.array( [[280, 170], [250, 270], [210, 290], [130, 150], [145, 165], [500, 350]] )
aggregated_student_count = student_count.sum(axis=1)
flattened_student_count = student_count.flatten()

ax3 = plt.subplot(2, 2, 3)
size = 0.3
ax3.pie(aggregated_student_count, radius=1, labels= labels, wedgeprops=dict(width=size, edgecolor='white'))
ax3.set_title('University Student Distribution per College')

ax4 = plt.subplot(2, 2, 4)
x = np.arange(len(labels))
width = 0.25
ax4.bar(x - width/2, student_count[:, 0], width, label='Male', color = "red")
ax4.bar(x + width/2, student_count[:, 1], width, label='Female', color = "blue")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax4.set_ylabel('PPU Students')
ax4.set_title('Students per College')
ax4.set_xticks(x)
ax4.set_xticklabels(labels, rotation=45)
ax4.legend()

fig.tight_layout()
plt.show()

