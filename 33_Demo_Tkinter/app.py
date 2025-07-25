import tkinter

# tkinter: Tool Kit INTERface

# créer une fenêtre



f = tkinter.Tk()

def open_window():
    new_window = tkinter.Toplevel(f)
    new_window.title('Popup')
    new_window.geometry('200x100')

    tkinter.Label(new_window,text='text new window').pack()

f.title('Fenêtre principale')
f.geometry('640x480')
tkinter.Label(f, text='main window').pack()
tkinter.Button(f, text="open window",command=open_window).pack()
tkinter.Button(f, text="Quitter",command=f.destroy).pack()

# afficher la fenêtre
f.mainloop()

# Inconvénients:
# Connaitre les classes et les fonctions
# Limité en widgets