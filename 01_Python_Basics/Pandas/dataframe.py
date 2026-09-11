# Creating a Pandas DataFrame

# 1. Creating an Empty DataFrame
import pandas as pd
df = pd.DataFrame()
print(df)

# 2. Creating a DataFrame from a List
lst = ['Python', 'Java', 'SQL', 'Machine Learning', 'C++', 'Data-Science']
df = pd.DataFrame(lst)
print(df)

# 3. Creating DataFrame from dict of Numpy Array
import numpy as np
data = { 'A': np.array([1, 4, 7]),
          'B': np.array([2, 5, 8]),
          'C': np.array([3, 6, 9]) }
df = pd.DataFrame(data)
print(df)

# 4. Creating a DataFrame from a List of Dictionaries
data1 = [
    {'name': 'Mike', 'degree': 'MBA', 'score': 90},
    {'name': 'Dan', 'degree': 'BCA', 'score': 40},
    {'name': 'Emilia', 'degree': 'M. tech', 'score': 80},
]

df = pd.DataFrame(data1)
print(df)