# Importing libraries
import pandas as pd
import numpy as np

# Making a list of missing value types
missing_values = ["n/a", "na", "--", "??"]
df = pd.read_csv("olympics.csv", na_values = missing_values)

# searching for missing values
print (df['0'].isnull())
