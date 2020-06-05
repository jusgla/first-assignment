import pandas as pd

df = pd.read_csv("./train.tsv", sep="\t", names=['Cena', 'Pokoje', 'Metraz', 'Pietro', 'Adres', 'Opis'])


df["CenaZaMetr2"] = df["Cena"]/df["Metraz"]

srednia_cena_za_m2 = df["CenaZaMetr2"].mean()
srednia_cena_za_m2 = round(srednia_cena_za_m2, 2)
print("Srednia cena za metr kwadratowy wynosi: ", srednia_cena_za_m2)

df = df[df["CenaZaMetr2"] < srednia_cena_za_m2] 
df = df[df["Pokoje"] >= 3]


print(df)


df = df[['Pokoje', 'Cena', 'CenaZaMetr2']] 

df.to_csv("out1.csv", index = False)

print(df)


