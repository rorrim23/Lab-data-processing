#%%
import pandas as pd

df = pd.read_table("Bead(2um)inDW(N1min)-C.dat", skiprows=12)

print(df)