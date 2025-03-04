# DataFrame ustunlari

import pandas as pd
import numpy as np

# Lug'atdan DataFrame yaratishda har bir qator indekslanadi (0,1,2...),
# ustunlar ketma-ketligi esa lug'atdagi ketma-ketlikka bog'liq bo'ladi.
# Ustunlar ketma-ketligini berishni istasak DataFrame yaratishda columns
# parametrini ham ko'rsatib ketishimiz mumkin:

data = {
    'Yil' : [2021 , 2020 , 2019 , 2018 , 2017 , 2016 , 2015 , 2010],
    'Aholi soni' : [33.9 , 33.5 , 32.9 , 32.5 , 31.9 , 31.4 , 30.9 , 28.5],
    'Temp' : [1.54 , 1.48 , 1.56 , 1.62 , 1.65 , 1.66 , 1.64 , 1.53]
}

df = pd.DataFrame(data, columns = ['Temp' , 'Aholi soni' , 'Yil' , 'YAIM'])

# Index lar ketma-ketligini ham o'zimiz berishimiz mumkin :

df = pd.DataFrame(data , columns = ['Yil' , 'Temp' , 'Aholi soni' , 'YAIM'] , index = [21 , 20 , 19 , 18 , 17 , 16 , 15 , 10])

print(df)

# DataFrame har bir ustuni va uning qiymatlari bu bitta Series dir :
df_series = df['Yil']
print(df_series)
print(type(df_series)) # ma'lummot turini ko'rish

# Faqatgina bir dona ustunni ishlatmoqchi bo'lsak ,
# agar uning nomi , pythondagi o'zgaruvchilar nomi qoidasiga mos tushsa quyidagicha chaqirishimiz mumkin :
print(df.Temp)
print(df.Yil)

# Agar probel yoki boshqa turdagi nom bo'lsa lug'atni chqairgandek chaqiramiz :
print(df['Aholi soni'])

# Bunday chaqirishning yana qulay tarafi o'zgartirish kiritishga oson :

# Butun ustunga o'zgartirsh kiritish :
df['YAIM'] = 1600
print(df['YAIM'])
print(df)

# Buni yana bir usuli = starlar soniga teng ro'ycat qo'shish
df['YAIM'] = [1700 , 1605 , 1650 , 1250 , 1320 , 1970 , 4560 , 2301]
print(df['YAIM'])
print(df)

# Ma'lum index dagi elementlarga o'zgartirish kiritish :
df['YAIM'] = pd.Series([1600 , 2503 , 8645 , 9346 , 5210] , index=[20 , 19 , 18 , 10 , 21])
print(df['YAIM'])
print(df)

# Yangi ustun va qiymatlar berish
df['1500+'] = df['YAIM'] >= 1500
print(df['1500+'])
print(df)

# Faqatgina qiymatlardan foydalanish uchun ularni matritsa ko'rinishiga o'tkazish
# dtype = object turishi kerak aks holda o'zgarib ketadi
df_arr = np.array(df , dtype = object)
print(df_arr)
print(type(df_arr))

