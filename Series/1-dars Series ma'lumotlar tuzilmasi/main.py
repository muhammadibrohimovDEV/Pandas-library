# 1-dars . Series ma'lumotlar tuzilmasi


# kutubxonalarni chaqirib olish
import pandas as pd
import numpy as np

# Pandasda 2 ta muhim ma'lumotlar tuzilmasi bor
# Ular : Series va DataFrame

from pandas import Series # Series ni pandasdan import qilish

# Series bu bir o'lchamli pandasdagi ma'lumotlar tuzilmasidir
# U ikki narsadan iborat bo'ladi index va value (qiymat)
# Seriesni odiiy python list(ro'yxat)dan farqi uning index larini biz o'zimiz berishimiz yoki o'zgartirishimiz mumkin


obj = Series([1 , 2 , 3 , 4 , 5]) # Series ma'lumotlar tuzilmasini yaratish

print(obj) # Seriesdagi ham indeks , ham qiymatlarni ko'rish
print(obj.values) # Seriesdagi faqatgina qiymatlarni ko'rish
print(obj.index) # Seriesdagi faqatgina indekslarni ko'rish


# Indexlarni biz o'zimiz berishimiz , yaratishimiz , o'zgartirishimiz mumkin
obj2 = Series([5 , 6 , 3.2 , -6.5] , index = ['a' , 'b' , 'c' , 'd'])
print(obj2)

# Faqat bir dona qiymatni indexi orqali chaqirish
data = obj2['a']

# Bir nechta qiymatni index lari orqali chaqirish
data2 = obj2[["a" , "d" , "c"]]

print(data , '\n' , data2)

# Series qiymatlarini shart orqali chop etish mumkin
data3 = obj[obj.values <= 3]
print(data3)

# Series qiymatlarini ma'lum bir songa ko'paytirish va bo'lish mumkin
obj2 = obj2 * 3
print(obj2)