import tkinter as tk
from tkinter import ttk,Toplevel
from Clases.Cuenta import Cuenta
from Clases.Funcion import Funcion
from Clases.Ticket import Ticket
from SQL import databases as db

class FormReserva(Toplevel):
    def __init__(self, master = None, cuenta_usuario = None, pelicula = None, base_datos = None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('500x550')
        self.config(bg = '#056595')
        self.title('Realiza tu Reserva')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.protocol('WM_DELETE_WINDOW', self.Cancelar)
        #self.resizable(0,0)

        self.bdd = base_datos
        self.cuenta = cuenta_usuario
        self.pelicula = pelicula
        #self.funcion = Funcion()
        #self.ticket = Ticket()
        
        """FRAMES"""
        self.F_cab = tk.Frame(self)     #Cabecera
        self.F_datos = tk.Frame(self)   #Datos de la Reserva
        self.F_boton = tk.Frame(self)   #Botones
        
        """WIDGETS"""
        #Titulo
        self.Cab_principal = ttk.Label(self.F_cab)
        #Comprador
        self.Compr_label = ttk.Label(self.F_datos)
        self.Compr_input = ttk.Entry(self.F_datos)
        #Pelicula
        self.Peli_label = ttk.Label(self.F_datos)
        self.Peli_input = ttk.Entry(self.F_datos)
        #Funcion
        self.Func_label = ttk.Label(self.F_datos)
        self.Func_input = ttk.Combobox(self.F_datos)
        #Butacas Seleccionadas
        self.Butac_label = ttk.Label(self.F_datos)
        self.Butac_input = ttk.Combobox(self.F_datos)
        #Precio
        self.Precio_label = ttk.Label(self.F_datos)
        self.Precio_entry = ttk.Entry(self.F_datos)
        #Botones
        self.Reservar_bott = ttk.Button(self.F_boton)
        self.Cancelar_bott = ttk.Button(self.F_boton)

        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()

    def frames_config(self):
        self.F_cab.config(border = 15, bg = '#002B40')
        self.F_datos.config(bg = '#056595')
        self.F_boton.config(bg = '#056595')
    
    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, rowspan = 2, columnspan = 3)
        self.F_datos.grid(row = 2, column = 0, rowspan = 5, columnspan = 3, pady = 20)
        self.F_boton.grid(row = 7, column = 0, columnspan = 3)

    def input_insert(self):
        self.Compr_input.insert(0, self.cuenta.dni)
        self.Peli_input.insert(0, '')
        self.Precio_entry.insert(0, '$0.00')

    def widgets_config(self):
        self.input_insert()
        #Titulo
        self.Cab_principal.config(text = 'Completá los datos y reservá\ntu entrada', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40', justify = 'center')
        #Comprador
        self.Compr_label.config(text = 'Comprador', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Compr_input.config(width = 30, state = 'readonly')
        #Pelicula
        self.Peli_label.config(text = 'Pelicula', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Peli_input.config(width = 30, state = 'readonly')
        #Funcion
        self.Func_label.config(text = 'Función', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Func_input.config(width = 27, state = 'readonly')
        #Butacas Seleccionadas
        self.Butac_label.config(text = 'Cantidad de Butacas', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Butac_input.config(width = 27, state = 'readonly')
        #Precio
        self.Precio_label.config(text = 'Precio', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Precio_entry.config(width = 30, state = 'readonly')
        #Botones
        self.Reservar_bott.config(text = 'Reservar', command = self.Reservar)
        self.Cancelar_bott.config(text = 'Cancelar', command = self.Cancelar)
    
    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0, ipady = 10)
        #Comprador
        self.Compr_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.Compr_input.grid(row = 0, column = 1, padx = 10, pady = 10)
        #Pelicula
        self.Peli_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.Peli_input.grid(row = 1, column = 1, padx = 10, pady = 10)
        #Funcion
        self.Func_label.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.Func_input.grid(row = 2, column = 1, padx = 10, pady = 10)
        #Butacas Seleccionadas
        self.Butac_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.Butac_input.grid(row = 3, column = 1, padx = 10, pady = 10)
        #Precio
        self.Precio_label.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.Precio_entry.grid(row = 4, column = 1, padx = 10, pady = 10)
        #Botones
        self.Reservar_bott.grid(row = 0, column = 0, padx = 20, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 0, column = 2, padx = 20, pady = 10, ipadx = 5, ipady = 5)

    def Reservar(self):
        pass

    def Cancelar(self):
        self.destroy()
        self.master.deiconify()