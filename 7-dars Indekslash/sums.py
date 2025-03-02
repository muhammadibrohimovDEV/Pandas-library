import pandas as pd

data = {
    'ID': [101, 102, 103, 104],
    'Ism': ['Ali', 'Vali', 'Hasan', 'Aziz'],
    'Yosh': [25, 30, 22, 27]
}


df = pd.DataFrame(data)
df = df.set_index('ID')
print(df)

df_reset = df.reset_index()
print(df_reset)

print(df.loc[103])
