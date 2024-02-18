import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.csv')

plt.scatter(iris['sepal_length'], iris['sepal_width'], alpha=0.2,
            s=100*iris['petal_width'], c=iris['species_number'], cmap='viridis')

plt.xlabel('sepal_length')
plt.ylabel('sepal_width');

plt.show()
