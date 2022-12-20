import tkinter as tk
from tkinter import ttk, Toplevel
from Clases.Pelicula import Pelicula
from SQL import databases as db

class MasDetalles(Toplevel):
    def __init__(self, master = None, id_pelicula = None, base_datos = None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('700x480')
        self.config(bg = '#056595')
        self.title('Más detalles')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.resizable(0,0)

        self.bdd = base_datos
        self.pelicula = Pelicula()
        self.detalles = self.pelicula.mas_detalles(self.bdd, id_pelicula)
        
        """FRAMES"""
        self.F_cab = tk.Frame(self)     #Cabecera
        self.F_datos = tk.Frame(self)   #Datos de la Funcion
    
        """WIDGETS"""
        self.Cab_principal = ttk.Label(self.F_cab)
        self.Direc_label = ttk.Label(self.F_datos)
        self.Direc_input = ttk.Entry(self.F_datos)
        self.Act_label = ttk.Label(self.F_datos)
        self.Act_input = tk.Text(self.F_datos)
        self.Sinop_label = ttk.Label(self.F_datos)
        self.Sinop_input = tk.Text(self.F_datos)
    
        self.input_fill()
        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()



    def frames_config(self):
        self.F_cab.config(border = 15, bg = '#002B40')
        self.F_datos.config(bg = '#056595')
    
    def widgets_config(self):
        self.Cab_principal.config(text = ' Detalles sobre la pelicula ', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40')
        self.Direc_label.config(text = 'Director', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Direc_input.config(width = 40, state = 'readonly')
        self.Act_label.config(text = 'Actores', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Act_input.config(width = 80, height = 4, state = 'disabled', wrap = 'word')
        self.Sinop_label.config(text = 'Sinopsis', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Sinop_input.config(width = 80, height = 7, state = 'disabled', wrap = 'word')

    def input_fill(self):
        self.Direc_input.insert(0, self.detalles[0])
        self.Act_input.insert('1.0', self.detalles[1])
        self.Sinop_input.insert('1.0', self.detalles[2])

    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, columnspan = 3)
        self.F_datos.grid(row = 1, column = 0, columnspan = 3, padx = 20)

    def widgets_grid(self):
        self.Cab_principal.grid(row = 0, column = 0, columnspan = 3)
        self.Direc_label.grid(row = 0, column = 0, columnspan = 3, pady = 10)
        self.Direc_input.grid(row = 1, column = 0, columnspan = 3)
        self.Act_label.grid(row = 2, column = 0, columnspan = 3, pady = 10)
        self.Act_input.grid(row = 3, column = 0, columnspan = 3)
        self.Sinop_label.grid(row = 4, column = 0, columnspan = 3, pady = 10)
        self.Sinop_input.grid(row = 5, column = 0, columnspan = 3)
    