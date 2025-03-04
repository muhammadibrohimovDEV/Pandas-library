import pandas as pd

data = {
    'Ism' : ['Ali' , 'Vali' , 'Hasan' , 'Husan'],
    'Yosh' : [25 , 30 , 22 , 28],
    'Kasb' : ['Dasturchi' , 'Muhandis' , 'Talaba' , "O'qituvchi"],
    'Shahar' : ['Toshkent' , 'Samarqand' , "Buxoro" , 'Andijon']
}

df = pd.DataFrame(data , index = ['A' , 'B' , 'C' , 'D'])
print()
print(df)

df['Maosh'] = [15_000_000 , 12_000_000 , 18_000_000 , 8_000_000]

print()
print(df)

df.Yosh *= 2

df.loc[df['Shahar'] == "Samarqand" , ['Shahar']] = 'Namangan'

print('\n' , df["Maosh"].min() , '\n' , df.Maosh.max() , '\n' , df[df.Yosh > 30])