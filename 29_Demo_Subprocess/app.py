import subprocess

print(">>>>> Exécution d'une commande")

p = subprocess.run(['ipconfig'], capture_output=True, text=True)
print(p.stderr)
print(p.stdout)

print(">>>>> Exécution d'un script dans un fichier python")

result = subprocess.run(['python','29_Demo_Subprocess/my_python_file.py'], capture_output=True, text=True)

print(result.stdout)

print(">>>>> Utilisation subprocess.popen()")
# run() fonction qui exécute une comande et capture la sortie en un seul appel (utilise le main thread)

# popen() permet de démarrer un nouveau processus dans un nouveau thread
#  et d'interagir avec ses flux d'entrée de sortie et d'erreurs.

process = subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

output,erreurs = process.communicate() # renvoie un tuple

process.wait()

print(output)
print('>>>>> erreurs:')
print(erreurs)

print(">>>>>>> Exécuter un programme")

#subprocess.run(['notepad'])

print('suite du script................')

print(">>>>>>> Exécution  d'un script python avec passage de paramètres")

subprocess.run(['python','29_Demo_Subprocess/log_file_find.py','app.log','resultat.txt','warning'])

