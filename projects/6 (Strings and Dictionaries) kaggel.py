# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:47:06 2021

@author: SAID Faten Racha
"""

"------------------------------------Strings-------------------------------------------"

x="cc racha"; print(x)
y='cc racha'; print(y)
print(x==y)

print("\n")
z='cc "SAID faten racha" ' #pr afficher les "" on mets thes tring entre''
print(z)

z="cc 'SAID faten racha'" #pr afficher les '' on mets thes tring entre ""
print(z)

print("\n")
a='it\'s racha\'s shirt' ;  #afficher les caracteres litereaux avec un \
b="it's racha's shirt"; 
print(a)
print(b)

print("\n")
d="""cc
racha""" #ecrire sur plusieurs lignes
e="cc\nracha"
print (d)
print(e)
print(e==d)

print("\n")
#pr avoir un systout.print au lieux du sysout.println automatiquement definit avec le print() de python:
print("cc ", end="")
print("racha")

print("\n")
#afficher des caracteres precis d'une chaine (string)
print(x[3])
print(x[-1])
print(x[3:])
print(x[-2:])

print("\n")
#loop f une chaine
f=[char+"!" for char in x] #ajouter un ! a chaque caractere de la chaine x et mettre tt ca dans le tableau f
print(f)


#ATTENTION : a major way in which they differ from lists is that they are immutable. We can't modify them.
#x[4]='o' --> erreur


print("\n")
x1="Cc Racha"
#transformer la chaine en majusules
x2=x1.upper()
print(x2)

#transformer la chaine en minuscule
x3=x1.lower()
print(x3)


print("\n")
#chercher une sous-chaine dans une chaine
i=x.index("racha")
print(i)


print("\n")
#trasformer une chaine en une liste
liste=x.split()
print(liste)

#trasformer une chaine en une liste (en lui supprimant une sous chaine)
dateStr="16-02-2021"
jj,mm,aa=dateStr.split("-")
print(jj) 
print(mm) 
print(aa) 

dateStr2="/".join([jj,mm,aa]) #ajouter une sous chaine a une liste de chaines (on obtient une chaine)
print(dateStr2)



print("\n")
#concatenation                                                                 #new
age=20
str1="cc "+"racha "+'tu as '+ str(age)+" ans !"
print(str1)


str2="{} racha tu as {}".format(x[0:2],age) #fill in the gaps
print(str2)

print("\nfill in the gaps evolué:")
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)



"------------------------------------Dictionaries-------------------------------------------"
print("\n")
print("\n")

#premiere facon de la declarer
algerie={"one":1, "two":2, "tree":3, "viva l'algerie":4}
print(algerie) #afficher le dico (la map ga3 ki clé ki val)

print(algerie["viva l'algerie"]) #afficher la valeur de la clé=="viva l'algerie"

algerie["viva l'algerie"]=10 #modifier la valeur de la clé=="viva l'algerie" 
print(algerie)

algerie["viva l'algerie"]="ta7ya dzayer" #modifier la valeur de la clé=="viva l'algerie" en utilisant un string
print(algerie)


#seconde facon de le declarer
algerie2={}
algerie2["one2"]=1
algerie2["two2"]=2
algerie2["tree2"]=3
print(algerie2)


print("\n")
#construire un dico a partir d'une liste existante
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planetes_initial={unePlanete: unePlanete[0] for unePlanete in planets}
print(planetes_initial)


print("\n")
#verifier que le dico contient ou nn ces clé
bool1="one" in algerie
bool2="four" in algerie

print(bool1)
print(bool2)

#afficher tt les clé
print(algerie.keys())

#afficher toutes les valeurs
print(algerie.values())


# Get all the initials, sort them alphabetically, and put them in a space-separated string.
cleOrdreAlphabetique=" ".join(sorted(algerie.keys()))
print(cleOrdreAlphabetique)
#PS: on aurait pu faire de mm avec les valeurs mais SEULEMENT si elle étaient TOUTES de type string
#valeurSeparee=" ".join(algerie.values()) --> erreur


print("\n")
#boucle et dico
for i in algerie:
    print("{} = {}".format(i,algerie[i])) #i c la clé ("one" ou "two" ..) et algerie[i] sa valeur (1 ou 2 ..)


# planetes_initial.items() retourn a la fois la clé et les valeur du dico
for planet, initial in planetes_initial.items():                               #new!
    print("{} commence avec {}".format(planet, initial))


print(planetes_initial.items()) 
#PS : pr l'itteration on DOIT ajouter le .items()

#help(algerie) #pr plus d'info 


"-----------------Exo------------------"
print("\n")
print("\n")

doc_list=['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']
keyword='casino'

indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
    
    print(doc_list)
    print(i) #index des element du tab
    print(doc) #le contenu du tab a chaque i
    
    tokens = doc.split()
    
    print(tokens)
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
    normalized = [token.rstrip('.,').lower() for token in tokens] #reja3naha un tab avec contenant a chaque fois une chaine en minuscule
    
    print(normalized)
    
    
        # Is there a match? If so, update the list of matching indices.
    if keyword.lower() in normalized:
        indices.append(i)
print (indices)



