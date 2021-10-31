# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:47:22 2021

@author: SAID Faten Racha
"""


#si tu ne veux rien mettre f ta fonction et eviter une erreur tu tape pass;    #Astuce

"--------------------------------------Boolean------------------------------------------"

#---declarer un bool
x=True; print(x); print(type(x));
y=False
print(int(True))

#---Boolean function version1
def mafonctionBool(age):
    return (age>=30)
    
print(mafonctionBool(25));

if(mafonctionBool(65)):
    print("Personne agé plus de 30 ans");
    

#---Boolean function version2
def mafonctionBool2(age):
   if(age==30):
       return True
   else:
       return False

print(mafonctionBool2(30));
print(mafonctionBool2('30')); #j'ai pu utiliser un string sans erreur          #Attention
                              #psk operateur '==' compatible avec les string 
                              #en revanche avec un '>=' par exp j'aurais eu une erreur
if(mafonctionBool2(65)):
    print("Personne agé plus de 30 ans");

#---Operateurs logiques
def trentenaire(age):
    return ((age>=30) and (age<=40)) #kayen aussi le 'or' et le 'not'          #NEW !

if(not trentenaire(38)):
    print("Personne n'est pas trentenaire"); 

else:
     print("Personne est trentenaire");                         


print(True or True and False) #elle retourne FALSE                             #Attention
                              #psk le and is evaluated before or 
                              #donc pr eviter les erreurs tjrs mettre des parenthèses
 
#---Boolean conversion                                                     
print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"         
                  
"--------------------------------------Conditions------------------------------------------"
rachaHayla=True
if(rachaHayla):
    print("Tu as bien raison")
elif (not rachaHayla):
    print("wech cv chwya ?")
elif (rachaHayla or rachaHayla):
    print("hum je dirais les deux !")
else:
    print("RACHA HAYLA !")
    
    

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies == 1:
        print("Splitting 1 candy")
    else:
        print("Splitting", total_candies, "candies")
    
    #EQUIVALENCE entre les deux ecritures
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")#NEW !

to_smash(91)
to_smash(1)

