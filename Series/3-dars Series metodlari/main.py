# Series metodlari

import pandas as pd
import numpy as np
from pandas import Series

cars_dict = {
    'malibu' : 40000,
    'lacetti' : 20000,
    'toyota' : 45000,
    'mazda' : 52000,
    'honda' : 38000,
}

models = ['honda' , 'mazda' , 'lacetti' , 'jaguar' , 'malibu' , 'toyota' , 'bmw' , 'mercedes']

cars = Series(cars_dict , index = models)

print(cars.isnull()) # Agar NaN bo'lsa True qaytaradi , aks holda False qaytaradi.

print(cars.notnull()) # Agar NaN bo'lsa False qaytaradi , aks holda True qaytaradi
cars1 = Series(cars_dict)

print(cars1 + cars) # pandas o'zi mos indeksdagi qiymatlar ustida matemetik amallarni bajaradi


# Metodlar


cars.name = "Avtosalon" # butun boshli Seriesga nom berish

print(cars.hasnans) # Butun boshli Seriesda NaN qiymatalr bormi yo'qmi bilib beradi

print(cars.dtype)# qiymatlarining ma'lumot turini ko'rsatadi

print(cars1.is_unique) # takrorlanmas qiymatlar bor bolsa True , takrorlansa Flase

print(cars.shape) # jami nechta ma'lumot borligini ko'rsatadi , hajm

print(cars.size) # ma'lumotlar hajmi

print(cars.iloc[0]) # ma'lumotlarga indekslarining tartib raqami bo'yicha murojaat qilish

print(cars.loc['bmw']) # ma'lumotlarga indekslari orqali murojaat qilish

print(cars.max()) # eng katta qiymatga murojaat qilish

print(cars.min()) # eng kichik qiymatga murojaat qilish

print(cars.mean()) # qiymatlarning o'rtacha raifmetigiga murojaat qilish

fanlar = {
    'matematika' : 'Abzalbek',
    'fizika' : 'Niyozbek' ,
    'adabiyot' : "Qodirbek" ,
    'informatika' : 'Izzatbek'
}

subjects = Series(fanlar)

print(subjects.loc['matematika']) # faqat bitta indeks

print(subjects.iloc[[1 , 0 , 2]]) # bir nechta qiymatlarga indeksalrining tartib raqami bo'yicha murojaat qilisgh


# String ma'lumotlarda .min va .max elemntlar aniqlanayotganaida ulardagi bosh hariflar (agar bir xil bo'lsa undan keyingilar)
# bo'yicha solishtiriladi . Ular ASCII jadvalidagi soniga qarab aniqlanadi. .max ga jadval tepasida joylashganlari
# . min ga esa jadval quyisida joylashganlari olinadi . Katta va kichik harf kelganida katta harf olinadi


print(subjects.max())

print(subjects.min())
