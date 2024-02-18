# Importing libraries
import pandas as pd
# Read csv file into a pandas dataframe
df = pd.read_csv("olympics.csv", header=1, skiprows=[1,2,4])
print (df.head())
