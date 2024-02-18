import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris.csv')

# Usual boxplot
ax = sns.boxplot(x='species', y='sepal_length', data=df)

# Add jitter with the swarmplot function.
ax = sns.swarmplot(x='species', y='sepal_length', data=df, color="grey")

plt.show()
