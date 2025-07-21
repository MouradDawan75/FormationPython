#1)
mot = input('Votre mot: ')

d = {}
for lettre in mot:
    d[lettre] = mot.count(lettre)

print(d)

#2)
nombres = range(10)

d = {e:e**2 for e in nombres if e % 2 == 0}
print(d)