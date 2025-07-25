
# pip install peewee
from peewee import *

# ORM: Object Relational Mapping

db = SqliteDatabase('32_Peewee_ORM_Demo/my_db.db')

class Product(Model):
    name = CharField()
    price = FloatField()

    class Meta:
        database = db
        table_name = 'produit' # personnaliser le nom de la table

db.connect()

db.create_tables([Product]) # par défaut, un id en autoincrément est généré dans la table

print('>>>>>>> Insertion de données:')

# Option1:
# p1 = Product(name='PC Dell', price=1500)
# p1.save()

# # Option2:
# p2 = Product.create(name='Ecran HP', price='99')

print('>>>>>> Lecture des données:')

print(len(Product.select()))

for p in Product.select():
    print(p.name)


print(Product.select().where(Product.id==2)) # commande sql générée

result = Product.select().where(Product.id==2)
print(result[0].name) # select renvoie une liste
print(result.get().name)

print(Product.get(Product.id == 2).name)

prod = Product.get_or_none(1)
if prod:
    print(prod.name)
else:
    print('prod introuvable..........')

#prod.delete_instance()

# Doc: https://docs.peewee-orm.com/en/latest/peewee/quickstart.html


