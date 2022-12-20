import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
from tkinter.scrolledtext import ScrolledText
from Clases.Pelicula import Pelicula
from SQL import databases as db

class FormPelicula(Toplevel):
    def __init__(self, master = None, base_datos = None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('720x720')
        self.config(bg = '#056595')
        self.title('Agregar Pelicula')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.protocol('WM_DELETE_WINDOW', self.Cancelar)
        self.resizable(0,0)

        self.bdd = base_datos
        self.pelicula = Pelicula()

        """FRAMES"""
        self.F_cab = tk.Frame(self)     #Cabecera
        self.F_datos = tk.Frame(self)   #Datos de la Pelicula
        self.F_boton = tk.Frame(self)   #Botones

        """WIDGETS"""
        #Titulo
        self.Cab_principal = ttk.Label(self.F_cab)
        #Nombre
        self.Nom_label = ttk.Label(self.F_datos)
        self.Nom_input = ttk.Entry(self.F_datos)
        #Duracion
        self.Dur_label = ttk.Label(self.F_datos)
        self.Dur_input = ttk.Entry(self.F_datos)
        #Genero
        self.Gen_label = ttk.Label(self.F_datos)
        self.Gen_input = ttk.Entry(self.F_datos)
        #Tipo
        self.Tipo_label = ttk.Label(self.F_datos)
        self.Tipo_input = ttk.Combobox(self.F_datos)
        #Director
        self.Direc_label = ttk.Label(self.F_datos)
        self.Direc_input = ttk.Entry(self.F_datos)
        #Actores
        self.Actor_label = ttk.Label(self.F_datos)
        self.Actor_input = ScrolledText(self.F_datos)
        #Sinopsis
        self.Sinop_label = ttk.Label(self.F_datos)
        self.Sinop_input = ScrolledText(self.F_datos)
        #Botones
        self.Cargar_bott = ttk.Button(self.F_boton)
        self.Cancelar_bott = ttk.Button(self.F_boton)

        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()



    def frames_config(self):
        self.F_cab.config(border = 15, bg = '#002B40')
        self.F_datos.config(bg = '#056595')
        self.F_boton.config(bg = '#056595')

    def widgets_config(self):
        #Titulo
        self.Cab_principal.config(text = '     Ingresá los datos de la nueva pelicula     ', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40')
        #Nombre
        self.Nom_label.config(text = 'Nombre', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Nom_input.config(width = 30)
        #Duracion
        self.Dur_label.config(text = 'Duración', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Dur_input.config(width = 30)
        #Genero
        self.Gen_label.config(text = 'Genero', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Gen_input.config(width = 30)
        #Tipo
        self.Tipo_label.config(text = 'Tipo', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Tipo_input.config(width = 27, state = 'readonly', values = ['2D', '3D'])
        #Director
        self.Direc_label.config(text = 'Director', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Direc_input.config(width = 40)
        #Actores
        self.Actor_label.config(text = 'Actores', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Actor_input.config(width = 80, height = 4)
        #Sinopsis
        self.Sinop_label.config(text = 'Sinopsis', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Sinop_input.config(width = 80, height = 7)
        #Botones
        self.Cargar_bott.config(text = 'Cargar Datos', command = self.Cargar)
        self.Cancelar_bott.config(text = 'Cancelar', command = self.Cancelar)

    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, rowspan = 2, columnspan = 3)
        self.F_datos.grid(row = 2, column = 0, rowspan = 12, columnspan = 3, padx = 30, pady = 20)
        self.F_boton.grid(row = 14, column = 0, columnspan = 3)

    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0)   
        #Nombre
        self.Nom_label.grid(row = 0, column = 0, pady = 10)
        self.Nom_input.grid(row = 1, column = 0)
        #Duracion
        self.Dur_label.grid(row = 0, column = 2, pady = 10)
        self.Dur_input.grid(row = 1, column = 2)
        #Genero
        self.Gen_label.grid(row = 2, column = 0, pady = 10)
        self.Gen_input.grid(row = 3, column = 0)
        #Tipo
        self.Tipo_label.grid(row = 2, column = 2, pady = 10)
        self.Tipo_input.grid(row = 3, column = 2)
        #Director
        self.Direc_label.grid(row = 4, column = 0, columnspan = 3, pady = 10)
        self.Direc_input.grid(row = 5, column = 0, columnspan = 3)
        #Actores
        self.Actor_label.grid(row = 6, column = 0, columnspan = 3, pady = 10)
        self.Actor_input.grid(row = 7, column = 0, rowspan = 2, columnspan = 3) 
        #Sinopsis
        self.Sinop_label.grid(row = 9, column = 0, columnspan = 3, pady = 10)
        self.Sinop_input.grid(row = 10, column = 0, rowspan = 3, columnspan = 3)
        #Botones
        self.Cargar_bott.grid(row = 0, column = 0, padx = 20, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 0, column = 2, padx = 20, pady = 10, ipadx = 5, ipady = 5)

    def Cargar(self):
        nom = self.Nom_input.get()
        dur = self.Dur_input.get()
        gen = self.Gen_input.get()
        tipo = self.Tipo_input.get()
        dir = self.Direc_input.get()
        act = self.Actor_input.get('1.0', 'end')
        sin = self.Sinop_input.get('1.0', 'end')

        if len(nom) > 0 and len(dur) > 0 and len(gen) > 0 and len(tipo) > 0 and len(dir) > 0 and len(act) > 0 and len(sin) > 0:
            self.pelicula.cargar_pelicula(self.bdd, nom, dur, gen, tipo, dir, act, sin)
            messagebox.showinfo('Aviso', 'Pelicula agregada exitosamente!')
            self.master.F_pelicula.input_fill()
            self.Cancelar()
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')

    def Cancelar(self):
        self.destroy()
        self.master.deiconify()