import pandas as pd

df = pd.read_csv("./train.tsv", sep="\t", names=['Cena', 'Pokoje', 'Metraz', 'Pietro', 'Adres', 'Opis'])


"""

df[["Cena", "Pokoje"]]

df["Cena"]

df["Cena"][0]


pd.set_option('display.max_colwidth', -1)

df[["Cena", "Pokoje"]]

df.info()
"""


# Average value - zadanie 1
# int(df["Cena"].mean()) - nie zaokrągla
average = round(df["Cena"].mean(), 0) # bez miejsc po przecinku, 2 jesli 2 miejsca po przecinku
result0 = {"Średnia_cena" : [average]} #zapisauje nam dane w takiej formie srednia i wartosc, przygotowuje dane
df0 = pd.DataFrame(result0) # tworzymy date frame, tą tabelę
df0.to_csv("out0.csv", index = False) # zapisz do pliku o nazwie, bez indeksow 

# bez nazw kolumn
# df0.to_csv("out0.csv", header = None)

# Square meter - zadanie 2
df1 = df 
df1["CenaZaMetr2"] = df1["Cena"]/df1["Metraz"]
df1["CenaZaMetr2"] = round(df1["CenaZaMetr2"], 2) #zaokraglenie do 2 miejsc 
average2 = round(df["CenaZaMetr2"].mean(), 2) #srednia za m2
print("Srednia cena za metr kwadratowy wynosi: ", average2)
print(df1) #drukuj 

df1_final = df1[(df1["Pokoje"] >= 3) & (df1["CenaZaMetr2"] < average2)] #cena za m2 mniej niz srednia 

print(df1_final)
df1_final = df1_final[['Pokoje', 'Cena', 'CenaZaMetr2']]
df1_final.to_csv("out1.csv", index = False) #zapisuje do pliku 
print(df1_final)

# Join - zadanie 3
df_des = pd.read_csv("./description.csv", sep=",") # sep=separator oddziela kolumny od siebie tutaj to jest przecinek
print(df_des)

df2 = df.merge(df_des, how="left", left_on = ['Pietro'], right_on = ['liczba']) # merge = join left 
print(df2)
df2.to_csv("out2.csv", index = False) # zapisujemy do pliku 