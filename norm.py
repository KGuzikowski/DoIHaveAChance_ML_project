import csv, pandas as pd
df = pd.read_csv('DoIHaveAChance_ML_project/speed_dating.csv')
def func(lista):
    selected_df = df[lista]
    print(selected_df)

    for x, row in selected_df.iterrows():
        multiplier = 100/row.sum()
        for col in lista:
            df.at[x, col] *= multiplier
    print(df[lista])

lista = ["attr1_1", "sinc1_1", "intel1_1", "fun1_1", "amb1_1", "shar1_1"]
lista1 = ["attr_o", "sinc_o", "intel_o", "fun_o", "amb_o", "shar_o"]
lista3 = ["attr2_1", "sinc2_1", "intel2_1", "fun2_1", "amb2_1", "shar2_1"]
lista4 = ["attr1_2", "sinc1_2", "intel1_2", "fun1_2", "amb1_2", "shar1_2"]
func(lista)
func(lista1)
func(lista3)
func(lista4)
df.to_csv('filtered_data.csv', index=False)