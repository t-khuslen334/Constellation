import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/hyg_v44.csv.gz")
print("Raw shape:", df.shape)

# Inspect raw data
# Full-catalog magnitude distribution (before any filtering)
plt.hist(df["mag"], bins=50)
plt.xlabel("Apparent magnitude")
plt.ylabel("Number of stars")
plt.title("magnitude distribution")
plt.show()

print("Sirius mag:", df.loc[df["proper"] == "Sirius", "mag"].item())

# Remove the Sun 
df = df[df["id"] != 0]

# convert to degrees (1 h = 15°)
df["ra_deg"] = df["ra"] * 15

# Keep naked-eye stars only (mag <= 6)
df = df[df["mag"] <= 6]

print("Clean shape:", df.shape)