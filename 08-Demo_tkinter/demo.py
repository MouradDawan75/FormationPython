# tkinter: Tool Kit INTERface

import tkinter

# créer une fen^tre
fenetre = tkinter.Tk()

def open_window():
    new_window = tkinter.Toplevel(fenetre) # s'affiche au dessus de la fen^tre principale
    new_window.title('New Window')
    new_window.geometry('200x100')

    tkinter.Label(new_window,text='Text de new window').pack()

fenetre.title('Fenêtre principale')
fenetre.geometry('400x600')
tkinter.Label(fenetre, text='Fenêtre principale').pack() # ajouter un lebl à la fenêtre
tkinter.Button(fenetre, text='Open new window', command=open_window).pack() # ajouter un bouton
tkinter.Button(fenetre,text='Quit', command=fenetre.destroy).pack()


# afficher a fenêtre

fenetre.mainloop()

# lien doc: https://python.doctor/page-tkinter-interface-graphique-python-tutoriel