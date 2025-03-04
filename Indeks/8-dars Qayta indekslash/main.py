# Qayta indekslash

import pandas as pd

data = {
    'Yil' : [2021 , 2020 , 2019 , 2018 , 2017 , 2016 , 2015 , 2010],
    'Aholi soni' : [33.9 , 33.5 , 32.9 , 32.5 , 31.9 , 31.4 , 30.9 , 28.5],
    'Temp' : [1.54 , 1.48 , 1.56 , 1.62 , 1.65 , 1.66 , 1.64 , 1.53],
    'Zichlik' : [79.77 , 78.68 , 77.53 , 76.34 , 75.13 , 73.91 , 72.71 , 67.03]
}

df = pd.DataFrame(data)

print(df)

df.index = [21 , 20 , 19 , 18 , 17 , 16 , 15 , 10]

print(df)

# Reindex metodi

indeks = [21 , 20 , 19 , 18 , 17 , 16 , 15 , 10]
indeks.sort()

print(df.reindex(indeks)) # reindex metodi bu yangi DataFrame qaytaradi

print(df.reindex(indeks)) # Agar o'zgarishni saqlamoqchi bo'lsak inplace = True qilishimiz kerak

print(df)

print(df.reindex([10 , 15 , 20]))

print(df.reindex(pd.Index(range(10 , 22)))) # reindex metodida biz hohlaganimizcha index bera olamiz faqat ularning qiymatlari NaN bo'ladi

print(df.reindex(pd.Index(range(10 , 22)) , method = 'nearest')) # NaN o'rniga methdolarda foydalansa bo'ladi . 'nearest' eng yaqin qiymatlar bilan to'ldiradi

print(df.reindex(pd.Index(range(10 , 22)) , method = 'ffill')) # forward fill - oxirgi qiymatni oladi va yozib tashlaydi

# Ustunlarni tashlab yuborish

print(df.reindex(columns = ['Aholi soni' , 'Temp' , "Zichlik"])) # ustunni tashlash uchun uni yozmaslik kerak

print(df.sample(3)) # ixtiyoriy qiymatlarni chiqaradi

print(df.loc[[10 , 15 , 20] , ["Aholi soni" , 'Temp']]) # index va ustunlarni ixtiyoriy kesish