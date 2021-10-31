# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:37:55 2021

@author: SAID Faten Racha
"""

"--------------------------------------Boucles------------------------------------------"

"---------------For--------------------"
#---sur des listes
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for p in planets:
    print(p, end=' ') # print all on same line

print("\n")

#s.isupper() recuperer la sous chaine de caracteres en majuscule               #NEW!
str1 = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video RACHAsaid .'
msg = ''

for s in str1:
    if(s.isupper()):  
        msg=msg+s
        
print(msg)


#range(n) genere des nombres de 0 a n-1 
for i in range(7):
    print(i)


#---sur des tuples
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1

for m in multiplicands:
    product=product*m

print("le produit =", product)



"---------------while--------------------"
j=6

while j>=0 :
    print(j)
    j -= 1
    
    
"----------------------------List comprehensions-----------------------------" #NEW!
#---For
print("\n")

squares=[nbr**2 for nbr in range(10)] #[resultat boucle]
print(squares)

#EQUIVALENT A :

squares=[]
for nbr in range(10):
    squares.append(nbr**2)
print(squares)





#---For & If
print("\n")
#(If you're familiar with SQL, you might think of this as being like a "WHERE" clause)

shortest_planets=[sp for sp in planets if(len(sp)<6)] #[resultat boucle condition]
print(shortest_planets)

#--opperer une modif sur le contenu a afficher

Majuscule_shortest_planets=[msp.upper()+'!' for msp in planets if (len(msp)<6)]
print(Majuscule_shortest_planets)

#EQUIVALENT A :
    
Majuscule_shortest_planets=[
                             msp.upper()+'!'         #SELECT
                             for msp in planets      #FROM
                             if (len(msp)<6)         #WHERE
                           ]

print(Majuscule_shortest_planets)

#--remarque le resultat
print("remarque le resultat : ",[32 for p in planets])


#--retourner un tableau de boolean

#-Exemple:
"""Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
#option1
def elementwise_greater_than(L, thresh):

    return [False for bool in L if(bool<=thresh)]+[True for bool in L if(bool>thresh)]

#option2
def elementwise_greater_than2(L, thresh):
    return [ele > thresh for ele in L]

L=[1, 2, 3, 4]
print(elementwise_greater_than(L, 2))
print(elementwise_greater_than2(L, 2))

#--Fonction particulieres
print("\n")
#any

def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums]) #retourn true 
                                               #si il existe dans la liste au moins une val 
                                               #(si la liste nums contien au moins un nbr divisible par 7)
tab=[10,2,70,94]
print(has_lucky_number(tab))

#sum
print(sum([num % 7 == 0 for num in tab]))

#len
print(len([num % 7 == 0 for num in tab]))


#---Matrices
print('\n')

M1=[['a' for x in range(4)] for y in range(3)] #LA MEILLUEUREE                 #NEW!
                                               #ME PERMET DE DECLARER KIMA NA7B                      
print(M1)




M2=[['' for x in range(3)] for y in range(3)] #3ayana psk je dois d'abord l'initialisé b hadik la méthode 
                                              #puis je ne peux modifier ses infos que si elle est carrée 
for i in range(3):
    for j in range(3):
        
        if (i<3) and (j<3):
            M2[i][j]='b'
        
print(M2)       
        

#--parcourir un tableau 
meals=['Spam', 'Eggs', 'Spam', 'Spam', 'Bacon', 'Spam']        
        
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i]== meals[i+1]:
            return True

    return False

print(menu_is_boring(meals))
