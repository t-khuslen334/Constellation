import matplotlib.pyplot as plt
from stars import load_stars, load_lines
from plot import plot_constellation

stars = load_stars("data/raw/hyg_v44.csv.gz")
lines = load_lines("data/raw/index.json")

plt.style.use("dark_background")

plot_constellation(stars, lines, "And")
plt.show()