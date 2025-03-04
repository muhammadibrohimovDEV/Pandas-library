# Lug'atdan DataFrame ga o'tish

import pandas as pd
import numpy as np

data = {
    'Uzbekistan' : {2021:33.9 , 2020:33.5 , 2019:32.9 , 2018:32.5 , 2017:31.9},
    'Kazakhstan' : {2021:18.9 , 2020:18.7 , 2019:18.5 , 2018:18.3 , 2017:18.1 , 2016:17.8}
}

df = pd.DataFrame(data)

# DataFrame ga nom berish
df.name = 'Country Data'

# DataFrame butun indexlariga bitta nom berish
df.index.name = 'Years'

print(df.name , df)

# Faqat ma'lum bir ma'lumotlarnigina ajratib DataFrame ga o'tkazish
df2 = pd.DataFrame(data , index=[2021 , 2020 , 2019])
print(df2)

# Index va Ustunlarning o'rinlarini almashtirish
df3 = df.T
print(df3)

# Faqatgina qiymatlarni alohida ajratib olish
arr = df.values (df.T.values)
print(arr , '\n' , type(arr))



