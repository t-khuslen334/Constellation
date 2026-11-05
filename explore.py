import pandas as pd
df = pd.read_csv("data/raw/hyg_v44.csv.gz")
# print(df.shape)
# print(df.columns.tolist())
# print(df.head().T)
# print(df["mag"].value_counts().head(10)) # 
# df["ra_deg"] = df["ra"] * 15
# print(df.loc[0,['proper', 'ra', 'dec', 'mag']])
result = df.loc[df["proper"] == "Sirius", 'mag']
print(df.shape)
df = df[df["id"] != 0]
print(df.shape)
print(result)