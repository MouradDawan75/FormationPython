import sqlite3

cnx = sqlite3.connect('31_Database/db.sqlite3')
cursor = cnx.cursor()

print('>>>>>>> select * from personne') # select nom,prenom from personne

sql = 'select * from personne'
cursor.execute(sql)

personnes = cursor.fetchall()

print(personnes) # est une liste de tuples

# unpacking

for id,nom,prenom,age in personnes:
    print(f'Id: {id} - Nom: {nom} - Prénom: {prenom} - Age: {age}')


print(cursor.fetchall()) # contenu du cursor consommé à la ligne 11 -> cursor réinitialisé en mémoire

print('>>>>>>> select * from personne where id=?')

sql = 'select * from personne where id=?'

cursor.execute(sql, (3,))

print(cursor.fetchone())
print(cursor.fetchone()) # None

print('>>>>>>> select * from personne where nom like ?')

sql = 'select * from personne where nom like ?'

# f% -> nom commençant par f
# %f -> nom se terminant par
# %f% -> nom contenant f quelque soit sa position dans le nom

params = ('%n%',)
# ou params = ['%n%']

cursor.execute(sql,params)

print(cursor.fetchall())