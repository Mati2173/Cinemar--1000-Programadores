import tkinter as tk
from tkinter import ttk
from Clases.Ticket import Ticket

class ReservaCli(tk.Frame):
    def __init__(self, master = None, cuenta_usuario = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master

        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos
        self.ticket = Ticket()

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
        self.fill_Tickets()
    

    
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
        self.Tabla.column('#0', width = 180, anchor = 'center')
        self.Tabla.heading('#0', text = 'Pelicula', anchor = 'center')
        self.Tabla.column('#1', width = 160, anchor = 'center')
        self.Tabla.heading('#1', text = 'Butacas Reservadas', anchor = 'center')
        self.Tabla.column('#2', width = 90, anchor = 'center')
        self.Tabla.heading('#2', text = 'Fecha', anchor = 'center')
        self.Tabla.column('#3', width = 70, anchor = 'center')
        self.Tabla.heading('#3', text = 'Horario', anchor = 'center')
        self.Tabla.column('#4', width = 70, anchor = 'center')
        self.Tabla.heading('#4', text = 'Precio', anchor = 'center')

    def fill_Tickets(self, peli = None):
        self.Tabla.delete(*self.Tabla.get_children())
        reservas = self.ticket.por_comprador(self.bdd, self.cuenta_usuario.dni)
        if peli == None:
            for res in reservas:
                self.Tabla.insert('', 'end', text = f'{res[2]}', values = (res[3], res[4], res[5], res[6]))
        else:
            for res in reservas:
                if res[2] == peli:
                    self.Tabla.insert('', 'end', text = f'{res[2]}', values = (res[3], res[4], res[5], res[6]))

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
        peli = self.Busq_input.get()
        if len(peli) == 0:
            self.fill_Tickets()
        else:
            self.fill_Tickets(peli)



class ReservaAdm(tk.Frame):
    def __init__(self, master = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.bdd = base_datos
        self.ticket = Ticket()

        """WIDGETS"""
        self.Cab_principal = ttk.Label(self)
        self.Tabla = ttk.Treeview(self)
        self.Busq_label = ttk.Label(self)
        self.Busq_input = ttk.Entry(self)
        self.Buscar_bott = ttk.Button(self)
        
        self.widgets_config()
        self.widgets_grid()
        self.fill_Tickets()



    def Tabla_config(self):
        self.Tabla.config(columns = (1,2,3,4,5,6))
        self.Tabla.column('#0', width = 70, anchor = 'center')
        self.Tabla.heading('#0', text = 'ID Ticket', anchor = 'center')
        self.Tabla.column('#1', width = 120, anchor = 'center')
        self.Tabla.heading('#1', text = 'Comprador', anchor = 'center')
        self.Tabla.column('#2', width = 180, anchor = 'center')
        self.Tabla.heading('#2', text = 'Pelicula', anchor = 'center')
        self.Tabla.column('#3', width = 160, anchor = 'center')
        self.Tabla.heading('#3', text = 'Butacas Reservadas', anchor = 'center')
        self.Tabla.column('#4', width = 90, anchor = 'center')
        self.Tabla.heading('#4', text = 'Fecha', anchor = 'center')
        self.Tabla.column('#5', width = 70, anchor = 'center')
        self.Tabla.heading('#5', text = 'Horario', anchor = 'center')
        self.Tabla.column('#6', width = 70, anchor = 'center')
        self.Tabla.heading('#6', text = 'Precio', anchor = 'center')

    def widgets_config(self):
        self.Cab_principal.config(text = '    Historial Reservas    ', foreground = '#FFFFFF', font = ('Segoe UI Black', 36), background = '#002B40')
        self.Tabla_config()
        self.Busq_label.config(text = 'Buscar reserva por DNI', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Busq_input.config(width = 15)
        self.Buscar_bott.config(text = 'Buscar', command = self.Buscar_tickets)

    def fill_Tickets(self):
        self.Tabla.delete(*self.Tabla.get_children())
        reservas = self.ticket.all_tickets(self.bdd)

        for res in reservas:
            self.Tabla.insert('', 'end', text = f'{res[0]}', values = (res[1], res[2], res[3], res[4], res[5], res[6]))
    
    def fill_Tickets_compr(self, dni):
        self.Tabla.delete(*self.Tabla.get_children())
        reservas = self.ticket.por_comprador(self.bdd, dni)

        for res in reservas:
            self.Tabla.insert('', 'end', text = f'{res[0]}', values = (res[1], res[2], res[3], res[4], res[5], res[6]))

    def widgets_grid(self):
        self.Cab_principal.grid(row = 0, column = 0, columnspan = 8, pady = 20, ipady = 10)
        self.Tabla.grid(row = 1, column = 0, rowspan = 4, columnspan = 8, pady = (0, 20))
        self.Busq_label.grid(row = 5, column = 1, columnspan = 4)
        self.Busq_input.grid(row = 5, column = 5)
        self.Buscar_bott.grid(row = 5, column = 6)

    def Buscar_tickets(self):
        dni = self.Busq_input.get()
        if len(dni) == 0:
            self.fill_Tickets()
        else:
            self.fill_Tickets_compr(dni)
