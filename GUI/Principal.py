import tkinter as tk
from tkinter import ttk, messagebox
from Clases.Cuenta import Cuenta
from SQL import databases as db
from Registro import Registro
from Cliente import Cliente
from Administrador import Administrador

class Principal(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('645x450')
        self.config(bg = '#056595')
        self.title('Sistema de Autogestión - Cinemar')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.img_Cine = tk.PhotoImage(file = "GUI\Assets\Cine.png")
        self.resizable(0,0)

        """FRAMES"""
        #Cabecera
        self.f_cab = tk.Frame(self)
        self.f_cab.config(border = 5, background = '#FFFFFF')
        #Inicio de Sesion
        self.f_login = tk.Frame(self)
        self.f_login.config(border = 20, bg = '#056595')
        #Registro
        self.f_regis = tk.Frame(self)
        self.f_regis.config(border = 20, bg = '#056595')

        self.widgets()

    def widgets(self):
        #Posicionando los frames
        self.f_cab.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        self.f_login.grid(row = 1, column = 0)
        self.f_regis.grid(row = 1, column = 2)

        """CABECERA"""
        #Titulo
        cab = ttk.Label(self.f_cab)
        cab.config(text = ' Bienvenido a Cinemar ', foreground = '#FFFFFF', font = ('Segoe UI Black', 40), background = '#056595')
        cab.grid(padx = 0, ipady = 5)

        """INICIO DE SESION"""
        cab_log = ttk.Label(self.f_login)
        cab_log.config(text = '  Inicio de Sesión  ', foreground = '#FFFFFF', font = ('Segoe UI Black', 15), background = '#002B40', justify = 'center')
        cab_log.grid(row = 0, ipady = 10, pady = 10, padx = 30)

        #Usuario
        us_label = ttk.Label(self.f_login)
        us_label.config(text = 'Usuario', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        us_label.grid(row = 1, column = 0, pady = 5)

        us_entry = ttk.Entry(self.f_login)
        us_entry.grid(row = 2, column = 0)
        
        #Contraseña
        con_label = ttk.Label(self.f_login)
        con_label.config(text = 'Constraseña', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        con_label.grid(row = 3, column = 0, pady = 5)
        
        con_entry = ttk.Entry(self.f_login, show = '*')
        con_entry.grid(row = 4, column = 0)

        """REGISTRO"""
        #Imagen
        cine_img = tk.Label(self.f_regis)
        cine_img.config(image = self.img_Cine)
        cine_img.grid(row = 0, column = 0, pady = 20)

        #Registro
        regis_label = ttk.Label(self.f_regis)
        regis_label.config(text = 'Todavia no tenés una cuenta? Create una', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        regis_label.grid()

        """BOTONES"""
        #Iniciar Sesión
        Login_bott = ttk.Button(self.f_login, text = 'Iniciar Sesión')
        Login_bott.config(command = lambda: self.login(us_entry.get(), con_entry.get()))
        Login_bott.grid(ipady = 5, ipadx = 5, pady = 30)
        
        #Registrarse
        Regis_bott = ttk.Button(self.f_regis, text = 'Registrarse')
        Regis_bott.config(command = self.registro)
        Regis_bott.grid(ipady = 5, ipadx = 5, pady = 10)

    def login(self, usuario, contra):
        bdd = db.DataBase('cinemar.db')
        cuenta = Cuenta()
        if len(usuario) > 0 and len(contra) > 0:
            mensaje = cuenta.iniciar_sesion(bdd, usuario, contra)
            messagebox.showinfo('Inicio de Sesión', mensaje)
            if mensaje == 'Inicio de Sesión Exitoso!' and cuenta.admin == 1:
                self.withdraw()
                ventana = Cliente(self)
                ventana.mainloop()
            elif mensaje == 'Inicio de Sesión Exitoso!' and cuenta.admin == 2:
                self.withdraw()
                ventana = Administrador(self)
                ventana.mainloop()
        else:
            messagebox.showinfo('Inicio de Sesión', 'Debe rellenar todos los campos!')
    
    def registro(self):
        self.withdraw()
        ventana = Registro(self)
        ventana.mainloop()