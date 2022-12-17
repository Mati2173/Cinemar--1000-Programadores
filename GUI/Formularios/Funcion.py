import tkinter as tk
from tkinter import ttk, Toplevel
from Clases.Funcion import Funcion
from SQL import databases as db

class FormFuncion(Toplevel):
    def __init__(self, master = None, base_datos = None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('358x550')
        self.config(bg = '#056595')
        self.title('Agregar Funcion')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.protocol('WM_DELETE_WINDOW', self.Cancelar)
        #self.resizable(0,0)

        self.bdd = base_datos
        #self.funcion = Funcion()
        
        """FRAMES"""
        self.F_cab = tk.Frame(self)     #Cabecera
        self.F_datos = tk.Frame(self)   #Datos de la Funcion
        self.F_boton = tk.Frame(self)   #Botones

        """ELEMENTOS"""
        #Titulo
        self.Cab_principal = ttk.Label(self.F_cab)
        #Sala
        self.Sala_label = ttk.Label(self.F_datos)
        self.Sala_input = ttk.Combobox(self.F_datos)
        #Pelicula
        self.Peli_label = ttk.Label(self.F_datos)
        self.Peli_input = ttk.Combobox(self.F_datos)
        #Butacas Disponibles
        self.Butac_label = ttk.Label(self.F_datos)
        self.Butac_input = ttk.Entry(self.F_datos)
        #Fecha
        self.Fecha_label = ttk.Label(self.F_datos)
        self.Fecha_input = ttk.Entry(self.F_datos)
        #Horario
        self.Hora_label = ttk.Label(self.F_datos)
        self.Hora_input = ttk.Entry(self.F_datos)
        #Precio
        self.Precio_label = ttk.Label(self.F_datos)
        self.Precio_input = ttk.Entry(self.F_datos)
        #Botones
        self.Cargar_bott = ttk.Button(self.F_boton)
        self.Cancelar_bott = ttk.Button(self.F_boton)

        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()



    def frames_config(self):
        self.F_cab.config(border = 15, bg = '#002B40')
        self.F_datos.config(bg = '#056596')
        self.F_boton.config(bg = '#056596')
    
    def widgets_config(self):
        self.input_insert()
        #Titulo
        self.Cab_principal.config(text = 'Ingresá los datos de\nla nueva función', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40', justify = 'center')
        #Sala
        self.Sala_label.config(text = 'Sala', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Sala_input.config(width = 7, state = 'readonly')
        #Pelicula
        self.Peli_label.config(text = 'Pelicula', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Peli_input.config(width = 27, state = 'readonly')
        #Butacas Disponibles
        self.Butac_label.config(text = 'Butacas', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Butac_input.config(width = 10, state = 'readonly')
        #Fecha
        self.Fecha_label.config(text = 'Fecha', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Fecha_input.config(width = 30)
        #Horario
        self.Hora_label.config(text = 'Horario', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Hora_input.config(width = 30)
        #Precio
        self.Precio_label.config(text = 'Precio ($)', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Precio_input.config(width = 10)
        #Botones
        self.Cargar_bott.config(text = 'Cargar Datos', command = self.Cargar)
        self.Cancelar_bott.config(text = 'Cancelar', command = self.Cancelar)

    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, rowspan = 2, columnspan = 3)
        self.F_datos.grid(row = 2, column = 0, rowspan = 5, columnspan = 3, pady = 20)
        self.F_boton.grid(row = 7, column = 0, columnspan = 3)

    def input_insert(self):
        self.Butac_input.insert(0, '0')
        self.Precio_input.insert(0, '0')

    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0, ipady = 10)
        #Sala
        self.Sala_label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.Sala_input.grid(row = 1, column = 2, padx = 10, pady = 10)
        #Pelicula
        self.Peli_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.Peli_input.grid(row = 1, column = 0, padx = 10, pady = 10)
        #Butacas Disponibles
        self.Butac_label.grid(row = 2, column = 2, padx = 10, pady = 10)
        self.Butac_input.grid(row = 3, column = 2, padx = 10, pady = 10)
        #Fecha
        self.Fecha_label.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.Fecha_input.grid(row = 3, column = 0, padx = 10, pady = 10)
        #Horario
        self.Hora_label.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.Hora_input.grid(row = 5, column = 0, padx = 10, pady = 10)
        #Precio
        self.Precio_label.grid(row = 4, column = 2, padx = 10, pady = 10)
        self.Precio_input.grid(row = 5, column = 2, padx = 10, pady = 10)
        #Botones
        self.Cargar_bott.grid(row = 0, column = 0, padx = 20, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 0, column = 2, padx = 20, pady = 10, ipadx = 5, ipady = 5)

    def Cargar(self):
        pass

    def Cancelar(self):
        self.destroy()
        self.master.deiconify()