# Importing libraries
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv("olympics.csv")

to_drop = ['0', '1']

df.drop(to_drop, inplace=True, axis=1)

print(df.head())
