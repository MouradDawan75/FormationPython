# string: est une collection ordonnée immuable
s = 'test'
s = s.upper() # par définition, le type str est immuable
print(s)

texte = ' ceci est une chaine '
print(texte.upper())
print(texte.lower())
print('ceci' in texte)
print(texte.startswith('ceci')) # False
print(texte.endswith('chaine ')) # True
print(texte.strip()) # suppression des éspaces en début et fin de chaine
print(texte.rstrip())
print(texte.lstrip())
print(texte.replace('e', 'a'))
print(texte.replace('e', 'a', count=1))
print(texte.find('chaine'))
print(len(texte))

print('>>>>>> split:')

mots = texte.split()
print(mots)

st = 'mot1,mot2,mot3,mot4'
print(st.split(',', 2))

print("fichier.notes.pdf".rsplit('.',1)[1])
print("fichier.notes.pdf".replace('pdf','txt'))

print(' '.join(['ceci', 'est', 'un', 'paragraphe']))



print('>>>>>>>>>>>>>>>>>>>>>> module string:')

import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

# En Python, les chaines sont encodées en utilisant l'Unicode. Chaque caractère est positionné
# dans une table et dispose d'une position dans cette table, nommé ordinal.
# A à pour ordianal 65
# a à pour ordinal 97

print([chr(x) for x in range(191,564)])

print('>>>>>>>>>>>>>>>>> chaine brute: raw string')
# chaine vernatime

chemin = r'c:\newFolder\notes.txt'

print('>>>>>>>>>> chaine en octets: bytes')

my_string = 'Helo, world'

mystr_byte = my_string.encode(encoding='utf-8')

print(mystr_byte)

# les types str et bytes sont immuables.
# str est une séquence de caractères
# bytes est une séquence d'entiers compris entre 0 et 255 (représentation sur 8 bits - 1 octet)

my_byte_string = bytearray('Hello, world', 'utf-8')
m1 = memoryview(my_byte_string)

print(m1[0])
m1[1] = 105
print(my_byte_string)

print('>>>>>>> Codage ASCII')
my_byte = b'Python'

print(my_byte)
print(type(my_byte))
print(my_byte[0])
print(list(my_byte))

print(chr(80))

print('>>>>> Codage UTF-8')
# est le codage le plus ourant qui est un encodage Unicode sur 8 bits
# les 128 char ASCII sont représenté par les mêmes entiers dans UTF-8, mais d'autres caractères peuvent
# également être représentés en utilisant 2 octets ou plus

chaine_byte = bytes('café', 'utf-8')
print(chaine_byte)

print(">>>>>>> gestion des erreurs d'encodage")

chaine = 'Café £2.20' # 2 char non ASCII

result = chaine.encode()

print(result) # les char non ASCII sont remplacés par leur séquences d'échappement hexadécimales

print('___________ Encodage ASCII:')

chaine = 'Café £2.20' # 2 char non ASCII
# ascii_result = chaine.encode('ascii')

# print(ascii_result)

# Option1: ignorés les char non ascii

ascii_result = chaine.encode('ascii', errors='ignore')
print(ascii_result)

# Option2: remplacer les char non ascii

ascii_result = chaine.encode('ascii', errors='replace')
print(ascii_result) # les chars non ascii sont remplacés par ?

# Option3: remplacer les char non ascii par \

ascii_result = chaine.encode('ascii', errors='backslashreplace')
print(ascii_result) # les chars non ascii sont remplacés par \

# Option4: remplacer les char non ascii par sa représentation xml

ascii_result = chaine.encode('ascii', errors='xmlcharrefreplace')
print(ascii_result) # les chars non ascii sont remplacés par xml ref

# Option5: remplacer les char non ascii par eur nom formel

ascii_result = chaine.encode('ascii', errors='namereplace')
print(ascii_result) # les chars non ascii sont remplacés par leur nom formel

# La conversion de chaines en octets est une opération qui trouve application dans divers domaines
# de la data science:
# - Traitement du langage naturel (NPL)
# - Nettoyage des données
# - Le scrping et l'extraction de données web
# - compression de données

import gc

collected = gc.collect() # cet appel explicite ne garantit pas le passage immédiat du garbage collector
print(collected)

