import tkinter as tk
from tkinter import ttk, messagebox
from Clases.Cuenta import Cuenta
from SQL import databases as db
from GUI.Formularios.Registro import FormRegistro
from GUI.Administrador import Administrador
from GUI.Cliente import Cliente

class Main(tk.Tk):
    def __init__(self, base_datos = None):
        tk.Tk.__init__(self)
        self.geometry('645x450')
        self.config(bg = '#056595')
        self.title('Cinemar')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.resizable(0,0)

        self.bdd = base_datos
        self.cuenta = Cuenta()

        """IMAGENES"""
        self.img_Cine = tk.PhotoImage(file = "GUI\Assets\Cine.png")

        """FRAMES"""
        self.F_cab = tk.Frame(self)
        self.F_login = tk.Frame(self)
        self.F_regis = tk.Frame(self)

        """WIDGETS"""
        self.Cab_principal = ttk.Label(self.F_cab)
        self.Cab_log = ttk.Label(self.F_login)
        self.UsName_label = ttk.Label(self.F_login)
        self.UsName_input = ttk.Entry(self.F_login)
        self.PassW_label = ttk.Label(self.F_login)
        self.PassW_input = ttk.Entry(self.F_login)
        self.Img_deco = tk.Label(self.F_regis)
        self.Regis_label = ttk.Label(self.F_regis)
        self.Login_bott = ttk.Button(self.F_login)
        self.Registrarse_bott = ttk.Button(self.F_regis)

        self.frames_settings()
        self.frames_grid()
        self.widgets_settings()
        self.widgets_grid()

    def frames_settings(self):
        self.F_cab.config(border = 5, background = '#FFFFFF')
        self.F_login.config(border = 20, bg = '#056595')
        self.F_regis.config(border = 20, bg = '#056595')
    
    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        self.F_login.grid(row = 1, column = 0)
        self.F_regis.grid(row = 1, column = 2)
    
    def widgets_settings(self):
        self.Cab_principal.config(text = ' Bienvenido a Cinemar ', foreground = '#FFFFFF', font = ('Segoe UI Black', 40), background = '#056595')
        self.Cab_log.config(text = '  Inicio de Sesión  ', foreground = '#FFFFFF', font = ('Segoe UI Black', 15), background = '#002B40', justify = 'center')
        self.UsName_label.config(text = 'Usuario', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        self.UsName_input.config(width = 20)
        self.PassW_label.config(text = 'Contraseña', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        self.PassW_input.config(width = 20, show = '*')
        self.Img_deco.config(image = self.img_Cine)
        self.Regis_label.config(text = 'Todavia no tenés una cuenta? Create una', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        self.Login_bott.config(text = 'Iniciar Sesión', command = self.Login)
        self.Registrarse_bott.config(text = 'Registrarse', command = self.Registrar)

    def widgets_grid(self):
        self.Cab_principal.grid(padx = 0, ipady = 5)
        self.Cab_log.grid(row = 0, ipady = 10, pady = 10, padx = 30)
        self.UsName_label.grid(row = 1, column = 0, pady = 5)
        self.UsName_input.grid(row = 2, column = 0)
        self.PassW_label.grid(row = 3, column = 0, pady = 5)
        self.PassW_input.grid(row = 4, column = 0)
        self.Img_deco.grid(row = 0, column = 0, pady = 20)
        self.Regis_label.grid()
        self.Login_bott.grid(ipady = 5, ipadx = 5, pady = 30)
        self.Registrarse_bott.grid(ipady = 5, ipadx = 5, pady = 10)

    def Login(self):
        usuario = self.UsName_input.get()
        contra = self.PassW_input.get()

        if len(usuario) > 0 and len(contra) > 0:
            mensaje = self.cuenta.iniciar_sesion(self.bdd, usuario, contra)
            messagebox.showinfo('Inicio de Sesión', mensaje)
            
            if mensaje == 'Inicio de Sesión Exitoso!':
                self.UsName_input.delete(0, 'end')
                self.PassW_input.delete(0, 'end')
                self.withdraw()

                if self.cuenta.admin == 1:
                    ventana = Cliente(self, self.cuenta, self.bdd)
                else:
                    ventana = Administrador(self, self.cuenta, self.bdd)

                ventana.mainloop()
        else:
            messagebox.showinfo('Inicio de Sesión', 'Debe rellenar todos los campos!')
    
    def Registrar(self):
        self.withdraw()
        ventana = FormRegistro(self, self.bdd)
        ventana.mainloop()