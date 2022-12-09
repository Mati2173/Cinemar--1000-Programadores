import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from Clases.Cuenta import Cuenta
from SQL import databases as db

class Registro(Toplevel):
    def __init__(self, ventana_padre):
        Toplevel.__init__(self, ventana_padre)
        self.ventana_padre = ventana_padre
        self.geometry('415x670')
        self.config(bg = '#056595')
        self.title('Sistema de Autogestión - Cinemar')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.resizable(0,0)
        self.protocol('WM_DELETE_WINDOW', self.cancelar)

        self.img = tk.PhotoImage(file = "GUI\Assets\Cine.png")
        
        """FRAMES"""
        #Cabecera
        self.f_cab = tk.Frame(self)
        self.f_cab.config(border = 15, bg = '#002B40')
        #Datos Personales
        self.f_persona = tk.Frame(self)
        self.f_persona.config(background = '#056595')
        #Datos Usuario
        self.f_cuenta = tk.Frame(self)
        self.f_cuenta.config(background = '#056595')
        #Botones
        self.f_boton = tk.Frame(self)
        self.f_boton.config(background = '#056595')

        self.widgets()

    def widgets(self):
        #Posicionando los frames
        self.f_cab.grid(row = 0, column = 0)
        self.f_persona.grid(row = 1, column = 0, pady = 20)
        self.f_cuenta.grid(row = 2, column = 0, pady = 20)
        self.f_boton.grid(row = 3, column = 0)

        """CABECERA"""
        #Titulo
        cab = ttk.Label(self.f_cab)
        cab.config(text = 'Ingresá tus datos y creá\ntu cuenta', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40', justify='center')
        cab.grid(row = 0, ipady = 10)
    
        """DATOS PERSONALES"""
        cab_per = ttk.Label(self.f_persona, text = 'Datos Personales', foreground = '#FFFFFF', font = ('Segoe UI Black', 24), background = '#002B40')
        cab_per.grid(row = 0, column = 0, columnspan = 2)

        #Apellido
        ap_label = ttk.Label(self.f_persona)
        ap_label.config(text = 'Apellido', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        ap_label.grid(row = 1, column = 0, pady = 5)

        ap_entry = ttk.Entry(self.f_persona)
        ap_entry.grid(row = 2, column = 0, padx = 20, ipadx = 20)

        #Nombre
        nom_label = ttk.Label(self.f_persona)
        nom_label.config(text = 'Nombre', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        nom_label.grid(row = 1, column = 1, pady = 5)

        nom_entry = ttk.Entry(self.f_persona)
        nom_entry.grid(row = 2, column = 1, padx = 20, ipadx = 20)

        #DNI
        dni_label = ttk.Label(self.f_persona)
        dni_label.config(text = 'DNI', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        dni_label.grid(row = 3, column = 0, pady = 5)

        dni_entry = ttk.Entry(self.f_persona)
        dni_entry.grid(row = 4, column = 0, padx = 20, ipadx = 20)

        #Correo Electróoico
        mail_label = ttk.Label(self.f_persona)
        mail_label.config(text = 'Correo Electrónico', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        mail_label.grid(row = 3, column = 1, pady = 5)

        mail_entry = ttk.Entry(self.f_persona)
        mail_entry.grid(row = 4, column = 1, padx = 20, ipadx = 20)

        #Numero de telefono
        tel_label = ttk.Label(self.f_persona)
        tel_label.config(text = 'Telefono', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        tel_label.grid(row = 5, column = 0, pady = 5, columnspan = 2)

        tel_entry = ttk.Entry(self.f_persona)
        tel_entry.grid(row = 6, column = 0, columnspan = 2, padx = 20, ipadx = 20)

        """DATOS CUENTA DE USUARIO"""
        #Titulo
        cab_cuenta = ttk.Label(self.f_cuenta)
        cab_cuenta.config(text = 'Cuenta de Usuario', foreground = '#FFFFFF', font = ('Segoe UI Black', 24), background = '#002B40')
        cab_cuenta.grid(row = 0, column = 0)

        #Usuario
        us_label = ttk.Label(self.f_cuenta)
        us_label.config(text = 'Usuario', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        us_label.grid(row = 1, column = 0, pady = 5)

        us_entry = ttk.Entry(self.f_cuenta)
        us_entry.grid(row = 2, column = 0, padx = 20, ipadx = 20)
        
        #Contraseña
        con_label = ttk.Label(self.f_cuenta)
        con_label.config(text = 'Contraseña', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        con_label.grid(row = 3, column = 0, pady = 5)

        con_entry = ttk.Entry(self.f_cuenta)
        con_entry.grid(row = 4, column = 0, padx = 20, ipadx = 20)

        """BOTONES"""
        #Registrarse
        Regis_bott = ttk.Button(self.f_boton, text = 'Registrarse')
        Regis_bott.config(command = lambda: self.register(ap_entry.get(), nom_entry.get(), dni_entry.get(), mail_entry.get(), tel_entry.get(), us_entry.get(), con_entry.get()))
        Regis_bott.grid(row = 5, ipady = 5, ipadx = 5, pady = 10, padx = 10, column = 0)

        #Cancelar
        Cancel_bott = ttk.Button(self.f_boton, text = 'Cancelar')
        Cancel_bott.config(command = self.cancelar)
        Cancel_bott.grid(row = 5, ipady = 5, ipadx = 5, pady = 10, padx = 10, column = 1)

    def register(self, ap, nom, dni, email, tel, us, cont):
        bdd = db.DataBase('cinemar.db')
        cuenta = Cuenta()
        if len(ap) > 0 and len(nom) > 0 and len(dni) > 0 and len(email) > 0 and len(tel) > 0 and len(us) > 0 and len(cont) > 0:
            mensaje = cuenta.registrarse(bdd, ap, nom, dni, email, tel, us, cont)
            messagebox.showinfo('Inicio de Sesión', mensaje)
        else:
            messagebox.showinfo('Inicio de Sesión', 'Debe rellenar todos los campos!')
    
    def cancelar(self):
        self.destroy()
        self.ventana_padre.deiconify()