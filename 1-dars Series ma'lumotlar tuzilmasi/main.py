# 1-dars . Series ma'lumotlar tuzilmasi


# kutubxonalarni chaqirib olish
import pandas as pd
import numpy as np

# Pandasda 2 ta muhim ma'lumotlar tuzilmasi bor
# Ular : Series va DataFrame

from pandas import Series # Series ni pandasdan import qilish


# Seriesni ro'yxatdan farqi bu indexni hohlagan holimizda berishimiz mumkin
obj = Series([1 , 2 , 3 , 4 , 5]) # Series ma'lumotlar tuzilmasini yaratish

print(obj) # Seriesdagi ham indeks , ham qiymatlarni ko'rish
print(obj.values) # Seriesdagi faqatgina qiymatlarni ko'rish
print(obj.index) # Seriesdagi faqatgina indekslarni ko'rish


obj2 = Series([5 , 6 , 3.2 , -6.5] , index = ['a' , 'b' , 'c' , 'd']) # indekslarni o'zimiz bera olamiz
print(obj2)
print(obj2.values)
print(obj2.index)
print(obj2["a"]) # bir dona elemntni indeksi bilan chaqirish
print(obj2[["a" , 'c' , 'd' , 'd']]) # bir nechta elementni quyidagi kabi chaqiriladi

print(obj2[obj2 < 3]) # 2 dan katta qiymatdagi elemntlarni chiqarish

print(obj2*2) # onj2 har bir elementni 2 ga ko'paytirish

print(np.exp(obj2))
