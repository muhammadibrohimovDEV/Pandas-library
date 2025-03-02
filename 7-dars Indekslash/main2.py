import pandas as pd

data = {
    'Kod': ['A001', 'A002', 'B001', 'B002', 'C001'],
    'Mahsulot': ['Olma', 'Banan', 'Gilos', 'Nok', 'Anor'],
    'Narx': [15000, 12000, 18000, 20000, 25000]
}

df = pd.DataFrame(data , index = data['Kod'])

print(df.loc[['B001' , 'C001']])
