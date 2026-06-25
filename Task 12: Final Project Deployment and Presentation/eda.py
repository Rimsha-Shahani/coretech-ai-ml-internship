
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

sns.histplot(df['Price'])
plt.show()

sns.scatterplot(x='Area', y='Price', data=df)
plt.show()

sns.boxplot(y=df['Price'])
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.show()

sns.pairplot(df)
plt.show()
