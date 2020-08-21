import pandas as pd
import matplotlib.pyplot as wykres
import numpy as np

dane = pd.read_csv('survey_results_public.csv')

x=dane.iloc[:,29]

y=dane.iloc[:,31]


wykres.scatter(x,y) #plot linia # punkty

wykres.show()









