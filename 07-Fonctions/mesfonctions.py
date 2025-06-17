def convertir_heures_en_minutes(heures):
    print(f'{heures}h = {heures * 60}m')

def convertir_minutes_en_heures(minutes):
    print(f'{minutes}m = {minutes // 60}h {minutes % 60}m')

def choix1():
    heures = int(input('Heures à convertir: '))
    convertir_heures_en_minutes(heures)

def choix2():
    minutes = int(input('Minutes à convertir: '))
    convertir_minutes_en_heures(minutes)