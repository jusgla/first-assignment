import pandas as pd
import matplotlib.pyplot as wykres
import numpy as np

dane = pd.read_csv('survey_results_public.csv', usecols=['Respondent', 'CompTotal', 'Age', 'WorkWeekHrs', 'Gender'], index_col='Respondent')  #wczytywanie #str nazwa pliku

#schemat = pd.read_csv('survey_results_schema.csv') #schemat danych - niepotrzebny, bo już znam kolumny :)


#podział na kobiety i mężczyzn
dane_mezczyzni = dane[dane['Gender'] == 'Man']
dane_kobiety = dane[dane['Gender'] == 'Woman']


#Drukowanie przykładowych danych posortowanych  względem liczby godzin przepracowanych tygodniow0 - widać, że są błędy - np. 4125 godzin - tyle nie ma w tygodniu
print(dane_mezczyzni.sort_values(by='WorkWeekHrs', ascending=False).head(10))
print("\n\n")
print(dane_kobiety.sort_values(by='WorkWeekHrs', ascending=False).head(10))


#Wykresy pracy godzinowej w zaleznosci od wieku i płci:

#wykres dla mezczyzn
wykres.plot(dane_mezczyzni['Age'], dane_mezczyzni['WorkWeekHrs'], 'ro')
wykres.xlabel('Age')
wykres.ylabel('WorkWeekHrs')
wykres.show()


#wykres dla kobiet
wykres.plot(dane_kobiety['Age'], dane_kobiety['WorkWeekHrs'], 'ro')
wykres.xlabel('Age')
wykres.ylabel('WorkWeekHrs')
wykres.show()




#Wykresy z odfiltrowanymi danymi, bo  w tygodniu mamy maksymalnie 168h - to już dodatkowo zrobiłam, żeby wyszły ładniejsze wykresy i żeby usunąć nieprawdziwe dane (powyżej 168h tygodniowo, chociaż i tak się nie da tyle pracować przecież)

dane_mezczyzni = dane_mezczyzni[dane_mezczyzni['WorkWeekHrs']<=168]
dane_kobiety = dane_kobiety[dane_kobiety['WorkWeekHrs']<=168]

#wykres dla mezczyzn
wykres.plot(dane_mezczyzni['Age'], dane_mezczyzni['WorkWeekHrs'], 'ro')
wykres.xlabel('Age')
wykres.ylabel('WorkWeekHrs')
wykres.show()


#wykres dla kobiet
wykres.plot(dane_kobiety['Age'], dane_kobiety['WorkWeekHrs'], 'ro')
wykres.xlabel('Age')
wykres.ylabel('WorkWeekHrs')
wykres.show()
