import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
from Clases.Cuenta import Cuenta
from SQL import databases as db
from GUI.Frames.Reservas import ReservaAdm
from GUI.Frames.Sala import SalaAdm
from GUI.Frames.Pelicula import PeliculaAdm
from GUI.Frames.Funciones import FuncionAdm
from GUI.Frames.Perfil import Perfil
from GUI.Frames.Descuento import DescuentoAdm
from GUI.Frames.Inicio import Inicio

class Administrador(Toplevel):
    def __init__(self, master = None, cuenta_usuario = None, base_datos = None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('1080x720')
        self.config(bg = '#056595')
        self.title('Sistema de Autogestión - Cinemar')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.protocol('WM_DELETE_WINDOW', self.Logout)
        self.resizable(0,0)

        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos

        """FRAMES"""
        self.F_principal = tk.Frame(self)
        self.F_inicio = Inicio(self.F_principal, 2)
        self.F_descuento = DescuentoAdm(self.F_principal, self.bdd)
        self.F_pelicula = PeliculaAdm(self, self.F_principal, self.bdd)
        self.F_sala = SalaAdm(self.F_principal, self.bdd)
        self.F_funcion = FuncionAdm(self, self.F_principal, self.bdd)
        self.F_reserva = ReservaAdm(self.F_principal, self.bdd)

        """BOTONES PRINCIPALES"""
        self.Inicio_bott = ttk.Button(self.F_principal)
        self.Descuento_bott = ttk.Button(self.F_principal)
        self.Peliculas_bott = ttk.Button(self.F_principal)
        self.Salas_bott = ttk.Button(self.F_principal)
        self.Funciones_bott = ttk.Button(self.F_principal)
        self.Reservas_bott = ttk.Button(self.F_principal)
        self.Logout_bott = ttk.Button(self.F_principal)
        self.Opciones_img = tk.Label(self.F_principal)

        """IMAGENES"""
        self.img_Opciones = tk.PhotoImage(file = "GUI\Assets\OpcionesAdministrador.png")
        self.img_Inicio = tk.PhotoImage(file = "GUI\Assets\Home.png")
        self.img_Descuento = tk.PhotoImage(file = "GUI\Assets\Descuento.png")
        self.img_Sala = tk.PhotoImage(file = "GUI\Assets\Sala.png")
        self.img_Pelicula = tk.PhotoImage(file = "GUI\Assets\Pelicula.png")
        self.img_Funciones = tk.PhotoImage(file = "GUI\Assets\Funcion.png")
        self.img_Reservas = tk.PhotoImage(file = "GUI\Assets\Ticket.png")
        self.img_Logout = tk.PhotoImage(file = 'GUI\Assets\Logout.png')

        self.frames_config()
        self.Opciones_config()

        self.F_principal.grid(row = 0, column = 0)
        self.Opciones_grid()
        self.MenuInicio()
    

    
    def frames_config(self):
        self.F_principal.config(bg = '#056595')
        self.F_inicio.config(bg = '#056595')
        self.F_descuento.config(bg = '#056595')
        self.F_pelicula.config(bg = '#056595')
        self.F_sala.config(bg = '#056595')
        self.F_funcion.config(bg = '#056595')
        self.F_reserva.config(bg = '#056595')

    def Opciones_config(self):
        self.Inicio_bott.config(image = self.img_Inicio, command = self.MenuInicio)
        self.Descuento_bott.config(image = self.img_Descuento, command = self.MenuPerfil)
        self.Peliculas_bott.config(image = self.img_Pelicula, command = self.MenuPelicula)
        self.Salas_bott.config(image = self.img_Sala, command = self.MenuSala)
        self.Funciones_bott.config(image = self.img_Funciones, command = self.MenuFuncion)
        self.Reservas_bott.config(image = self.img_Reservas, command = self.MenuReserva)
        self.Logout_bott.config(image = self.img_Logout, command = self.Logout)

    def Opciones_grid(self):
        self.Opciones_img.config(image = self.img_Opciones, border = 0)
        self.Inicio_bott.grid(row = 0, column = 1, ipadx = 13, ipady = 5)
        self.Descuento_bott.grid(row = 0, column = 2, ipadx = 40, ipady = 5)
        self.Peliculas_bott.grid(row = 0, column = 3, ipadx = 40, ipady = 5)
        self.Salas_bott.grid(row = 0, column = 4, ipadx = 40, ipady = 5)
        self.Funciones_bott.grid(row = 0, column = 5, ipadx = 40, ipady = 5)
        self.Reservas_bott.grid(row = 0, column = 6, ipadx = 40, ipady = 5)
        self.Logout_bott.grid(row = 0, column = 7, ipadx = 40, ipady = 5)   
        self.Opciones_img.grid(row = 1, column = 0, columnspan = 8)

    def MenuInicio(self):
        self.ocultar_frames()
        self.F_inicio.grid(row = 2, column = 0, columnspan = 8)

    def MenuPerfil(self):
        self.ocultar_frames()
        self.F_descuento.grid(row = 2, column = 0, columnspan = 8)

    def MenuPelicula(self):
        self.ocultar_frames()
        self.F_pelicula.grid(row = 2, column = 0, columnspan = 8)

    def MenuSala(self):
        self.ocultar_frames()
        self.F_sala.grid(row = 2, column = 0, columnspan = 8)

    def MenuFuncion(self):
        self.ocultar_frames()
        self.F_funcion.grid(row = 2, column = 0, columnspan = 8)

    def MenuReserva(self):
        self.ocultar_frames()
        self.F_reserva.grid(row = 2, column = 0, columnspan = 8)

    def ocultar_frames(self):
        self.F_inicio.grid_forget()
        self.F_descuento.grid_forget()
        self.F_pelicula.grid_forget()
        self.F_sala.grid_forget()
        self.F_funcion.grid_forget()
        self.F_reserva.grid_forget()

    def Logout(self):
        self.cuenta_usuario.cerrar_sesion()
        messagebox.showinfo('Sesion Finalizada', 'Usted ha cerrado sesion.\nGracias por operar con Cinemar!')
        self.destroy()
        self.master.deiconify()