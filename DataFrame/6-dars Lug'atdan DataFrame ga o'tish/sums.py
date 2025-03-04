import pandas as pd

data = {
    'Mahsulot': ['Olma', 'Banan', 'Gilos', 'Xurmo'],
    'Narx': [15000, 12000, 18000, 20000],
    'Miqdor': [10, 15, 7, 20]
}

df = pd.DataFrame(data)

df['Jami'] = pd.Series(df['Narx']*df['Miqdor'])
print(df)

# .describe() -  faqat sonli ustunlarning statistik ma'lumotlarini chiqaradi .
# .info() -  DataFrame tarkibi haqida umumiy ma'lumot beradi
print(df.describe() , '\n' , df.info() , '\n' , df.head(2) , '\n' , df.tail(2))