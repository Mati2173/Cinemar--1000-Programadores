import tkinter as tk
from tkinter import ttk
from SQL import databases as db

class Administrador(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('1080x720')
        self.config(bg = '#056595')
        self.title('Sistema de Autogestión - Cinemar')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.bdd = db.DataBase('cinemar.db')

        self.img_Inicio = tk.PhotoImage(file = "GUI\Assets\Home.png")
        self.img_Perfil = tk.PhotoImage(file = "GUI\Assets\Customer.png")
        self.img_Sala = tk.PhotoImage(file = "GUI\Assets\Sala.png")
        self.img_Pelicula = tk.PhotoImage(file = "GUI\Assets\Pelicula.png")
        self.img_Funciones = tk.PhotoImage(file = "GUI\Assets\Funcion.png")
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
        botSalas = ttk.Button(self, image = self.img_Sala, command = self.list_salas)
        botFunciones = ttk.Button(self, image = self.img_Funciones, command = self.list_funciones)
        botReservas = ttk.Button(self, image = self.img_Reservas, command = self.list_reservas)
        botLogout = ttk.Button(self, image = self.img_Logout, command = self.logout)

        botInicio.grid(row = 0, column = 1, ipadx = 13, ipady = 5)
        botPerfil.grid(row = 0, column = 2, ipadx = 40, ipady = 5)
        botPeliculas.grid(row = 0, column = 3, ipadx = 40, ipady = 5)
        botSalas.grid(row = 0, column = 4, ipadx = 40, ipady = 5)
        botFunciones.grid(row = 0, column = 5, ipadx = 40, ipady = 5)
        botReservas.grid(row = 0, column = 6, ipadx = 40, ipady = 5)
        botLogout.grid(row = 0, column = 7, ipadx = 40, ipady = 5)

    def menu_inicio(self):
        pass

    def mostrar_perfil(self):
        pass

    def list_peliculas(self):
        frameTabla = tk.Frame(self, background = '#00FF00')
        frameTabla.grid(row = 1, column = 0, columnspan = 4)
        
        tabla = ttk.Treeview(frameTabla, columns = (1))
        tabla.column('#0', width = 90, anchor = 'center')
        tabla.column('#1', width = 220, anchor = 'center')
        tabla.heading('#0', text = 'ID_Pelicula')
        tabla.heading('#1', text = 'Nombre')
        tabla.grid(row = 1, column = 0, columnspan = 4, pady = 20, padx = 20)

        frameForm = tk.Frame(self, background = '#0000FF')
        frameForm.grid(row = 1, column = 4, columnspan = 2)
        
        cant = 10 + self.bdd.count('peliculas', 'id_pelicula', 'id_pelicula != 0')
        valores = []
        for i in range(cant):
            valores.append(i+1)
        
        select_pel = ttk.Label(frameForm, text = 'Seleccione una pelicula')
        select_pel.grid(row = 1, column = 4, pady = 10)
        box = ttk.Combobox(frameForm, values = valores)
        box.grid(row = 2, column = 4, pady = 10)

    def list_salas(self):
        tabla = ttk.Treeview(self, columns = (1,2,3))
        tabla.column('#0', width = 70, anchor = 'center')
        tabla.column('#1', width = 160, anchor = 'center')
        tabla.column('#2', width = 70, anchor = 'center')
        tabla.column('#3', width = 90, anchor = 'center')


        tabla.heading('#0', text = 'ID_Sala')
        tabla.heading('#1', text = 'Cantidad de Butacas')
        tabla.heading('#2', text = 'Tipo')
        tabla.heading('#3', text = 'ID_Funcion')

        tabla.grid(row = 1, column = 0, columnspan = 4, pady = 20, padx = 20)

    def list_funciones(self):
        tabla = ttk.Treeview(self, columns = (1,2,3,4,5))
        tabla.column('#0', width = 90, anchor = 'center')
        tabla.column('#1', width = 160, anchor = 'center')
        tabla.column('#2', width = 120, anchor = 'center')
        tabla.column('#3', width = 90, anchor = 'center')
        tabla.column('#4', width = 90, anchor = 'center')
        tabla.column('#5', width = 90, anchor = 'center')


        tabla.heading('#0', text = 'ID_Funcion')
        tabla.heading('#1', text = 'Pelicula')
        tabla.heading('#2', text = 'Butacas Libres')
        tabla.heading('#3', text = 'Fecha')
        tabla.heading('#4', text = 'Horario')
        tabla.heading('#5', text = 'Precio')

        tabla.grid(row = 1, column = 0, columnspan = 6, pady = 20, padx = 20)

    def list_reservas(self):
        tabla = ttk.Treeview(self, columns = (1,2,3,4,5,6))
        tabla.column('#0', width = 70, anchor = 'center')
        tabla.column('#1', width = 160, anchor = 'center')
        tabla.column('#2', width = 160, anchor = 'center')
        tabla.column('#3', width = 120, anchor = 'center')
        tabla.column('#4', width = 90, anchor = 'center')
        tabla.column('#5', width = 90, anchor = 'center')
        tabla.column('#6', width = 90, anchor = 'center')


        tabla.heading('#0', text = 'ID_Ticket')
        tabla.heading('#1', text = 'Comprador')
        tabla.heading('#2', text = 'Pelicula')
        tabla.heading('#3', text = 'Cantidad de Butacas')
        tabla.heading('#4', text = 'Fecha')
        tabla.heading('#5', text = 'Horario')
        tabla.heading('#6', text = 'Precio')

        tabla.grid(row = 1, column = 0, columnspan = 7, pady = 20, padx = 20)

    def logout(self):
        self.destroy()

    """ PROBANDO
    def list_clientes(self):
        tabla = ttk.Treeview(self, columns = (1,2,3,4,5,6,7))
        tabla.column('#0', width = 70, anchor = 'center')
        tabla.column('#1', width = 160, anchor = 'center')
        tabla.column('#2', width = 160, anchor = 'center')
        tabla.column('#3', width = 90, anchor = 'center')
        tabla.column('#4', width = 220, anchor = 'center')
        tabla.column('#5', width = 90, anchor = 'center')
        tabla.column('#6', width = 120, anchor = 'center')
        tabla.column('#7', width = 120, anchor = 'center')

        tabla.heading('#0', text = 'ID_Cliente')
        tabla.heading('#1', text = 'Apellido')
        tabla.heading('#2', text = 'Nombre')
        tabla.heading('#3', text = 'DNI')
        tabla.heading('#4', text = 'Email')
        tabla.heading('#5', text = 'Telefono')
        tabla.heading('#6', text = 'Usuario')
        tabla.heading('#7', text = 'Password')

        tabla.grid(row = 1, column = 1, columnspan = 6, pady = 20, padx = 20)
    """
a = Administrador()
a.mainloop()
