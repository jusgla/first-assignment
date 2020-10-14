import pandas as pd
import matplotlib.pyplot as wykres
import numpy as np



dane = pd.read_csv('survey_results_public.csv', usecols=['Respondent', 'CompTotal', 'Age', 'WorkWeekHrs', 'Gender'], index_col='Respondent')  





#Zad 1
pd.set_option('max_columns', None) 
daneAll = pd.read_csv('survey_results_public.csv', index_col='Respondent')  
print()
print("Przykładowe dane:")
print(daneAll.head(10))
print()
print("----------------------------------------------------------------------------------------------------")
print(daneAll.corr())
print("----------------------------------------------------------------------------------------------------")
print(daneAll.describe())
print("----------------------------------------------------------------------------------------------------")
print()

pd.reset_option('max_columns') #powrót do domyślnych wartości jeżeli chodzi o drukowanie kolumn


"""
Tutaj widzę dwie opcje zmiennych objaśnianych i objaśniających:
y = 'ConvertedComp'
x1 = 'Age'
x2 = 'CompTotal'

lub:

y = 'CompTotal'
x1 = 'ConvertedComp'
x2 = 'CodeRevHrs'
"""


"""
Dodatkowe dane ze schematu (z pliku survey_results_schema.csv):

    CompTotal,"What is your current total compensation (salary, bonuses, and perks, before taxes and deductions), in `CurrencySymbol`? Please enter a whole number in the box below, without any punctuation. If you are paid hourly, please estimate an equivalent weekly, monthly, or yearly salary. If you prefer not to answer, please leave the box empty."

    ConvertedComp,"Salary converted to annual USD salaries using the exchange rate on 2019-02-01, assuming 12 working months and 50 working weeks."

    WorkWeekHrs,"On average, how many hours per week do you work?"

    CodeRevHrs,"On average, how many hours per week do you spend on code review?"

    Age,"What is your age (in years)? If you prefer not to answer, you may leave this question blank." 

    Hobbyist,Do you code as a hobby?

    BetterLife,Do you think people born today will have a better life than their parents?

"""


#Zad 2

daneAll['Hobbyist'] = daneAll['Hobbyist'].replace("Yes", 1)
daneAll['Hobbyist'] = daneAll['Hobbyist'].replace("No", 0)

#testowa korelacja
#print(daneAll.corr())

#kodowanie one hot encoding za pomocą Pandas
one_hot_encoding = pd.get_dummies(daneAll['BetterLife'])
print(one_hot_encoding)
daneAll = daneAll.join(one_hot_encoding)

#wydrukowanie pierwszych 10 wierszy na ekranie - tutaj mamy już: skonwertowaną kolumnę Hobbyist oraz one hot encoding dla kolumny BetterLife
print(daneAll[['CompTotal', 'Age', 'WorkWeekHrs', 'Gender', 'Hobbyist', 'BetterLife', 'Yes', 'No']].head(10))
