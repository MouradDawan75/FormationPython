# pip install object-mapper

from dataclasses import dataclass
from typing import Optional


# Entity (Model): objets persistés en base de données

@dataclass
class UserEntity:

    first_name:  Optional[str] = None 
    last_name:Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


# DTO: Data Transfert Object - Objets métier

@dataclass
class UserDTO:

    name: Optional[str] = None
    emailId: Optional[str] = None


from mapper.object_mapper import ObjectMapper

# Définir le mapping:

mapping = {
    'name': lambda entity: entity.first_name,
    'emailId': lambda entity: entity.email
}

mapper = ObjectMapper()

mapper.create_map(UserEntity, UserDTO, mapping)

entity = UserEntity('Jean', 'DUPONT', 'j.dupont@gmail.com', '@@pwd@@')
dto = mapper.map(entity, UserDTO)

print(dto)
