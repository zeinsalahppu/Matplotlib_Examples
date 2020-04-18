import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure()

gs0 = gridspec.GridSpec(1, 2, figure=fig)
gs00 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=gs0[0])
gs01 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[1])

ax1 = fig.add_subplot(gs00[0, 0])
ax1.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24)

ax2 = fig.add_subplot(gs00[1, 0])
ax2.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24)

ax3 = fig.add_subplot(gs00[2, 0])
ax3.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24)

ax4 = fig.add_subplot(gs01[0])
ax4.text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24)

plt.show()