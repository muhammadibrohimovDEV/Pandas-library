import pandas as pd

data = {
    'Davlat': ['USA', 'USA', 'UK', 'UK', 'Germany', 'Germany'],
    'Shahar': ['New York', 'Los Angeles', 'London', 'Manchester', 'Berlin', 'Munich'],
    'Aholi': [8500000, 4000000, 9000000, 550000, 3500000, 1400000]
}


df = pd.DataFrame(data)

df = df.set_index(['Davlat' , 'Shahar'])
print(df , '\n')

print(df.loc['Germany' , 'Berlin'] , '\n')


df = df.sort_index()
print(df , '\n')

df = df.xs('UK')
print(df)