# Importing libraries
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv("olympics.csv")

# Extracting the code
extr = df['0'].str.extract(r'^(\d{1})', expand=False)
print(extr.head())

# Converting to numeric
df['0'] = pd.to_numeric(extr)
print(df.head())
