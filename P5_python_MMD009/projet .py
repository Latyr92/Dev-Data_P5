from csv import reader
from Mesfonctions import *
# import numpy as np
# import matplotlib.pyplot as plt
list=[]
list_invalide=[]

with open("/home/faye/Downloads/Donnees_Projet_Python_DataC5.csv","r") as monlecteur:
    monlecteur_csv=reader(monlecteur,delimiter=',')
    #donnees.shape
    # list_valide=[]
    # list_invalide=[]
        #print(i)
    for i in monlecteur_csv:
        print(i, end='\n')
        list.append(i)
        #print('La variable tableau est égale à :\n',list_valide)

        if '' not in i:
           if det(i[3]):
               list.append(i[3])
               #print(list)
           if det_nom(i[2]):
               list.append(i[2])
               #print(list)
           if det_classe(i[5]):
              list.append(i[5])
              #print(list)
           if determine(i[1]):
               list.append(i[1])
               #print(list)
           if det_date(i[4]):
               list.append(i[4])
               #print(list)
           if det(i[6]):
               list.append(i[6])

               #print(list)
    #list.columns
    #print(list)
    for list in monlecteur_csv:
        if det(i[6]):
        #for row in monlecteur_csv:
         monlecteur_csv.writerow(list)
        else:
            monlecteur_csv.writerow(list_invalide)
        
