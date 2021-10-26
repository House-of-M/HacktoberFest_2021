# récupérer la chaine 
string = input('entrez la chaine à compresser :\t')

# définir une fonction qui compare entre deux éléments d'une chaine jusqu'à ce qu'ils soient identitiques 
def not_identical(string):
	i=0
	while(i<len(string)-1 and string[i]!=string[i+1]):
		i+=1
	return i

# définir une fonction qui compare entre deux éléments d'une chaine jusqu'à ce qu'ils ne soient pas identitiques
def identical(string):
	i=0
	while(i<len(string)-1 and string[i]==string[i+1]):
		i+=1
	return i

# concatène la liste contenant les suites de chaines identiques/non identiques
# quand deux chaines de suite commencent par 0, on enlève le zéro de la deuxième chaine
def concat(list):
	compressed=list[0]
	for i in range(1, len(list)):
		if(list[i][0]=='0' and list[i-1][0]=='0'):
			compressed+=list[i][1:]
		else: 
			compressed+=list[i]
	return compressed

# Pour implémenter la compression des chaînes, le traitement est séparé en deux parties : 
# Les bouts de chaînes répétitifs 
# Les bouts de chaînes non répétitifs
# Chaque bout de chaîne est stocké dans une liste. La liste est stockée pour construire la chaine compressée par concaténation.

def compression(string):
	(a_concatener, liste_chaines)=("", [])
	while(len(string)-1>=0):
		if(identical(string)+1>=3 and identical(string)+1<=len(string)):
			liste_chaines.append(str(len(string[:identical(string)])+1) + string[identical(string)])
			string=string[identical(string)+1:] 
		else:
			a_concatener = string[:identical(string)+1]
			string=string[identical(string)+1:]
			liste_chaines.append("0" + a_concatener + string[:not_identical(string)])
			string=string[not_identical(string):]
	return concat(liste_chaines)

def taux_compression(string):
	return len(compression(string))/len(string)*100

print("chaine compressée: "+compression(string))
print("taux de compression de la chaine: "+str(taux_compression(string))+"%")