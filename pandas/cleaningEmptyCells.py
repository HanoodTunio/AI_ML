import pandas as pd


df = pd.read_csv('data.csv')

x = df["Salary"].mean()
df["Salary"].fillna(x, inplace =True)
df.drop_duplicates(inplace = True)

print(df)
