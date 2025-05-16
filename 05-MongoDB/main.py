# pip install pymongo

from pymongo import MongoClient

# connexion à mongodb

client = MongoClient('localhost',27017)

print('Databases:', client.list_database_names())

# choisir une base de données

db = client.initiation # si la base n'existe pas, elle est créée
# db = client['initiation'] -> autre syntaxe

# choisir une collection:

employe_collection = db.employes # si collection inexistante -> elle est créée

print('Databases:', client.list_database_names())

print(">>>>>>>>> Ajouts:")

player = {
    "nom": "FEDERER",
    "prenom": "Roger",
    "age": 39
}

########### insert_one()
# resultat = employe_collection.insert_one(player)

# print(resultat.inserted_id)
# print(resultat.acknowledged

players = [
     {
    "nom": "NADAL",
    "prenom": "Rafael",
    "age": 37
},
{
    "nom": "DJOKOVIC",
    "prenom": "Novak",
    "age": 36
}
]


########### insert_many()
# resultas = employe_collection.insert_many(players)
# print(resultas.inserted_ids)
# print(resultas.acknowledged)

print('Databases:', client.list_database_names())

print('Liste collections:', db.list_collection_names())

print('Nombre de documents:', employe_collection.count_documents({}))

print(">>>> filtre:")

curseur = employe_collection.find()

for d in curseur:
    print(d)

# curseur: sorte de pointeur vers les documents de la collection
curseur = employe_collection.find({"nom": "FEDERER"}, {"nom":1,"prenom":1, "_id":0})
print(curseur)
print(curseur.to_list())

one = employe_collection.find_one({"nom":"NADAL"})

print(one)

print(">>>>> update:")

filtre = {"nom": "FEDERER"}
new_values = {"$set": {"nom": "new_federer"}}

result = employe_collection.update_one(filtre,new_values)

print(result.modified_count)

#doc: https://www.w3schools.com/python/python_mongodb_delete.asp

print(">>>>>>>> delete:")

filtre = {"nom":"DJOKOVIC"}

result = employe_collection.delete_one(filtre)

print(result.deleted_count)

# BSON: est l'acronyme de Binary JSON.
# MongoDB utilise le format BSON pour le stockage physique des données

from bson import BSON

d = {
    'a':1,
    'b':2
}

resultat = BSON.encode(d)

print(resultat)

decoded = BSON(resultat).decode()

print(decoded)


# Génération d'un BSON à partir d'une collection

lst = []

for e in employe_collection.find():
    print('Encoded:', BSON.encode(e))
    #lst.append(BSON.encode(e))

    # wb: write byte
    # ab: append byte
    with open('05-MongoDB/employes.bson', 'ab') as flux:
        flux.write(BSON.encode(e))


# Lecture d'un fichier bson: génération d'un json à partir d'un bson

from bson import decode_all
from bson.json_util import dumps

with open('05-MongoDB/employes.bson', 'rb') as flux:
    data = decode_all(flux.read())


print(data)

with open('05-MongoDB/resultat.json', 'w') as flux:
    flux.write(dumps(data, indent=2))