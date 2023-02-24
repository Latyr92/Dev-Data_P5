notes_des_eleves= 'SVT[12|20:19] #PC[13|14:10] #Francais[14|18:19] #SVT[16|19:14] #Anglais[14|15:18] #HG[10|07:20] #Math[19|17:18]'.split('#')
eleve = ['AMG015', 'SONA003', 'DIOP', 'YOUSSOU', '12/06/94', '5emA', 'Math[04|03:05] #Francais[15|16:14] #Anglais[15|16:17] #PC[04|03:07] #SVT[12|09:10] #HG[16|15:17]']
import csv
def transformer_csv_en_liste_de_liste(fichier):
  with open(fichier,"r") as f:
    csv_f = csv.reader(f)
    list_eleve = []
    for ligne in csv_f:
      list_eleve.append(ligne)
    return list_eleve
  # Retourne une liste de liste d'èleves

def DictMatiere(ch):
  try:
    tmp = ch.replace("[","-").replace("|","-").replace(":","-").replace("]","-").split("-")
    del tmp[-1]
    return {tmp[0]:{
        "devoir": [float(x) for x in tmp[1:-1]],
        "examen": float(tmp[-1])
    }}
  except Exception as e:
    ""

def TransformerNoteEnDictionnaire(notes):
  matieres = {}
  for n in notes:
    m = DictMatiere(n)
    matieres.update(m)
  return matieres


dict_note = TransformerNoteEnDictionnaire("Math[04|03:05] #Francais[15|16:14] #Anglais[15|16:17] #PC[04|03:07] #SVT[12|09:10] #HG[16|15:17]".split("#"))
dict_note
def TransformerEleveEnDictionnaire(e):
  try:
    return {
        "code": e[0],
        "numero": e[1],
        "nom":e[2],
        "prenom": e[3],
        "date_de_naissance": e[4],
        "classe": e[5],
        "notes": TransformerNoteEnDictionnaire(e[6].split("#"))
    }
  except Exception as e:
    ""

def det_nom(nom):
   if nom!="  " and len(nom)>=2:
      for i in nom:
       if nom.isalpha()==True:
         return True
      else:
            return False

def determine(numero):
      for i in numero:
       if numero!="":
         if len(numero)==7:
          if i.isalnum()==True:
            return True
            #liste.append(True)
         else:
            return False
      else:
            return False
      
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
              return True
         #naissance=naissance.split()
   else:
      return False
   
def det_classe(classe):
   if classe!="":
    for i in classe:
      classe.replace(" ","")
      if classe[0] in ["3","4","5","6"] and classe[-1] in ["A","B"]:
            return True
            #liste.append(True)
      else:
            return False
   else:
      return False
      #tab.append(False)

def det(prenom):
#    prenom_valide=[]
#    prenom_invalide=[]
   for i in prenom:
      if len(prenom)>=3:
         if prenom.isalpha()==True:
               return True
               #liste.append(True)
         else:
            return False
            #tab.append(False)

def calcul_de_la_moyenne(e):
  somme_des_moyennes = 0
  for n in e["notes"]:
    devoir = e["notes"][n]["devoir"]
    somme_des_devoirs = 0
    nombre_de_devoir = len(devoir)
    for i in devoir:
      somme_des_devoirs+=i
    # La moyenne des devoirs d'une seule matière
    moyenne_des_devoir=somme_des_devoirs/nombre_de_devoir
    # La moyenne générale d'une seule matière
    moyenne_general = (moyenne_des_devoir+(2*e["notes"][n]["examen"]))/3
    somme_des_moyennes+=moyenne_general
    print("La moyenne générale en {} est {:.2f}".format(n,moyenne_general))
  moyenne = somme_des_moyennes/len(e["notes"])
  print("La moyenne de {} {} est {:.2f}".format(e["nom"],e["prenom"],moyenne))


###"-----------------------PROGRAMME PRINCIPAL-----------------------------------------"
# e = TransformerEleveEnDictionnaire(eleve)
all = transformer_csv_en_liste_de_liste("data.csv")
# print(type(all[-1][6]))
tab_eleves = []
for i in all:
  Eleve = TransformerEleveEnDictionnaire(i)
  tab_eleves.append(Eleve)

good_eleves = []
bad_eleves = []
def lesnotes(note_des_eleve):
     #for i in e["note"]:
     for i in notes_des_eleves:
      try:
        good_eleves.append(i)
        #print(good_eleves)
      except Exception as e:
        bad_eleves.append(i)
        
        
lesnotes(good_eleves)

good_eleves = []
bad_eleves = []
for el in tab_eleves:
  print(el)
  try:
   if det_nom(el["nom"]) and determine(el["numero"]) and det_date(el["date_de_naissance"]) and det_classe(el["classe"]) and det(el["prenom"]): #and calcul_de_la_moyenne(el["notes"]):
    good_eleves.append(el)
    calcul_de_la_moyenne(el)
   else:
    bad_eleves.append(el)
  except Exception as e:
   bad_eleves.append(el)


print(bad_eleves) 
