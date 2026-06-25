
import pandas as pd

df = pd.read_csv("dataset.csv")

df.drop_duplicates(inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

print(df.head())
