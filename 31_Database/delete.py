import sqlite3

cnx = sqlite3.connect('31_Database/db.sqlite3')
cursor = cnx.cursor()

sql = 'delete from personne where id=?'
params = (3,)

cursor.execute(sql,params)
cnx.commit()

# CRUD: Create - Read - Update - Delete