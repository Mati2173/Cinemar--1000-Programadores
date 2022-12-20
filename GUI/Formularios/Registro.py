import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from Clases.Cuenta import Cuenta
from SQL import databases as db

class FormRegistro(Toplevel):
    def __init__(self, master = None, base_datos = None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('418x700')
        self.config(bg = '#056595')
        self.title('Registro')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.protocol('WM_DELETE_WINDOW', self.Cancelar)
        self.resizable(0,0)

        self.bdd = base_datos
        self.cuenta = Cuenta()
        
        """FRAMES"""
        self.F_cab = tk.Frame(self)         #Cabecera
        self.F_persona = tk.Frame(self)     #Datos de la Persona
        self.F_cuenta = tk.Frame(self)      #Datos de la cuenta
        self.F_boton = tk.Frame(self)       #Botones

        """WIDGETS"""
        #Titulo - Principal
        self.Cab_principal = ttk.Label(self.F_cab)
        #Titulo - Datos de la Persona
        self.Cab_persona = ttk.Label(self.F_persona)
        #Titulo - Datos de la Cuenta
        self.Cab_cuenta = ttk.Label(self.F_cuenta)
        #Apellido
        self.Ape_label = ttk.Label(self.F_persona)
        self.Ape_input = ttk.Entry(self.F_persona)
        #Nombre
        self.Nom_label = ttk.Label(self.F_persona)
        self.Nom_input = ttk.Entry(self.F_persona)
        #DNI
        self.Dni_label = ttk.Label(self.F_persona)
        self.Dni_input = ttk.Entry(self.F_persona)
        #Correo Electronico
        self.Mail_label = ttk.Label(self.F_persona)
        self.Mail_input = ttk.Entry(self.F_persona)
        #Telefono
        self.Tel_label = ttk.Label(self.F_persona)
        self.Tel_input = ttk.Entry(self.F_persona)
        #Usuario
        self.UsName_label = ttk.Label(self.F_cuenta)
        self.UsName_input = ttk.Entry(self.F_cuenta)
        #Contraseña
        self.PassW_label = ttk.Label(self.F_cuenta)
        self.PassW_input = ttk.Entry(self.F_cuenta)
        #Botones
        self.Registrarse_bott = ttk.Button(self.F_boton)
        self.Cancelar_bott = ttk.Button(self.F_boton)

        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()

        

    def frames_config(self):
        self.F_cab.config(border = 15, bg = '#002B40')
        self.F_persona.config(bg = '#056595')
        self.F_cuenta.config(bg = '#056595')
        self.F_boton.config(bg = '#056595')
    
    def widgets_config(self):
        #Titulo - Principal
        self.Cab_principal.config(text = 'Ingresá tus datos y creá\ntu cuenta ', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40', justify='center')
        #Titulo - Datos de la Persona
        self.Cab_persona.config(text = 'Datos Personales', foreground = '#FFFFFF', font = ('Segoe UI Black', 24), background = '#002B40')
        #Titulo - Datos de la Cuenta
        self.Cab_cuenta.config(text = 'Cuenta de Usuario', foreground = '#FFFFFF', font = ('Segoe UI Black', 24), background = '#002B40')
        #Apellido
        self.Ape_label.config(text = 'Apellido', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.Ape_input.config(width = 30)
        #Nombre
        self.Nom_label.config(text = 'Nombre', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.Nom_input.config(width = 30)
        #DNI
        self.Dni_label.config(text = 'DNI', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.Dni_input.config(width = 30)
        #Correo Electronico
        self.Mail_label.config(text = 'Correo Electrónico', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.Mail_input.config(width = 30)
        #Telefono
        self.Tel_label.config(text = 'Telefono', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.Tel_input.config(width = 30)
        #Usuario
        self.UsName_label.config(text = 'Usuario', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.UsName_input.config(width = 30)
        #Contraseña
        self.PassW_label.config(text = 'Contraseña', foreground = '#FFFFFF', font = ('Segoe UI Black', 14), background = '#056595')
        self.PassW_input.config(width = 30)
        #Botones
        self.Registrarse_bott.config(text = 'Registrarse', command = self.Registrarse)
        self.Cancelar_bott.config(text = 'Cancelar', command = self.Cancelar)

    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, columnspan = 2)
        self.F_persona.grid(row = 1, column = 0, columnspan = 2, pady = 20)
        self.F_cuenta.grid(row = 2, column = 0, columnspan = 2, pady = 20)
        self.F_boton.grid(row = 3, column = 0, columnspan = 2)

    def widgets_grid(self):
        #Titulo - Principal
        self.Cab_principal.grid(row = 0, ipady = 10)
        #Titulo - Datos de la Persona
        self.Cab_persona.grid(row = 0, column = 0, columnspan = 2)
        #Titulo - Datos de la Cuenta
        self.Cab_cuenta.grid(row = 0, column = 0)
        #Apellido
        self.Ape_label.grid(row = 1, column = 0, pady = 5)
        self.Ape_input.grid(row = 2, column = 0, padx = 10)
        #Nombre
        self.Nom_label.grid(row = 1, column = 1, pady = 5)
        self.Nom_input.grid(row = 2, column = 1, padx = 10)
        #DNI
        self.Dni_label.grid(row = 3, column = 0, pady = 5)
        self.Dni_input.grid(row = 4, column = 0, padx = 10)
        #Correo Electronico
        self.Mail_label.grid(row = 3, column = 1, pady = 5)
        self.Mail_input.grid(row = 4, column = 1, padx = 10)
        #Telefono
        self.Tel_label.grid(row = 5, column = 0, columnspan = 2, pady = 5)
        self.Tel_input.grid(row = 6, column = 0, columnspan = 2)
        #Usuario
        self.UsName_label.grid(row = 1, column = 0, pady = 5)
        self.UsName_input.grid(row = 2, column = 0, padx = 10)
        #Contraseña
        self.PassW_label.grid(row = 3, column = 0, pady = 5)
        self.PassW_input.grid(row = 4, column = 0, padx = 10)
        #Botones
        self.Registrarse_bott.grid(row = 5, column = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 5, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)

    def Registrarse(self):
        ap = self.Ape_input.get()
        nom = self.Nom_input.get()
        dni = self.Dni_input.get()
        email = self.Mail_input.get()
        tel = self.Tel_input.get()
        us = self.UsName_input.get()
        cont = self.PassW_input.get()

        if len(ap) > 0 and len(nom) > 0 and len(dni) > 0 and len(email) > 0 and len(tel) > 0 and len(us) > 0 and len(cont) > 0:
            mensaje = self.cuenta.registrarse(self.bdd, ap, nom, dni, email, tel, us, cont)
            messagebox.showinfo('Aviso', mensaje)
            if mensaje == 'Cuenta registrada exitosamente!':
                self.Cancelar()
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')

    def Cancelar(self):
        self.destroy()
        self.master.deiconify()