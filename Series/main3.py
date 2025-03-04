import pandas as pd

data = [5, 10, 15, 20, 25]

indexes = ['A' , 'B' , 'C' , 'D' , 'E']

s1 = pd.Series(data , index = indexes)

print(s1)

s2 = s1 + 5 # har bir elementga 5 qo'shib yangi Series yaratish

s2["C"] = 100 # "C" indeksidagi elementni 100 ga tenglash

print(list(filter(lambda x : x % 2 == 0 , s2))) # juft sonlarni chop qilish