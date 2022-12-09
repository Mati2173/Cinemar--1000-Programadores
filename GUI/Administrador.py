import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
from SQL import databases as db

class Administrador(Toplevel):
    def __init__(self, ventana_padre):
        Toplevel.__init__(self, ventana_padre)
        self.ventana_padre = ventana_padre
        self.geometry('1080x720')
        self.config(bg = '#056595')
        self.title('Sistema de Autogestión - Cinemar')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.protocol('WM_DELETE_WINDOW', self.logout)
        #self.resizable(0,0)

        """IMAGENES"""
        self.img_Opciones = tk.PhotoImage(file = "GUI\Assets\OpcionesAdministrador.png")
        self.img_Inicio = tk.PhotoImage(file = "GUI\Assets\Home.png")
        self.img_Perfil = tk.PhotoImage(file = "GUI\Assets\Customer.png")
        self.img_Sala = tk.PhotoImage(file = "GUI\Assets\Sala.png")
        self.img_Pelicula = tk.PhotoImage(file = "GUI\Assets\Pelicula.png")
        self.img_Funciones = tk.PhotoImage(file = "GUI\Assets\Funcion.png")
        self.img_Reservas = tk.PhotoImage(file = "GUI\Assets\Ticket.png")
        self.img_Logout = tk.PhotoImage(file = 'GUI\Assets\Logout.png')

        """FRAMES"""
        #Menu Opciones
        self.f_principal = tk.Frame(self)
        self.f_principal.config()
        #Home
        self.f_inicio = tk.Frame(self.f_principal)
        self.f_inicio.config()
        #Perfil
        self.f_perfil = tk.Frame(self.f_principal)
        self.f_perfil.config()
        #Peliculas
        self.f_pelicula = tk.Frame(self.f_principal)
        self.f_pelicula.config()
        #Salas
        self.f_sala = tk.Frame(self.f_principal)
        self.f_sala.config()
        #Funcion
        self.f_funcion = tk.Frame(self.f_principal)
        self.f_funcion.config()
        #Reservas
        self.f_reserva = tk.Frame(self.f_principal)
        self.f_reserva.config()

        self.widgets()
    
    def widgets(self):
        #Posicionando el Frame Principal
        self.f_principal.grid(row = 0, column = 0)
    
        self.barra_opciones()
        self.menu_inicio()

    def barra_opciones(self):
        """BOTONES"""
        #Inicio
        Inicio_bott = ttk.Button(self.f_principal)
        Inicio_bott.config(image = self.img_Inicio, command = self.menu_inicio)
        Inicio_bott.grid(row = 0, column = 1, ipadx = 13, ipady = 5)

        #Perfil
        Perfil_bott = ttk.Button(self.f_principal)
        Perfil_bott.config(image = self.img_Perfil, command = self.menu_perfil)
        Perfil_bott.grid(row = 0, column = 2, ipadx = 40, ipady = 5)

        #Peliculas
        Peliculas_bott = ttk.Button(self.f_principal)
        Peliculas_bott.config(image = self.img_Pelicula, command = self.menu_pelicula)
        Peliculas_bott.grid(row = 0, column = 3, ipadx = 40, ipady = 5)

        #Salas
        Salas_bott = ttk.Button(self.f_principal)
        Salas_bott.config(image = self.img_Sala, command = self.menu_sala)
        Salas_bott.grid(row = 0, column = 4, ipadx = 40, ipady = 5)

        #Funciones
        Funciones_bott = ttk.Button(self.f_principal)
        Funciones_bott.config(image = self.img_Funciones, command = self.menu_funcion)
        Funciones_bott.grid(row = 0, column = 5, ipadx = 40, ipady = 5)

        #Reservas
        Reservas_bott = ttk.Button(self.f_principal)
        Reservas_bott.config(image = self.img_Reservas, command = self.menu_reserva)
        Reservas_bott.grid(row = 0, column = 6, ipadx = 40, ipady = 5)

        #Cerrar sesion
        Logout_bott = ttk.Button(self.f_principal)
        Logout_bott.config(image = self.img_Logout, command = self.logout)
        Logout_bott.grid(row = 0, column = 7, ipadx = 40, ipady = 5)   

        #Imagen
        opciones_img = tk.Label(self.f_principal)
        opciones_img.config(image = self.img_Opciones, border = 0)
        opciones_img.grid(row = 1, column = 0, columnspan = 8)

    def menu_inicio(self):
        self.borrar_frames()
        self.f_inicio.grid(row = 1, column = 0, columnspan = 8)

    def menu_perfil(self):
        self.borrar_frames()
        self.f_perfil.grid(row = 1, column = 0, columnspan = 8)
        self.mostrar_perfil()

    def menu_pelicula(self):
        self.borrar_frames()
        self.f_pelicula.grid(row = 1, column = 0, columnspan = 8)
        self.mostrar_peliculas()

    def menu_sala(self):
        self.borrar_frames()
        self.f_sala.grid(row = 1, column = 0, columnspan = 8)
        self.mostrar_salas()

    def menu_funcion(self):
        self.borrar_frames()
        self.f_funcion.grid(row = 1, column = 0, columnspan = 8)
        self.mostrar_funciones()

    def menu_reserva(self):
        self.borrar_frames()
        self.f_reserva.grid(row = 1, column = 0, columnspan = 8)
        self.mostrar_reservas()

    def borrar_frames(self):
        self.f_inicio.grid_forget()
        self.f_perfil.grid_forget()
        self.f_pelicula.grid_forget()
        self.f_sala.grid_forget()
        self.f_funcion.grid_forget()
        self.f_reserva.grid_forget()

    def logout(self):
        messagebox.showinfo('Sesion Finalizada', 'Usted ha cerrado sesion.\nGracias por operar con Cinemar!')
        self.destroy()
        self.ventana_padre.deiconify()
    
    def mostrar_perfil(self):
        pass

    def mostrar_peliculas(self):
        pass

    def mostrar_salas(self):
        pass

    def mostrar_funciones(self):
        pass

    def mostrar_reservas(self):
        pass

    def list_salas(self):
        """FRAMES"""    ### NO ESTÁ TERMINADO ###
        #Tabla
        f_tabla = tk.Frame(self.f_sala)
        f_tabla.config()
        f_tabla.grid(row = 0, column = 0)


        tabla = ttk.Treeview(self.f_tabla, columns = (1,2))
        tabla.column('#0', width = 70, anchor = 'center')
        tabla.heading('#0', text = 'ID_Sala')

        tabla.column('#1', width = 160, anchor = 'center')
        tabla.heading('#1', text = 'Cantidad de Butacas')

        tabla.column('#2', width = 70, anchor = 'center')
        tabla.heading('#2', text = 'Tipo')

        tabla.grid(row = 1, column = 0, columnspan = 4, pady = 20, padx = 20)