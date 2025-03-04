import pandas as pd

data = {
    'Ism' : ['Ali' , 'Vali' , 'Hasan' , 'Husan'],
    'Yosh' : [25 , 30 , 22 , 28],
    'Kasb' : ['Dasturchi' , 'Muhandis' , 'Talaba' , "O'qituvchi"],
    'Shahar' : ['Toshkent' , 'Samarqand' , "Buxoro" , 'Andijon']
}

df = pd.DataFrame(data)

print(df)

indexes = ['A' , 'B' , 'C' , 'D']

df.index = indexes # Index larni o'zgartirish

print(df)

data_main = df.values

print()

for i in data_main:

    for j in range(len(i)):
        if i[j] == 'Talaba':
            i[j] = 'Data Scientist' # "Talaba" ni "Data Scientist" ga o'zgartirish

        if i[j] == 'Buxoro':
            i[j] = "Farg'ona" # "Buxoro" ni 'Farg'ona" ga o'zgartirish

    print(i)

print()

print(data_main)

print()

df = pd.DataFrame(data_main , columns = df.columns)

print(df)

print(df['Yosh'].mean()) # yoshlarning o'rtacha qiymati

print(df)

print(df.describe()) # statistik ma'lumotlarni olish

print(df[df.Yosh > 25]) # Yoshi 25 dan katta insonlarni chop qilish
#
# df.loc[df["Kasb"] == "Talaba", "Kasb"] = "Data Scientist"
# df.loc[df["Shahar"] == "Buxoro", "Shahar"] = "Farg'ona"
#
#
# df["Kasb"] = df["Kasb"].replace("Talaba", "Data Scientist")
# df["Shahar"] = df["Shahar"].replace("Buxoro", "Farg'ona")
