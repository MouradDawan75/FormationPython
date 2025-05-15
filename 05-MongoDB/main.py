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

# resultat = employe_collection.insert_one(player)

# print(resultat.inserted_id)
# print(resultat.acknowledged)

print('Databases:', client.list_database_names())

print('Liste collections:', db.list_collection_names())

print('Nombre de documents:', employe_collection.count_documents({}))

print(">>>> filtre:")

pointeur = employe_collection.find()

for d in pointeur:
    print(d)

# cursuer: pointeur
curseur = employe_collection.find({"nom": "FEDERER"}, {"nom":1,"prenom":1, "_id":0})
print(curseur)
print(curseur.to_list())

