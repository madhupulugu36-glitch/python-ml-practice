import pandas as pd

data = {
    "Age": [22, 25, 30, 35, 40],
    "Salary": [25000, 50000, 75000, 100000, 150000]
}

df = pd.DataFrame(data)
print(df)

from sklearn.preprocessing import StandardScaler
SS = StandardScaler()
df_scaled = SS.fit_transform(df)
df_standardized = pd.DataFrame(df_scaled, columns = df.columns)
print(df_standardized)


from sklearn.preprocessing import MinMaxScaler
MM = MinMaxScaler()
df_scaled_mm = MM.fit_transform(df)
df_minmax = pd.DataFrame(df_scaled_mm, columns = df.columns)
print(df_minmax)