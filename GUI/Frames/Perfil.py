import tkinter as tk
from tkinter import ttk
from Clases.Cuenta import Cuenta

class Perfil(tk.Frame):
    def __init__(self, master = None, cuenta_usuario = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos

        """WIDGETS"""
        #Titulo
        self.Cab_principal = ttk.Label(self)
        #Apellido
        self.Ape_label = ttk.Label(self)
        self.Ape_input = ttk.Entry(self)
        #Nombre
        self.Nom_label = ttk.Label(self)
        self.Nom_input = ttk.Entry(self)
        #DNI
        self.Dni_label = ttk.Label(self)
        self.Dni_input = ttk.Entry(self)
        #Correo Electronico
        self.Mail_label = ttk.Label(self)
        self.Mail_input = ttk.Entry(self)
        #Telefono
        self.Tel_label = ttk.Label(self)
        self.Tel_input = ttk.Entry(self)
        #Usuario
        self.UsName_label = ttk.Label(self)
        self.UsName_input = ttk.Entry(self)
        #Contraseña
        self.PassW_label = ttk.Label(self)
        self.PassW_input = ttk.Entry(self)
        #Botones
        self.Ver_Contra_bott = ttk.Button(self)
        self.Ocultar_Contra_bott = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()



    def widgets_config(self):
        self.input_insert()
        #Titulo
        self.Cab_principal.config(text = '     Datos Personales     ', foreground = '#FFFFFF', font = ('Segoe UI Black', 36), background = '#002B40', justify = 'center')
        #Apellido
        self.Ape_label.config(text = 'Apellido', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Ape_input.config(width = 30, state = "readonly")
        #Nombre
        self.Nom_label.config(text = 'Nombre', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Nom_input.config(width = 30, state = "readonly")
        #DNI
        self.Dni_label.config(text = 'DNI', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Dni_input.config(width = 30, state = "readonly")
        #Correo Electronico
        self.Mail_label.config(text = 'Correo Electrónico', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Mail_input.config(width = 30, state = "readonly")
        #Telefono
        self.Tel_label.config(text = 'Telefono', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Tel_input.config(width = 30, state = "readonly")
        #Usuario
        self.UsName_label.config(text = 'Usuario', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.UsName_input.config(width = 30, state = "readonly")
        #Contraseña
        self.PassW_label.config(text = 'Contraseña', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.PassW_input.config(width = 30, state = 'readonly' , show = '*')
        #Botones
        self.Ver_Contra_bott.config(text = 'Mostrar Contraseña', command = self.Ver_PassW)
        self.Ocultar_Contra_bott.config(text = 'Ocultar contraseña', command = self.Ocultar_PasW)

    def input_insert(self):
        self.Ape_input.insert(0, self.cuenta_usuario.apellido)
        self.Nom_input.insert(0, self.cuenta_usuario.nombre)
        self.Dni_input.insert(0, self.cuenta_usuario.dni)
        self.Mail_input.insert(0, self.cuenta_usuario.email)
        self.Tel_input.insert(0, self.cuenta_usuario.telefono)
        self.UsName_input.insert(0, self.cuenta_usuario.usuario)
        self.PassW_input.insert(0, self.cuenta_usuario.password)

    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0, column = 0, columnspan = 2, pady = 20, ipady = 10)
        #Apellido
        self.Ape_label.grid(row = 1, column = 0, pady = 5)
        self.Ape_input.grid(row = 1, column = 1, padx = 20)
        #Nombre
        self.Nom_label.grid(row = 2, column = 0, pady = 5)
        self.Nom_input.grid(row = 2, column = 1, padx = 20)
        #DNI
        self.Dni_label.grid(row = 3, column = 0, pady = 5)
        self.Dni_input.grid(row = 3, column = 1, padx = 20)
        #Correo Electronico
        self.Mail_label.grid(row = 4, column = 0, pady = 5)
        self.Mail_input.grid(row = 4, column = 1, padx = 20)
        #Telefono
        self.Tel_label.grid(row = 5, column = 0, pady = 5)
        self.Tel_input.grid(row = 5, column = 1, padx = 20)
        #Usuario
        self.UsName_label.grid(row = 6, column = 0, pady = 5)
        self.UsName_input.grid(row = 6, column = 1, padx = 20)
        #Contraseña
        self.PassW_label.grid(row = 7, column = 0, pady = 5)
        self.PassW_input.grid(row = 7, column = 1, padx = 20)
        #Botones
        self.Ver_Contra_bott.grid(row = 8, column = 0, columnspan = 2, pady = 20, padx = 10, ipady = 5, ipadx = 5)

    def Ver_PassW(self):
        self.PassW_input.config(show = '')
        self.Ver_Contra_bott.grid_forget()
        self.Ocultar_Contra_bott.grid(row = 8, column = 0, columnspan = 2, pady = 20, padx = 10, ipady = 5, ipadx = 5)
    
    def Ocultar_PasW(self):
        self.PassW_input.config(show = '*')
        self.Ocultar_Contra_bott.grid_forget()
        self.Ver_Contra_bott.grid(row = 8, column = 0, columnspan = 2, pady = 20, padx = 10, ipady = 5, ipadx = 5)