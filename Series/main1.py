import pandas as pd

data = [5, 10, 15, 20, 25]

s1 = pd.Series(data)

print(s1) # indeklar avtomatik [0 , 1 , 2 , 3 , 4] bo'ladi

s2 = pd.Series(data , index = ['A' , 'B' , 'C' , 'D' , 'E']) # indexlarni qo'lda berish

print(s2[s2>20]) # 20 dan katta elementlarni chiqarish

print(s2[s2<15]) # 15 dan kichik ma'lumotlarni chiqarish

s3 = s1*2 # barcha ma'lumotlarni 2 ga ko'paytirish

print(s3)

print(s2["B"]) # "B" indeksidagi elementni chiqarish

print(s3.max()) # eng katta elementni chiqarish
print(s3.min()) # eng kichik elemntni chiqarish