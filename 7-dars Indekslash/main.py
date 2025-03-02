# Indekslar bilan ishlash

import pandas as pd

usernames = {"anvar":"anvarbek223", "olim":"olimtoy", "maryam":"mary334455","javohir":"javohir445"}
emails = {"anvar":"anvar@gmail.com", "olim":"olim@mail.ru", "maryam":"mary33@gmail.com","javohir":"javohir445@gmail.com"}

data = {
    'username':usernames,
    'email':emails
}
df1 = pd.DataFrame(data)

data2 = {
    'username':{"olim":"olimjon21", "maryam":"maryam2020"},
    'email':{"olim":"olimjon21@mail.ru", "maryam":"maryam20@gmail.com"}
}
df2 = pd.DataFrame(data2)

df3 = pd.concat([df1 , df2]) # pd.concat(df1 , df2) df1 va df2 larni birlashtiradi
indexes = df3.index

newindex = pd.Index(['olim' , 'nafisa' , 'hamida'])
print(df3.index.isin(newindex)) # var1.isin(var2) var1 ichida var2 elementlari bormi tekshiradi

print(df3.index.difference(newindex)) # var1.index.difference(var2) var1 ning var2 dagi indexlar farqini ko'rsatadi

newind1 = pd.Index([2016 , 2018 , 2020 , 2019])
newindex = newindex.union(newind1) # var1.index.union(var2.index) ikki df ni indexlarini birlashtirish
print(newindex)

print(df3.index.delete(1)) # var.index.delete(n) n-indeksdagi indexni o'chirib tashlaydi

print(df3.index.drop('anvar')) # var,index.drop(name_index) index nomini kiritlsa o'sha index o'xhirib tashlanadi

print(df3.index.insert(4 , 'masha')) # var.index.insert(location , name) dfning maxsus joyiga index qo'shadi

print(df3.index.is_unique) # df butunlay indexlari ichida takrorlanish bo'lmasa True , aks holda False
print(newindex.is_unique)

print(df3.index.unique()) # faqatgina takrorlanmas indekslarni qayatardi
df3.index['anvar'] = 'makka' # indexlarni o'zgartirib bo'lmaydi

