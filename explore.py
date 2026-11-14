import matplotlib.pyplot as plt
from stars import load_stars

stars = load_stars("data/raw/hyg_v44.csv.gz")

orion = stars[stars["con"] == "Ori"]
named_orion = orion[orion["proper"].notna()].sort_values("mag")

plt.style.use("dark_background")

# Brighter stars (smaller mag) get bigger dots
plt.scatter(orion["ra_deg"], orion["dec"], s=(6 - orion["mag"]) * 7, c="white")

for name, x, y in zip(named_orion["proper"], named_orion["ra_deg"], named_orion["dec"]):
    plt.text(x, y + 0.5, name, fontsize=8)

plt.gca().invert_xaxis()  # sky maps show east (increasing RA) on the left
plt.xlabel("Right ascension (deg)")
plt.ylabel("Declination (deg)")
plt.title("Orion: naked-eye stars (mag ≤ 6)")
plt.show()