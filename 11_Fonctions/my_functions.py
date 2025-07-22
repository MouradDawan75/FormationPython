def menu():

        choix = input("""
1- Convertir heures en minutes
2- Convertir minutes en heures
3- Quitter
""")
        return choix

def convertir_heures_en_minutes(message):

    heures = saisie_nombre_valide(message)
    print(f'{heures}h = {heures * 60}m')



def convertir_minutes_en_heures(message):
    minutes = saisie_nombre_valide(message)
    print(f'{minutes}m = {minutes // 60}h {minutes % 60}m')

def choix1():
      convertir_heures_en_minutes('Heures: ')


def choix2():
    convertir_minutes_en_heures('Minutes: ')


def saisie_nombre_valide(message):
       while True:
              nb = input(message)
              if nb.isdigit():
                     return nb
              else:
                     print('nombre invalide.....')
                
      