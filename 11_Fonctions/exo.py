

      
     

while True:
    choix = input("""
1- Convertir heures en minutes
2- Convertir minutes en heures
3- Quitter
""")
    
    if choix == '1':
        heures = input('Heures: ')
        if heures.isdigit():
            heures = int(heures)
            print(f'{heures}h = {heures * 60}m')
        else:
             print('nombre invalide....')

    if choix == '2':
        minutes = input('Minutes: ')
        if minutes.isdigit():
            minutes = int(minutes)
            print(f'{minutes}m = {minutes // 60}h {minutes % 60}m')

        else:
             print('nombre invalide....')

    if choix == '3':
        break

# Optimisation du code:

from my_functions import menu,choix1,choix2

while True:
      choix = menu()

      if choix == '1':
            choix1()

      if choix == '2':
          choix2()

      if choix == '3':
            break
            