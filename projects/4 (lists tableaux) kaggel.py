# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 22:53:26 2021

@author: SAID Faten Racha
"""

"--------------------------------------Tableaux(listes) & Matrices------------------------------------------"
print("\n--Tableaux & Matrices")
t1=[5,4,3,2]
t2=[14,0,-8,10,15,43,0,-76]
t3=["RACHA",'f','aten']
t4=['a',4,'Wassila']
t5=["be",'zu',"ax","tp"]

M1=[[5,7],[0,0]]
M2=[[5,7,2],[57,27,12],[1000,0],[4]]                                           #NEW!


print(t1,"\t",t1[0],"\t",t1[2],"\t",t1[-1]);                                   #NEW!
print(t2, "\t",t2[-2])
print(t3)
print(t4)
print(t2[2:4])                                                                 #NEW!
print(t2[:4])                                                                  #NEW!
print(t2[2:])                                                                  #NEW!
print(t2[-3:])                                                                 #NEW!
print(t2[2:-1])                                                                #NEW!

print(M1,"\t", M1[0][0]);
print(M2,"\t", M2[1][2]);

t3[1:]=['FATEN',"SAID"] #on modifis les val du tab a partir de l'indice num1   #NEW!
t1[-3:]=[6,7,8] #on modifis les 3 dernieres val du tab                         #NEW!

print(t3)
print(t1)

"--------------------------------------Fonctions sur Tableaux & Matrices------------------------------------------"
print("\n--Fonctions sur Tableaux & Matrices")                                 #NEW!

#taille
print(len(t1)) #la taille du tableau
print(len(t4))
print(len(M1)) #la taille de la matrice

#trie
print(sorted(t3)) #trie selon l'odre alphabetique
print(sorted(t2)) #trie selon l'ordre croissant des val

#sommation des val d'un tableau
print(sum(t2)) #on aurait eu une erreur                                        #Attention
               #si on avait essayer de sommer un tab qui contient des strings

#Max
print(max(t2))
print(max(t3)) #ordre alphabtique max
print(max(t5))
print(max(M2))

#append ==empiler== ajouter a la fin de la liste 
t1.append(9) #modifies a list by adding an item to the end
print(t1)

#pop ==depiler== supprimer a la fin de la liste
print(t1.pop()) #removes and returns the last element of a list
print(t1)

print(t2.pop(2)) #supprime (depile) le 2 eme element a partir de la fin 
print(t2)

#recherche
print(t2.index(0)) #j'avais 2 val ta3 0 f t2, il m'a affiché la premiere occurence ta3ou
print(t3.index('SAID')) #loukan ktebt "said"                                   #Erreur
                        #j'aurais eu une erreur du type 'said' is not in list
                        #To avoid unpleasant surprises like this, 
                        #we can use the in operator to determine whether a list contains a particular value:
print("RACHA" in t3)
print("Amina" in t3)

#effacer le contenu d'un tableau
t1.clear()
print(t1)

t1=t2.copy()  
print(t1)                      

"--------------------------------------POO------------------------------------------"
print("\n--POO")

s="abc"
x = 3 # x is a real number, so its imaginary part is 0.

#on fait appel a  des methodes contenu dans la classe variables
print(x.bit_length()); #calcul le nbr de bits necessaire pr codé la val decimale de x
help(int.bit_length)
print(x.imag) #imag var predefinit dans la classe des nombres

# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

#print(help(t3)) #afficher la docu sur le type de cet objet                    #NEW!
                 #(ga3 les methodes et att qu'il contient)
#print(help(x))

"--------------------------------------Tuples------------------------------------------"
print("\n--Tuples")
#tuple kima listes a qlq exceptions près :
   #1: The syntax for creating them uses parentheses instead of square brackets
t = (1, 2, 3)
   #2: They cannot be modified (they are immutable).
#t[0]=5  

#Tuples are often used for functions that have multiple return values exp:
x = 0.125
print(x.as_integer_ratio())    


