import sqlite3

cnx = sqlite3.connect('31_Database/db.sqlite3')
cursor = cnx.cursor()

sql = 'update personne set nom=:last_name,prenom=:first_name,age=:age where id=:id'

# les params peuvent avoir le mm nom que les champs: c'est le cas de id et age

# les params anonymes ? sont founis via un tuple
# les params nommés sont via un dict

params = {
    'id': 3,
    'last_name' : 'new_nom',
    'first_name': 'new_prenom',
    'age': 99
}

cursor.execute(sql,params)
cnx.commit()