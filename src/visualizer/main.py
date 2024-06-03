import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from common.const import H, W

fig, ax = plt.subplots()


def update(num):
    ax.clear()
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    current_x, current_y = steps[num]
    for i in range(len(current_x)):
        rect = patches.Rectangle(
            (current_x[i], current_y[i]),
            w[i],
            h[i],
            edgecolor="black",
            facecolor="blue",
        )
        ax.add_patch(rect)
    ax.set_title(f"Step {num + 1}")


ani = FuncAnimation(fig, update, frames=len(steps), repeat=False)
writer = PillowWriter(fps=1)
ani.save("bottom_left_placement.gif", writer=writer)
plt.show()
