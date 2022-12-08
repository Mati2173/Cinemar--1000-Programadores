import tkinter as tk
from tkinter import ttk

class Bienvenido(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('645x450')
        self.config(bg = '#056595')
        self.title('Sistema de Autogestión - Cinemar')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.img = tk.PhotoImage(file = "GUI\Assets\Cine.png")
        self.resizable(0,0)

        self.widgets()

    def widgets(self):
        self.frame_cab()
        self.frame_login()
        self.frame_regis()

    def frame_cab(self):
        frame = tk.Frame(self, border = 5, background = '#FFFFFF')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        text = ttk.Label(frame, text = ' Bienvenido a Cinemar ', foreground = '#FFFFFF', font = ('Segoe UI Black', 40), background = '#056595')
        text.grid(padx = 0, ipady = 5)

    def frame_login(self):
        frame = tk.Frame(self, border = 20, bg = '#056595')
        frame.grid(row = 1, column = 0)

        #Inicio de Sesion
        ini_ses = ttk.Label(frame, text = '  Inicio de Sesión  ', foreground = '#FFFFFF', font = ('Segoe UI Black', 15), background = '#002B40', justify = 'center')
        ini_ses.grid(row = 0, ipady = 10, pady = 10, padx = 30)

        #Usuario
        us_label = ttk.Label(frame, text = 'Usuario', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        us_label.grid(row = 1, column = 0, pady = 5)
        us_entry = ttk.Entry(frame)
        us_entry.grid(row = 2, column = 0)
        
        #Contraseña
        pass_label = ttk.Label(frame, text = 'Constraseña', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        pass_label.grid(row = 3, column = 0, pady = 5)
        pass_entry = ttk.Entry(frame, show = '*')
        pass_entry.grid(row = 4, column = 0)

        #Boton - Inicio de Sesión
        login_bot = ttk.Button(frame, text = 'Iniciar Sesión')
        login_bot.grid(ipady = 5, ipadx = 5, pady = 30)
        
    def frame_regis(self):
        frame = tk.Frame(self, border = 20, bg = '#056595')
        frame.grid(row = 1, column = 2)

        #Imagen
        lbl_img = tk.Label(frame, image = self.img)
        lbl_img.grid(row = 0, column = 0, pady = 20)

        #Registro
        regis = ttk.Label(frame, text = 'Todavia no tenés una cuenta? Create una', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        regis.grid()
        
        #Botón - Registrarse
        registro_bot = ttk.Button(frame, text = 'Registrarse')
        registro_bot.grid(ipady = 5, ipadx = 5, pady = 10)

a = Bienvenido()
a.mainloop()