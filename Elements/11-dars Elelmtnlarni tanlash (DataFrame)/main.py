# Elementlarni tanlash (DataFrame)

import pandas as pd
import numpy as np

uz = {2020:33.5 , 2019:32.9 , 2018:32.5 , 2017:31.9 , 2016:31.4 , 2015:30.9}
kz = {2020:18.8 , 2019:18.5 , 2018:18.3 , 2017:18.1 , 2016:17.8 , 2015:17.6}
tj = {2020:9.5 , 2019:9.3 , 2018:9.1 , 2017:8.9 , 2016:8.7 , 2015:8.5}
kg = {2020:6.5 , 2019:6.4 , 2018:6.3 , 2017:6.2 , 2016:6.1 , 2015:6.0}
tr = {2020:6.0 , 2019:5.9 , 2018:5.8 , 2017:5.8 , 2016:5.6 , 2015:5.6}

data = {
    'Uzbekistan' : uz,
    'Kazakhstan' : kz,
    'Tajikistan' : tj,
    'Kyrgizstan' : kg,
    'Turkmenistan' : tr
}

df = pd.DataFrame(data)
print(df)