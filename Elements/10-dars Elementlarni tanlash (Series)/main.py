# Elementlarni tanlash (Series)

import pandas as pd
import numpy as np

# DataFramening har bir ustuni bu alohida Series ma'lumot tuzilmasi hisoblanadi

data1 = {
    'Yil' : [2021 , 2020 , 2019 , 2018 , 2017 , 2016 , 2015 , 2010],
    'Aholi soni' : [33.9 , 33.5 , 32.9 , 32.5 , 31.9 , 31.4 , 30.9 , 28.5],
    'Temp' : [1.54 , 1.48 , 1.56 , 1.62 , 1.65 , 1.66 , 1.64 , 1.53],
    'Zichlik' : [79.77 , 78.68 , 77.53 , 76.34 , 75.13 , 73.91 , 72.71 , 67.03]
}

df = pd.DataFrame(data1 , index = [21 , 20 , 19 , 18 , 17 , 16 , 15 , 10])
print(df)

data = df['Aholi soni'] # DataFrame ning bir ustunini ajratib olish , natijada Series shaklidagi ma'lumot qayatadi
print(data , type(data))

data2 = df[['Aholi soni']] # DataFrame dan ixtiyoriy ustunni DataFrame ko'rinishida olish (ichma-ich kvadrat qavs)
print(data2 , type(data2))

print(data[21] , type(data[21])) # Seriesni ichidagi bitta qiymatni numpy.float ko'rinishida qaytishi

print(data[[21]] , type(data[[21]])) # Seriesni bitta qiymatini pandas.Series ko'rinishida olish

print(data[0:4]) # bir dona qavs orqali bir nechta elementlarni chiqarish
print(data[[21 , 20 , 19 , 18]]) # ikkita qavs orqali index lar yordamida bir nechta elementlarni chaqirish

obj = pd.Series(np.arange(8.0) , index = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
print(obj[['a']])
print(obj['a' : 'e']) # harf orqali ko'p oby'ektlarga olish

obj['a' : 'c'] = 15 # oraliqga qiymat ber
print(obj)

print(obj[obj<15]) # filtrla

