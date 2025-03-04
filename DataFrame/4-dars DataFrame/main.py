# DataFrame ma'lumotlar tuzilmasi

import pandas as pd
import numpy as np


# DataFrame bu pandas ning ichidagi ma'lumtlar tuzilamsining bir turi bo'lib , u 2 o'lchamli bo'ladi .
# DataFrame satr va ustunlardan iborat bo'ladi . Unda asosan index va column bo'ladi .
# Index va column larni biz o'zimiz berishimiz mumkin

# Nested dictionary (icham-ich lug'at)

data = {
    'Yil' : [2021 , 2020 , 2019 , 2018 , 2017 , 2016 , 2015 , 2010],
    'Aholi soni' : [33.9 , 33.5 , 32.9 , 32.5 , 31.9 , 31.4 , 30.9 , 28.5],
    'Temp' : [1.54 , 1.48 , 1.56 , 1.62 , 1.65 , 1.66 , 1.64 , 1.53]
}

# Lug'atdan DataFrame hosil qilish

df = pd.DataFrame(data)
print(df) # Agar ushbu ko'rinishda chop qiladigan bo'lsak barcha ma'lumot chop etiladi (bu esa juda ko'p)

df_head = df.head() # DataFrame ichidagi dastlabki 5 ta ma'lumotni ko'rish uchun .head() ishlatilinadi
print(df_head)

df_shape = df.shape # DataFrame o'lchamini ko'rish uchun .shape metodi ishlatilinadi
print(df_shape)


