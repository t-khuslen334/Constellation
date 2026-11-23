import matplotlib.pyplot as plt
from stars import load_stars, load_lines
from plot import plot_constellation

stars = load_stars("data/raw/hyg_v44.csv.gz")
lines = load_lines("data/raw/index.json")
by_hip = stars.set_index("hip")

plt.style.use("dark_background")

for path in lines["UMa"]:
    coords = by_hip.loc[path, ["ra_deg", "dec"]]
    plt.plot(coords["ra_deg"], coords["dec"], color="gray", linewidth=1)

plot_constellation(stars, "UMa")
plt.savefig("orion.png", dpi=150)
plt.show()