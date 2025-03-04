# Qator va ustunlarni tashlash

import pandas as pd

import pandas as pd

data = {
    'Yil' : [2021 , 2020 , 2019 , 2018 , 2017 , 2016 , 2015 , 2010],
    'Aholi soni' : [33.9 , 33.5 , 32.9 , 32.5 , 31.9 , 31.4 , 30.9 , 28.5],
    'Temp' : [1.54 , 1.48 , 1.56 , 1.62 , 1.65 , 1.66 , 1.64 , 1.53],
    'Zichlik' : [79.77 , 78.68 , 77.53 , 76.34 , 75.13 , 73.91 , 72.71 , 67.03]
}

df = pd.DataFrame(data)

df.index = [21 , 20 , 19 , 18 , 17 , 16 , 15 , 10]
df = df.sort_index()
print(df)

# Qator (index , axis = 0 , 'rows') larni tashlab yuborish

df2 = df.drop(10) # bir dona qatorni tashlab yuborish
print(df2)

df3 = df.drop([10 , 19 , 20 , 18]) # bir nechta qatorlarni tshlab yuborish
print(df3)

# Ustunlarni (columns , axis = 1 , 'columns') tashlab yuborish
df4 = df.drop('Yil' , axis = 1) # bir dona ustunni tashlab yuborish
print(df4)

df5 = df.drop(['Temp' , 'Yil'] , axis = 'columns') # bir nechta ustunlarni tashlab yuborish
print(df5)

# O'zgarishlarni asosiy df ga saqlash
df.drop("Yil" , axis = 1 , inplace = True) # shu yerda ehtiyot bo'lish kerak chunki asosi dfga ta'sir qiladi
print(df)

