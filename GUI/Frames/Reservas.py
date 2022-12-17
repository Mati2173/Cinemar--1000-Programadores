import tkinter as tk
from tkinter import ttk

class ReservaCli(tk.Frame):
    def __init__(self, master = None, cuenta_usuario = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master

        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos

        """WIDGETS"""
        #Titulo
        self.Cab_principal = ttk.Label(self)
        #Tabla
        self.Tabla = ttk.Treeview(self)
        #Busqueda
        self.Busq_label = ttk.Label(self)
        self.Busq_input = ttk.Entry(self)
        self.Buscar_bott = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()
    
    def widgets_config(self):
        #Titulo
        self.Cab_principal.config(text = '    Historial de Reservas    ', foreground = '#FFFFFF', font = ('Segoe UI Black', 36), background = '#002B40', justify = 'center')
        #Tabla
        self.Tabla_config()
        #Busqueda
        self.Busq_label.config(text = 'Buscar reserva por nombre de pelicula', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Busq_input.config(width = 40)
        self.Buscar_bott.config(text = 'Buscar', command = self.Buscar_peli)

    def Tabla_config(self):
        self.Tabla.config(columns = (1,2,3,4))
        self.Tabla.column('#0', width = 160, anchor = 'center')
        self.Tabla.heading('#0', text = 'Pelicula')
        self.Tabla.column('#1', width = 120, anchor = 'center')
        self.Tabla.heading('#1', text = 'Butacas Reservadas')
        self.Tabla.column('#2', width = 90, anchor = 'center')
        self.Tabla.heading('#2', text = 'Fecha')
        self.Tabla.column('#3', width = 70, anchor = 'center')
        self.Tabla.heading('#3', text = 'Horario')
        self.Tabla.column('#4', width = 70, anchor = 'center')
        self.Tabla.heading('#4', text = 'Precio')

    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0, column = 0, columnspan = 4, pady  = 20, ipady = 10)
        #Tabla
        self.Tabla.grid(row = 1, column = 0, rowspan = 4, columnspan = 4, padx = 20, pady = (0, 20))
        #Busqueda
        self.Busq_label.grid(row = 5, column = 0, columnspan = 4)
        self.Busq_input.grid(row = 6, column = 0, columnspan = 4, pady = 20)
        self.Buscar_bott.grid(row = 7, column = 0, columnspan = 4, ipadx = 5, ipady = 5)

    def Buscar_peli(self):
        pass


class ReservaAdm(tk.Frame):
    def __init__(self, master = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.bdd = base_datos

        """WIDGETS"""
        self.Cab_principal = ttk.Label(self)
        self.Tabla = ttk.Treeview(self)
        self.Busq_label = ttk.Label(self)
        self.Busq_input = ttk.Entry(self)
        self.Buscar_bott = ttk.Button(self)
        
        self.widgets_config()
        self.widgets_grid()

    def widgets_config(self):
        self.Cab_principal.config(text = '    Historial Reservas    ', foreground = '#FFFFFF', font = ('Segoe UI Black', 36), background = '#002B40')
        self.Tabla_config()
        self.Busq_label.config(text = 'Buscar reserva por DNI', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Busq_input.config(width = 15)
        self.Buscar_bott.config(text = 'Buscar', command = self.Buscar_tickets)

    def widgets_grid(self):
        self.Cab_principal.grid(row = 0, column = 0, columnspan = 8, pady = 20, ipady = 10)
        self.Tabla.grid(row = 1, column = 0, rowspan = 4, columnspan = 8, pady = (0, 20))
        self.Busq_label.grid(row = 5, column = 1, columnspan = 4)
        self.Busq_input.grid(row = 5, column = 5)
        self.Buscar_bott.grid(row = 5, column = 6)

    def Tabla_config(self):
        self.Tabla.config(columns = (1,2,3,4,5,6))
        self.Tabla.column('#0', width = 70, anchor = 'center')
        self.Tabla.heading('#0', text = 'ID Ticket')
        self.Tabla.column('#1', width = 160, anchor = 'center')
        self.Tabla.heading('#1', text = 'Comprador')
        self.Tabla.column('#2', width = 160, anchor = 'center')
        self.Tabla.heading('#2', text = 'Pelicula')
        self.Tabla.column('#3', width = 120, anchor = 'center')
        self.Tabla.heading('#3', text = 'Butacas Reservadas')
        self.Tabla.column('#4', width = 90, anchor = 'center')
        self.Tabla.heading('#4', text = 'Fecha')
        self.Tabla.column('#5', width = 70, anchor = 'center')
        self.Tabla.heading('#5', text = 'Horario')
        self.Tabla.column('#6', width = 70, anchor = 'center')
        self.Tabla.heading('#6', text = 'Precio')
    
    def Buscar_tickets(self):
        pass
