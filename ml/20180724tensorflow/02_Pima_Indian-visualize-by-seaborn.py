import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.figure(figsize=(12,12))

df = pd.read_csv("pima-indians-diabetes.csv",
            names=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'])

# take a sip of the file
print("===only take 5 first rows from input csv file===")
print(df[['preg', 'class']].head(5))

# visualize
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white', annot=True)
plt.show()