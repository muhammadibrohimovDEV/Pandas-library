import pandas as pd

data = {'Apple': 15000, 'Banana': 12000, 'Cherry': 18000, 'Date': 20000}

fruits = pd.Series(data)
print(fruits['Cherry'])