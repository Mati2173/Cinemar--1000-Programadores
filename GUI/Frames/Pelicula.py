import tkinter as tk
from tkinter import ttk
from Clases.Cuenta import Cuenta
from GUI.Formularios.Reserva import FormReserva

class PeliculaCli(tk.Frame):
    def __init__(self, ventana_padre = None, master = None, cuenta_usuario = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.ventana_padre = ventana_padre
        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos

        """WIDGETS"""
        #Titulo
        self.Cab_principal = ttk.Label(self)
        #Tabla
        self.Tabla = ttk.Treeview(self)
        #Detalles
        self.Info_label = ttk.Label(self)
        self.Info_input =  ttk.Combobox(self)
        self.Info_bott = ttk.Button(self)
        #Reservar
        self.Reser_label = ttk.Label(self)
        self.Reser_input =  ttk.Combobox(self)
        self.Aceptar_bott = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()



    def Tabla_config(self):
        self.Tabla.config(columns = (1,2,3,4))
        self.Tabla.column('#0', width = 70, anchor = 'center')
        self.Tabla.heading('#0', text = 'ID Pelicula')
        self.Tabla.column('#1', width = 160, anchor = 'center')
        self.Tabla.heading('#1', text = 'Nombre')
        self.Tabla.column('#2', width = 70, anchor = 'center')
        self.Tabla.heading('#2', text = 'Duracion')
        self.Tabla.column('#3', width = 70, anchor = 'center')
        self.Tabla.heading('#3', text = 'Genero')
        self.Tabla.column('#4', width = 70, anchor = 'center')
        self.Tabla.heading('#4', text = 'Tipo')

    def widgets_config(self):
        #Titulo
        self.Cab_principal.config(text = '         Peliculas Disponibles         ', foreground = '#FFFFFF', font = ('Segoe UI Black', 36), background = '#002B40')
        #Tabla
        self.Tabla_config()
        #Detalles
        self.Info_label.config(text = 'Selecciona una pelicula\npara ver mas detalles', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595', justify = 'center')
        self.Info_input.config(width = 5)
        self.Info_bott.config(text = 'MÁS INFO', command = self.Detalles)
        #Reservar
        self.Reser_label.config(text = 'Selecciona una pelicula\npara reservar', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595', justify = 'center')
        self.Reser_input.config(width = 10)
        self.Aceptar_bott.config(text = 'Aceptar', command = self.Reservar)

    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0, column = 0, columnspan = 8, pady = 20, ipady = 10)
        #Tabla
        self.Tabla.grid(row = 1, column = 0, rowspan = 5, columnspan = 5, padx = 20, pady = (0, 20))
        #Detalles
        self.Info_label.grid(row = 2, column = 5, rowspan = 2, columnspan = 8)
        self.Info_input.grid(row = 4, column = 5, columnspan = 2, pady = 20)
        self.Info_bott.grid(row = 4, column = 7, columnspan = 1, ipadx = 5, ipady = 5)
        #Reservar
        self.Reser_label.grid(row = 6, column = 1, rowspan = 2, columnspan = 3)
        self.Reser_input.grid(row = 7, column = 4, columnspan = 2)
        self.Aceptar_bott.grid(row = 7, column = 6, columnspan = 1, ipadx = 5, ipady = 5)

    def Reservar(self):
        self.ventana_padre.withdraw()
        ventana = FormReserva(self.ventana_padre, self.cuenta_usuario, None, self.bdd)
        ventana.mainloop()
    
    def Detalles(self):
        pass

class PeliculaAdm(tk.Frame):
    def __init__(self, ventana_padre = None, master = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.ventana_padre = ventana_padre
        self.bdd = base_datos

        """WIDGETS"""
        #Titulo
        self.cab_principal = ttk.Label(self)
        #Tabla
        self.Tabla = ttk.Treeview(self)
        #Detalles
        self.Info_label = ttk.Label(self)
        self.Info_input =  ttk.Combobox(self)
        self.Info_bott = ttk.Button(self)
        #Añadir
        self.Add_label = ttk.Label(self)
        self.Add_bott = ttk.Button(self)
        #Eliminar
        self.Elim_label = ttk.Label(self)
        self.Elim_input = ttk.Combobox(self)
        self.Elim_bott = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()


    
    def Tabla_config(self):
        self.Tabla.config(columns = (1,2,3,4))
        self.Tabla.column('#0', width = 70, anchor = 'center')
        self.Tabla.heading('#0', text = 'ID Pelicula')
        self.Tabla.column('#1', width = 160, anchor = 'center')
        self.Tabla.heading('#1', text = 'Nombre')
        self.Tabla.column('#2', width = 70, anchor = 'center')
        self.Tabla.heading('#2', text = 'Duracion')
        self.Tabla.column('#3', width = 70, anchor = 'center')
        self.Tabla.heading('#3', text = 'Genero')
        self.Tabla.column('#4', width = 70, anchor = 'center')
        self.Tabla.heading('#4', text = 'Tipo')

    def widgets_config(self):
        #Titulo
        self.cab_principal.config(text = '          Peliculas Disponibles          ', foreground = '#FFFFFF', font = ('Segoe UI Black', 36), background = '#002B40', justify = 'center')
        #Tabla
        self.Tabla_config()
        #Detalles
        self.Info_label.config(text = 'Selecciona una pelicula\npara ver mas detalles', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595', justify = 'center')
        self.Info_input.config(width = 5)
        self.Info_bott.config(text = 'MAS INFO', command = self.Detalles)
        #Añadir
        self.Add_label.config(text = 'Agregar pelicula', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Add_bott.config(text = 'Agregar')
        #Eliminar
        self.Elim_label.config(text = 'Eliminar pelicula', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Elim_input.config(width = 5)
        self.Elim_bott.config(text = 'Eliminar', command = self.Eliminar)

    def widgets_grid(self):
        #Titulo
        self.cab_principal.grid(row = 0, column = 0, columnspan = 8, pady = 20, ipady = 10)
        #Tabla
        self.Tabla.grid(row = 1, column = 0, rowspan = 5, columnspan = 5, padx = 20, pady = (0, 20))
        #Detalles
        self.Info_label.grid(row = 2, column = 5, rowspan = 2, columnspan = 3)
        self.Info_input.grid(row = 4, column = 5, columnspan = 2)
        self.Info_bott.grid(row = 4, column = 7, columnspan = 1)
        #Añadir
        self.Add_label.grid(row = 6, column = 2)
        self.Add_bott.grid(row = 7, column = 2, columnspan = 1, pady = 10)
        #Eliminar
        self.Elim_label.grid(row = 6, column = 4, columnspan = 2)
        self.Elim_input.grid(row = 7, column = 4)
        self.Elim_bott.grid(row = 7, column = 5, columnspan = 1, pady = 10)

    def Detalles(self):
        pass

    def Eliminar(self):
        pass