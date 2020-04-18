"""
simple matplotlib Examples

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
f_sin = 3 * np.sin(x)
f_2 = np.sin(2 * x) - np.cos(x)

fig, axs = plt.subplots(2, 2)

fig.suptitle('Some periodic functions')

axs[0, 0].set_title('f(x)=3$sin(x)$')
axs[0, 0].plot(x, f_sin, '--', label="3$sin(x)$")

axs[1, 0].set_title('f(x)=sin(2x)-cos(x)$')
axs[1, 0].plot(x, f_2, 'r', label="$sin(2x)-cos(x)$")


labels = ['Eng', 'IT', 'CAS', 'Sci', 'Med', 'CAP']
student_count = np.array( [[280, 170], [250, 270], [210, 290], [130, 150], [145, 165], [500, 350]] )
aggregated_student_count = student_count.sum(axis=1)
flattened_student_count = student_count.flatten()

size = 0.3
axs[0, 1].pie(aggregated_student_count, radius=1, labels= labels, wedgeprops=dict(width=size, edgecolor='white'))
axs[0, 1].set_title('University Student Distribution per College')


x = np.arange(len(labels))
width = 0.25

axs[1, 1].bar(x - width/2, student_count[:, 0], width, label='Male', color = "red")
axs[1, 1].bar(x + width/2, student_count[:, 1], width, label='Female', color = "blue")

# Add some text for labels, title and custom x-axis tick labels, etc.
axs[1, 1].set_ylabel('PPU Students')
axs[1, 1].set_title('Students per College')
axs[1, 1].set_xticks(x)
axs[1, 1].set_xticklabels(labels, rotation=45)
axs[1, 1].legend()

fig.tight_layout()
plt.show()

