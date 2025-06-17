#1) 
nombres = range(-10,10)
nombres_positifs = [e for e in nombres if e >= 0]

#2)
nombres = range(10)
nombres_inverses = [-e if e % 2 != 0 else e for e in nombres]

#3)
lst = [1,7,4,2,9,5]
print(len([e for e in lst if e > 3]))

#4) 

def somme_entiers_pairs_distincts(entiers: list[int]) -> int:

    # construire une liste ne contenant que les pairs distincts
    lst = []

    for e in entiers:
        if e % 2 == 0 and e not in lst:
            lst.append(e)

    return sum(lst)