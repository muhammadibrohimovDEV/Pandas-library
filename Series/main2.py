import pandas as pd

data = [5, 10, 15, 20, 25]

indexes = ['a' , 'b' ,  'c' , 'd' , 'e']

s = pd.Series(data , index = indexes)

s.index = list(map (lambda x : x.upper() , indexes)) # index lar katta harflar bilan almashadi

print(s)
print(s.sum()) # barcha qiymatlar yig'indisi
print(s.mean()) # o'rtacha qiymat
print(s.median()) # qiymatlar mediani