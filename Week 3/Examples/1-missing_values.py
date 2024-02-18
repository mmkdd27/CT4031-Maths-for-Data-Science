# Importing libraries
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv("olympics.csv")

# Take a look at the first few rows
print (df.head())

# searching for missing values
print (df['0'].isnull())
