import pandas as pd
import matplotlib.pyplot as plt
from stars import load_stars

stars = load_stars("data/raw/hyg_v44.csv.gz")
# print(stars.shape)    

is_orion = stars["con"] == "Ori"    # Select whether true or not if con == Ori
orion = stars[is_orion]     #Create a new column with only True value in it

proper_named_orion = orion[orion["proper"].notna()].sort_values("mag") # Create a column with only proper names in orion and sort
print(proper_named_orion)
