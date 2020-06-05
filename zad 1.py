
#zad 1

import pandas as pd

df = pd.read_csv("./train.tsv", sep="\t", names=['Cena', 'Pokoje', 'Metraz', 'Pietro', 'Adres', 'Opis'])

srednia = df["Cena"].mean()
srednia = round(srednia, 0)
print("Srednia cena mieszkania wynosi:", srednia)



with open("out0.csv", "w") as out0:
    out0.write(str(srednia))

               




