import pandas as pd 

df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())

print("Replace Null Values withe the number 130 : ")
df.fillna(130, inplace=True)
print(df)