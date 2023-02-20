from csv import reader
# import numpy as np
# import matplotlib.pyplot as plt

with open("/home/faye/Downloads/Donnees_Projet_Python_DataC5.csv","r") as monlecteur:
    monlecteur_csv=reader(monlecteur)

    def determine(numero):
        for i in numero:
            if len(numero)==7:
              if i.isalnum()==True:
                 return True
                 list.append(True)
            else:
                return False
                list.append(False)

    for i in monlecteur_csv:    
        b=determine(i[1])
        print(b)

    def det_date(naissance):
        if naissance!="":
            naissance=naissance.replace(".","/")
            naissance=naissance.replace(":","/")
            naissance=naissance.replace(" ","/")
            naissance=naissance.replace("_","/")
            naissance=naissance.replace(".","/")
            naissance=naissance.replace(",","/")
            naissance=naissance.replace("-","/")
            return naissance
            for i in monlecteur_csv:
               if 8<=len(naissance)<=10:
                 return naissance
            naissance=naissance.split()
        else:
             return False
    for i in monlecteur_csv:    
        a=det_date(i[4])
        print(a)

    def determine(numero):
        for i in numero:
            if len(numero)==7:
              if i.isalnum()==True:
                 return True
                 list.append(True)
            else:
                return False
                list.append(False)

    for i in monlecteur_csv:    
        b=determine(i[1])
        print(b)


    def det_classe(classe):
       if classe!=" ":
        for i in classe:
           classe.replace(" ","")
           if classe[0] in ["3","4","5","6"] and classe[-1] in ["A","B"]:
               return classe
               list.append(classe)
           else:
               return False
        else:
               return False
               list.append(False)

    for i in monlecteur_csv: 
        c=det_classe(i[5])
        print(c)
      
     
        
    def det(prenom):
    #    prenom_valide=[]
    #    prenom_invalide=[]
        for i in prenom:
            if len(prenom)>=3:
              if prenom.isalpha()==True:
                  return prenom
                  list.append(True)
            else:
                 return False
                 list.append(False)
         
    for i in monlecteur_csv:   
        d=det(i[3])
        print(d)

    def det_nom(nom):
             if nom!="  " and len(nom)>=2:
              for i in nom:
                if nom.isalpha()==True:
                    return nom
                    list.append(nom)
                else:
                 return False
             #list.append(False)
             else:
                 return False
                 list.append(False)

    for i in monlecteur_csv:   
        e=det_nom(i[2])
        print(e)

    def det(note):
      if note!="":
         for i in note:
             note=note.replace("#","")
             note=note.split()
             return note
             list.append(note)
      else:
         return False
         list.append(False)
    
            #list.append(list[:1])    
         #list.remove(math)   
    for i in monlecteur_csv:

        f=det(i[6])
           #f=f.remove(list)
        print(f)    
        

        #    return False 
#          from datetime import date
#         date.fromisoformat("%day/%month/%year")
# #         a=%day/%month/%year

# #         if 1<=%month<=12:
           
 
#         k=""
#          a=[]
#          for i in range(len(a)):
#              if 0<=i<=9 and i=="/":
#                k+=i
#                a.append(k)
#          return a
#       for i in monlecteur_csv:
#           l=date(i[4])
#           print(l)
          
