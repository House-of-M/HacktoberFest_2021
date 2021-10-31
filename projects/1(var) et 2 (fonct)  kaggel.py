# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 09:50:34 2021

@author: SAID Faten Racha
"""
#My first comment !

x=5
print("the value of x is", x,"yaaaay")
y="abc" * x                                                                    #NEW !
print(y)
if x < 8:
    print("if cond")
    print(x,"is lower then 8")
else:
    print("else cond")   
    x=x*4

print("the value of x is", x,"yaaaay")
y="abc" * x
print(y)


z=2.0
print(type(z))                                                                 #NEW !
print(type(x))
print(type(y))
print("ok")


print(x//z) #5/2==2.5 yakhod wech kayen avant la virgule berk                  #NEW !
print(x%z)  #modulo  yakhod 7assil el 9sima                                                          
print(x**z) #x puissance z                                                     #NEW !


print(min(x,z))                                                                #NEW !
#print(min(x,y,z)) tmedli erreur psk y est un str                              #ERROR X
print(abs(-12)) #valeur absolue                                                #NEW !
print(int(z))
print(float(x))
#print(int(y))  psk y est un str                                               #ERROR X

#trick to swap two variables in one line:                                      #NEW !
x, z = z, x
print(x)
print(z)

#Documentation                                                                 #NEW !
help(print)
help(round)
#help(print(x)) il faut mettre le mot clé et pas appeler la fonction           #ERROR X

#------------------------------------FONCTION--------------------------------------------

def LeDouble(a):
    return a*2

def Somme(a,b):                                                                #NEW !
    """docstrings                                                              #NEW !
    Je crée cette docummentation grace aux commentaire ajouter a la fonct"""  
    "Ce type de commentaire est valable aussi il suffit de choisir un des 2 types mais pas les deux a la fois"
    #ATTENTION ca ne marche PAS avec ce type de commentaires                                                           
    
    print("La somme de ",a,"+",b, "est :",a+b)
    return a+b

print(Somme(8,4));
help(Somme)

#---Default arguments                                                          #NEW !

#Attribuer une valeur par defaut
def Multipication(who="Racha"):
    print("Hello",who)

Multipication() #on a rien specifier donc prend la valeur par defaut
Multipication("Amina")
Multipication(who="Wassim")
    

    
#---Functions Applied to Functions                                             #NEW !
def CoolFunction(uneFontion,x,y):
    return uneFontion(x,y) 

CoolFunction(Somme,10,3)


def CoolerFunction(uneFontion,x):
    return uneFontion(uneFontion(x))#une fonction qui fait appel a elle mm 
                                    #(condition qu'elle ai comme argument un att et qu'il soit du type envoyé)
    
print(CoolerFunction(LeDouble,5))




"""By default, max returns the largest of its arguments. 
But if we pass in a function using the optional key argument, 
it returns the argument x that maximizes key(x) (aka the 'argmax')."""

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)








