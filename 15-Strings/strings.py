s = 'test'

s = s.upper()

print(s)

# Le type String par définition est immuble

texte = ' ceci est une chaine '

print(len(texte))
print(texte[0]) # premier caractère
print(texte[-1]) # dernier caractère
print(texte.strip()) # suppression des espaces de début et de fin de chaine
print(texte.rstrip())
print(texte.upper())
print(texte.lower())
print(texte.replace('e', 'a'))
print(texte.replace('e', 'a', count=1))
print(texte.replace('une chaine', 'un paragraphe'))

print('>>>>>> Découper une chaine:')

print(texte.split())

chaine_csv = 'mot1,mot2,mot3,mot4'

print(chaine_csv.split(','))

nom_fichier = 'notes.etudiants.pdf'

print(nom_fichier.rsplit('.', 1)[1])

print(texte.startswith(' ceci'))
print(texte.endswith(' chaine '))
print(texte.count('e'))

print(texte.find('une')) # renvoie l'index de début du mot une dans la chaine
print(texte.find('Une')) # renvoie -1 si non trouvé 