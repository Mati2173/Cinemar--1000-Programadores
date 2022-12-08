import tkinter as tk
from tkinter import ttk

class Registro(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('415x670')
        self.config(bg = '#056595')
        self.title('Sistema de Autogestión - Cinemar')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.img = tk.PhotoImage(file = "GUI\Assets\Cine.png")
        self.resizable(0,0)

        self.widgets()

    def widgets(self):
        self.frame_cab()
        self.frame_persona()
        self.frame_cuenta()
        self.reg_boton()
    
    def frame_cab(self):
        frame = tk.Frame(self, border = 15, bg = '#002B40')
        frame.grid(row = 0, column = 0)

        text = ttk.Label(frame, text = 'Ingresá tus datos y creá\ntu cuenta', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40', justify='center')
        text.grid(row = 0, ipady = 10)
    
    def frame_persona(self):
        frame = tk.Frame(self, background = '#056595')
        frame.grid(row = 1, column = 0, pady = 20)

        text = ttk.Label(frame, text = 'Datos Personales', foreground = '#FFFFFF', font = ('Segoe UI Black', 24), background = '#002B40')
        text.grid(row = 0, column = 0, columnspan = 2)

        apellido_label = ttk.Label(frame, text = 'Apellido', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        apellido_label.grid(row = 1, column = 0, pady = 5)
        apellido_entry = ttk.Entry(frame)
        apellido_entry.grid(row = 2, column = 0, padx = 20, ipadx = 20)

        nombre_label = ttk.Label(frame, text = 'Nombre', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        nombre_label.grid(row = 1, column = 1, pady = 5)
        nombre_entry = ttk.Entry(frame)
        nombre_entry.grid(row = 2, column = 1, padx = 20, ipadx = 20)

        dni_label = ttk.Label(frame, text = 'DNI', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        dni_label.grid(row = 3, column = 0, pady = 5)
        dni_entry = ttk.Entry(frame)
        dni_entry.grid(row = 4, column = 0, padx = 20, ipadx = 20)

        email_label = ttk.Label(frame, text = 'Correo Electrónico', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        email_label.grid(row = 3, column = 1, pady = 5)
        email_entry = ttk.Entry(frame)
        email_entry.grid(row = 4, column = 1, padx = 20, ipadx = 20)

        telefono_label = ttk.Label(frame, text = 'Telefono', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        telefono_label.grid(row = 5, column = 0, pady = 5, columnspan = 2)
        telefono_entry = ttk.Entry(frame)
        telefono_entry.grid(row = 6, column = 0, columnspan = 2, padx = 20, ipadx = 20)

    def frame_cuenta(self):
        frame = tk.Frame(self, background = '#056595')
        frame.grid(row = 2, column = 0, pady = 20)

        text = ttk.Label(frame, text = 'Cuenta de Usuario', foreground = '#FFFFFF', font = ('Segoe UI Black', 24), background = '#002B40')
        text.grid(row = 0, column = 0)

        us_label = ttk.Label(frame, text = 'Usuario', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        us_label.grid(row = 1, column = 0, pady = 5)
        us_entry = ttk.Entry(frame)
        us_entry.grid(row = 2, column = 0, padx = 20, ipadx = 20)
        
        pass_label = ttk.Label(frame, text = 'Contraseña', foreground = '#FFFFFF', font = ('Segoe UI Black', 12), background = '#056595')
        pass_label.grid(row = 3, column = 0, pady = 5)
        pass_entry = ttk.Entry(frame)
        pass_entry.grid(row = 4, column = 0, padx = 20, ipadx = 20)
    
    def reg_boton(self):
        registro = ttk.Button(self, text = 'Registrarse')
        registro.grid(row = 5, ipady = 5, ipadx = 5, pady = 10)

a = Registro()
a.mainloop()