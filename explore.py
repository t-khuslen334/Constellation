import pandas as pd
import matplotlib.pyplot as plt
from stars import load_stars

stars = load_stars("data/raw/hyg_v44.csv.gz")
print(stars.shape)    # expect (5070, 7)

