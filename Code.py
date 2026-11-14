import math
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]

fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

x, y, angle = 0, 0, 0

for i in range(200):
    # work out where the line ends
    new_x = x + (i * 2) * math.cos(math.radians(angle))
    new_y = y + (i * 2) * math.sin(math.radians(angle))

    ax.plot([x, new_x], [y, new_y], color=colors[i % len(colors)], linewidth=2)

    x, y = new_x, new_y
    angle += 59        # turn, just like t.left(59)

ax.set_aspect("equal")
ax.axis("off")
plt.savefig("pattern.png", facecolor="black", dpi=150)
print("Saved pattern.png")