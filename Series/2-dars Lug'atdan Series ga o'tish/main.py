# Lug'atdan Series mt ni yaratish

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

print(type(cars_dict))

cars1 = Series(cars_dict)

print('malibu' in cars1) # bir elementni Seriesda borligini tekshirish

print(cars1['toyota']) # kalit so'z boyicha chaqirish

# yangi indekslarni yaratib olish
models = ['honda' , 'mazda' , 'lacetti' , 'jaguar' , 'malibu' , 'toyota' , 'bmw' , 'mercedes']

# yangi qo'shilgan indekslar NaN qiymatiga ega bo'ladi
# mavjud lug'atni Seriesga o'girish va uni indekslarnini almashtirish
cars2 = Series(cars_dict , index = models)

print(cars_dict) # oddiy lug'at
print(cars2) # indekslari o'zgargan Series

