"""import pandas as pd
import numpy as np

data = np.array(['m', 'a', 'd', 'h', 'u'])
s = pd.Series(data)
print("Pandas Series:")
print(s)

import pandas as pd
import numpy as np

data = ['Madhu', 'Rahul', 'Priya']
s = pd.Series(data, index = ['A', 'B', 'C'])
print(s)

import pandas as pd
df = pd.DataFrame()
lst = ['Python', 'Java', 'SQL', 'C++']

df = pd.DataFrame(lst, index=['A', 'B', 'C', 'D'])

print(df)"""
import pandas as pd

# 1. Loading Data:
df = pd.read_csv("data.csv")
print(df.head)

# 2. Viewing and Exploring Data:
df.info()

# 3. Handling missing Data:
print(df.isnull().sum())
df = df.fillna(0)

# 4. Selecting and Filtering Data:
ages = df[df['age'] > 25]
print(ages)

# 5. Adding and Removing Columns:
df['total'] = df['a'] + df['b']
print(df.head)

# 6. Grouping Data(GroupBy):
res = df.groupby('category') ['sales'].sum()
print(res)