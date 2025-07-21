#1)Nouvelle liste ne contenant que les nombres positifs

nombres = range(-10,10)
nombres_positifs = [e for e in nombres if e > 0]

#2)Nouvelle liste en inversant uniquement les nombres impairs: 0,-1,2,-3,4.....
nombres = range(10)

nombres_inverses= [e if e % 2 == 0 else -e for e in nombres]

#3)Afficher le nombre d'éléments supérieurs à 3
lst = [2,3,6,1,9,7]
print("Nombre d'éléments sup à 3:",len([e for e in lst if e > 3]))

#4)Différence entre 2 listes (listA - listB) -> résultat est une liste = [3,4]
listA = [1,2,3,4]
listB = [1,2]

liste_difference = [e for e in listA if e not in listB]