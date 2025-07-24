# installer le connecter pip install conneter_selon_type_base_données

import sqlite3

cnx = sqlite3.connect('31_Database/db.sqlite3')
cursor = cnx.cursor()

# Commandes sql LDD: Langage de définition de données (commande pour la structure de la BD): create, drop,alter
# Commandes sql LMD: Langage de manipulation de données: select,delete,insert,update


cursor.execute("""
create table if not exists personne(
 id integer primary key autoincrement not null,
 nom varchar(30) not null,              
 prenom varchar(30) not null, 
 age int unsigned not null,
 constraint unique_names unique (nom,prenom)                
               
)
""")

# Insérer des données de tests: En Python les opérations d'écriture s'exécutent en mode transactionnel

try:

    # Mauvaise pratique: ne jamais définir des fcts prenant en paramètres des commandes sql
    cursor.execute("insert into personne(nom,prenom,age) values('DUPONT', 'Jean', 65)")

    # Injection sql: utilisez des commandes paramètrées. Se sont des commandes précompiées, chargées 
    # en mémoire en attente de params
    cursor.execute('insert into personne values (null,?,?,?)', ('FEDERER', 'Roger', 39))
    cursor.execute('insert into personne values (null,?,?,?)', ('NADAL', 'Rafael', 37))

    cnx.commit() # commit: valide toutes les commandes sql

except Exception as e:
    print(e)
    cnx.rollback()

finally:
    cursor.close()
    cnx.close()


# Pour sqlite:
# installer un client externe sqlitebrowser
# dans vs code, extension sqlite viewer