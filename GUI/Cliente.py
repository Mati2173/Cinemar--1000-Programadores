import tkinter as tk
from tkinter import ttk

class Cliente(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('1080x720')
        self.config(bg = '#056595')
        self.title('Sistema de Autogestión - Cinemar')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')

        self.img_Inicio = tk.PhotoImage(file = "GUI\Assets\Home.png")
        self.img_Perfil = tk.PhotoImage(file = "GUI\Assets\Customer.png")
        self.img_Pelicula = tk.PhotoImage(file = "GUI\Assets\Pelicula.png")
        self.img_Reservas = tk.PhotoImage(file = "GUI\Assets\Ticket.png")
        self.img_Logout = tk.PhotoImage(file = 'GUI\Assets\Logout.png')
        self.resizable(0,0)

        self.widgets()
    
    def widgets(self):
        self.menu_opciones()

    def menu_opciones(self):
        botInicio = ttk.Button(self, image = self.img_Inicio, command = self.menu_inicio)
        botPerfil = ttk.Button(self, image = self.img_Perfil, command = self.mostrar_perfil)
        botPeliculas = ttk.Button(self, image = self.img_Pelicula, command = self.list_peliculas)
        botReservas = ttk.Button(self, image = self.img_Reservas, command = self.list_reservas)
        botLogout = ttk.Button(self, image = self.img_Logout, command = self.logout)

        botInicio.grid(row = 0, column = 1, ipadx = 15, ipady = 5)
        botPerfil.grid(row = 0, column = 2, ipadx = 80, ipady = 5)
        botPeliculas.grid(row = 0, column = 3, ipadx = 80, ipady = 5)
        botReservas.grid(row = 0, column = 4, ipadx = 80, ipady = 5)
        botLogout.grid(row = 0, column = 5, ipadx = 80, ipady = 5)

    def menu_inicio(self):
        pass

    def mostrar_perfil(self):
        pass

    def list_peliculas(self):
        pass

    def list_reservas(self):
        pass

    def logout(self):
        self.destroy()

a = Cliente()
a.mainloop()