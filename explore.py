import matplotlib.pyplot as plt
from stars import load_stars
from plot import plot_constellation
import json

stars = load_stars("data/raw/hyg_v44.csv.gz")

#plt.style.use("dark_background")
#plot_constellation(stars, "Ori")
#plt.savefig("uma.png", dpi=150)
#plt.show()

with open("data/raw/index.json", encoding="utf-8") as f:
    data = json.load(f)


cons = data["constellations"]

for c in cons:
    if c["id"] == "CON modern Ori":
        orion_lines = c["lines"]

by_hip = stars.set_index("hip")
belt = by_hip.loc[orion_lines[0], ["ra_deg", "dec"]]
print(belt)
plt.style.use("dark_background")



for path in orion_lines:
    coords = by_hip.loc[path, ["ra_deg", "dec"]]
    plt.plot(coords["ra_deg"], coords["dec"], color="gray", linewidth=1)

plot_constellation(stars, "Ori")
plt.savefig("orion.png", dpi=150)
plt.show()
