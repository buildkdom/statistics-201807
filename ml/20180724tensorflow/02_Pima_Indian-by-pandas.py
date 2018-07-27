import pandas as pd

df = pd.read_csv("pima-indians-diabetes.csv",
            names=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'])
print(df.head(5))
print(df.info())
print(df.describe())

#
print("===only take 5 first rows from input csv file===")
print(df[['preg', 'class']].head(5))