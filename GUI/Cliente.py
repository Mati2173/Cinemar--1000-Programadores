import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
from Clases.Cuenta import Cuenta
from SQL import databases as db
from GUI.Frames.Perfil import Perfil
from GUI.Frames.Reservas import ReservaCli
from GUI.Frames.Pelicula import PeliculaCli
from GUI.Frames.Inicio import Inicio

class Cliente(Toplevel):
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
        self.F_inicio = Inicio(self.F_principal, 1)
        self.F_perfil = Perfil(self.F_principal, self.cuenta_usuario, self.bdd)
        self.F_pelicula = PeliculaCli(self, self.F_principal, self.cuenta_usuario, self.bdd)
        self.F_reserva = ReservaCli(self.F_principal, self.cuenta_usuario, self.bdd)

        """BOTONES PRINCIPALES"""
        self.Inicio_bott = ttk.Button(self.F_principal)
        self.Perfil_bott = ttk.Button(self.F_principal)
        self.Peliculas_bott = ttk.Button(self.F_principal)
        self.Reservas_bott = ttk.Button(self.F_principal)
        self.Logout_bott = ttk.Button(self.F_principal)
        self.Opciones_img = tk.Label(self.F_principal)
        
        """IMAGENES"""
        self.img_Opciones = tk.PhotoImage(file = "GUI\Assets\OpcionesCliente.png")
        self.img_Inicio = tk.PhotoImage(file = "GUI\Assets\Home.png")
        self.img_Perfil = tk.PhotoImage(file = "GUI\Assets\Customer.png")
        self.img_Pelicula = tk.PhotoImage(file = "GUI\Assets\Pelicula.png")
        self.img_Reservas = tk.PhotoImage(file = "GUI\Assets\Ticket.png")
        self.img_Logout = tk.PhotoImage(file = 'GUI\Assets\Logout.png')

        self.frames_settings()
        self.F_principal.grid(row = 0, column = 0)
        self.Opciones_settings()
        self.Opciones_grid()
        self.MenuInicio()

    def frames_settings(self):
        self.F_principal.config(bg = '#056595')
        self.F_inicio.config(bg = '#056595')
        self.F_perfil.config(bg = '#056595')
        self.F_pelicula.config(bg = '#056595')
        self.F_reserva.config(bg = '#056595')

    def Opciones_settings(self):
        self.Inicio_bott.config(image = self.img_Inicio, command = self.MenuInicio)
        self.Perfil_bott.config(image = self.img_Perfil, command = self.MenuPerfil)
        self.Peliculas_bott.config(image = self.img_Pelicula, command = self.MenuPelicula)
        self.Reservas_bott.config(image = self.img_Reservas, command = self.MenuReservas)
        self.Logout_bott.config(image = self.img_Logout, command = self.Logout)
        self.Opciones_img.config(image = self.img_Opciones, border = 0)
        
    def Opciones_grid(self):
        self.Inicio_bott.grid(row = 0, column = 1, ipadx = 15, ipady = 5)
        self.Perfil_bott.grid(row = 0, column = 2, ipadx = 80, ipady = 5)
        self.Peliculas_bott.grid(row = 0, column = 3, ipadx = 80, ipady = 5)
        self.Reservas_bott.grid(row = 0, column = 4, ipadx = 80, ipady = 5)
        self.Logout_bott.grid(row = 0, column = 5, ipadx = 80, ipady = 5)
        self.Opciones_img.grid(row = 1, column = 0, columnspan = 8)
        
    def MenuInicio(self):
        self.ocultar_frames()
        self.F_inicio.grid(row = 2, column = 0, columnspan = 8)

    def MenuPerfil(self):
        self.ocultar_frames()
        self.F_perfil.grid(row = 2, column = 0, columnspan = 8)

    def MenuPelicula(self):
        self.ocultar_frames()
        self.F_pelicula.grid(row = 2, column = 0, columnspan = 8)

    def MenuReservas(self):
        self.ocultar_frames()
        self.F_reserva.grid(row = 2, column = 0, columnspan = 8)

    def ocultar_frames(self):
        self.F_inicio.grid_forget()
        self.F_perfil.grid_forget()
        self.F_pelicula.grid_forget()
        self.F_reserva.grid_forget()

    def Logout(self):
        self.cuenta_usuario.cerrar_sesion()
        messagebox.showinfo('Sesion Finalizada', 'Usted ha cerrado sesion.\nGracias por operar con Cinemar!')
        self.destroy()
        self.master.deiconify()