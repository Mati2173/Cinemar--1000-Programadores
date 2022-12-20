from tkinter import messagebox
from GUI.Main import Main
from SQL import databases as db

try:
    base = db.DataBase('cinemar.db')

    a = Main(base)
    a.mainloop()

    base.close()
except:
    messagebox.showerror('Error en la aplicación', 'Algo salio mal :(')