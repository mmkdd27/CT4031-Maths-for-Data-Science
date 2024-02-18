import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris.csv')

sns.boxplot( y=df["sepal_length"] )

plt.show()
