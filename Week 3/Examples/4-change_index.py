# Importing libraries
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv("olympics.csv")

print(df['0'].is_unique)

#changing the index
df = df.set_index('0')

print(df.head())
