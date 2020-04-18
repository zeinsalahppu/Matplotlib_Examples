import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure()

gs = gridspec.GridSpec(3, 3, figure=fig)

ax1 = plt.subplot(gs[0, :])
ax1.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24)

ax2 = fig.add_subplot(gs[1, :2])
ax2.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24)

ax3 = fig.add_subplot(gs[2, 0])
ax3.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24)

ax4 = fig.add_subplot(gs[2, 1])
ax4.text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24)

ax5 = fig.add_subplot(gs[1:, 2])
ax5.text(0.5, 0.5, 'Axes 5', ha='center', va='center', size=24)

plt.show()