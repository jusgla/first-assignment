import pandas as pd

df = pd.read_csv("./train.tsv", sep="\t", names=['Cena', 'Pokoje', 'Metraz', 'Pietro', 'Adres', 'Opis'])


df_description = pd.read_csv("./description.csv")
print(df_description)


wynik = pd.merge(df, df_description, how="left",left_on='Pietro', right_on='liczba')
print(wynik)

wynik.to_csv("out2.csv", index = False)

# w myśl tej zasady pd.merge(df1, df2, left_on='nazwa1', right_on='nazwa2')


#wynik = df.merge(df_description, how="left", left_on = ['Pietro'], right_on = ['liczba'])
#print(wynik)


