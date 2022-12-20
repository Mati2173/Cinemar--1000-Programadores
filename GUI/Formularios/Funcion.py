import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
from Clases.Funcion import Funcion
from Clases.Pelicula import Pelicula
from Clases.Sala import Sala
from SQL import databases as db

class FormFuncion(Toplevel):
    def __init__(self, master = None, base_datos = None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('358x550')
        self.config(bg = '#056595')
        self.title('Agregar Función')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.protocol('WM_DELETE_WINDOW', self.Cancelar)
        self.resizable(0,0)

        self.bdd = base_datos
        self.funcion = Funcion()
        self.pelicula = Pelicula()
        self.sala = Sala()
        
        """FRAMES"""
        self.F_cab = tk.Frame(self)     #Cabecera
        self.F_datos = tk.Frame(self)   #Datos de la Funcion
        self.F_boton = tk.Frame(self)   #Botones

        """ELEMENTOS"""
        #Titulo
        self.Cab_principal = ttk.Label(self.F_cab)
        #Sala
        self.Sala_label = ttk.Label(self.F_datos)
        self.Sala_input = ttk.Combobox(self.F_datos)
        #Pelicula
        self.Peli_label = ttk.Label(self.F_datos)
        self.Peli_input = ttk.Combobox(self.F_datos)
        #Butacas Disponibles
        self.Butac_label = ttk.Label(self.F_datos)
        self.Butac_input = ttk.Entry(self.F_datos)
        #Fecha
        self.Fecha_label = ttk.Label(self.F_datos)
        self.Fecha_input = ttk.Entry(self.F_datos)
        #Horario
        self.Hora_label = ttk.Label(self.F_datos)
        self.Hora_input = ttk.Entry(self.F_datos)
        #Precio
        self.Precio_label = ttk.Label(self.F_datos)
        self.Precio_input = ttk.Entry(self.F_datos)
        #Botones
        self.Cargar_bott = ttk.Button(self.F_boton)
        self.Cancelar_bott = ttk.Button(self.F_boton)

        self.peli_fill()
        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()



    def frames_config(self):
        self.F_cab.config(border = 15, bg = '#002B40')
        self.F_datos.config(bg = '#056596')
        self.F_boton.config(bg = '#056596')
    
    def widgets_config(self):
        #Titulo
        self.Cab_principal.config(text = 'Ingresá los datos de\nla nueva función', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40', justify = 'center')
        #Sala
        self.Sala_label.config(text = 'Sala', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Sala_input.config(width = 7, state = 'readonly')
        self.Sala_input.bind("<<ComboboxSelected>>", self.sala_selected)
        #Pelicula
        self.Peli_label.config(text = 'Pelicula', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Peli_input.config(width = 27, state = 'readonly')
        self.Peli_input.bind("<<ComboboxSelected>>", self.peli_selected)
        #Butacas Disponibles
        self.Butac_label.config(text = 'Butacas', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Butac_input.config(width = 10, state = 'readonly')
        #Fecha
        self.Fecha_label.config(text = 'Fecha', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Fecha_input.config(width = 30)
        #Horario
        self.Hora_label.config(text = 'Horario', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Hora_input.config(width = 30)
        #Precio
        self.Precio_label.config(text = 'Precio ($)', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Precio_input.config(width = 10)
        #Botones
        self.Cargar_bott.config(text = 'Cargar Datos', command = self.Cargar)
        self.Cancelar_bott.config(text = 'Cancelar', command = self.Cancelar)
    
    def peli_fill(self):
        peli_input = []

        pelis = self.pelicula.mostrar_nombres(self.bdd)
        for i in range(len(pelis)):
            peli_input.append(pelis[i][1])  
        self.Peli_input.config(values = peli_input)
    
    def sala_fill(self):
        pelis = self.pelicula.mostrar_nombres(self.bdd)
        i = 0
        while pelis[i][1] != self.Peli_input.get():
            i += 1
        tipo_peli = pelis[i][2]

        sala_input = []
        salas = self.sala.mostrar_salas(self.bdd)
        for j in range(len(salas)):
            if salas[j][2] == tipo_peli:
                sala_input.append(salas[j][0])
        self.Sala_input.config(values = sala_input)
        
    def sala_selected(self, event):
        opc = self.Sala_input.get()
        salas = self.sala.mostrar_salas(self.bdd)
        i = 0
        while salas[i][0] != int(opc):
            i += 1
        self.Butac_input.config(state = 'normal')
        self.Butac_input.delete(0, 'end')
        self.Butac_input.insert(0, f'{salas[i][1]}')
        self.Butac_input.config(state = 'readonly')
    
    def peli_selected(self, event):
        self.sala_fill()

    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, rowspan = 2, columnspan = 3)
        self.F_datos.grid(row = 2, column = 0, rowspan = 5, columnspan = 3, pady = 20)
        self.F_boton.grid(row = 7, column = 0, columnspan = 3)

    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0, ipady = 10)
        #Sala
        self.Sala_label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.Sala_input.grid(row = 1, column = 2, padx = 10, pady = 10)
        #Pelicula
        self.Peli_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.Peli_input.grid(row = 1, column = 0, padx = 10, pady = 10)
        #Butacas Disponibles
        self.Butac_label.grid(row = 2, column = 2, padx = 10, pady = 10)
        self.Butac_input.grid(row = 3, column = 2, padx = 10, pady = 10)
        #Fecha
        self.Fecha_label.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.Fecha_input.grid(row = 3, column = 0, padx = 10, pady = 10)
        #Horario
        self.Hora_label.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.Hora_input.grid(row = 5, column = 0, padx = 10, pady = 10)
        #Precio
        self.Precio_label.grid(row = 4, column = 2, padx = 10, pady = 10)
        self.Precio_input.grid(row = 5, column = 2, padx = 10, pady = 10)
        #Botones
        self.Cargar_bott.grid(row = 0, column = 0, padx = 20, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 0, column = 2, padx = 20, pady = 10, ipadx = 5, ipady = 5)

    def Cargar(self):
        sala = self.Sala_input.get()
        peli = self.Peli_input.get()
        butac = self.Butac_input.get()
        fecha = self.Fecha_input.get()
        hora = self.Hora_input.get()
        precio = self.Precio_input.get()
        if len(sala) > 0 and len(peli) > 0 and len(butac) > 0 and len(fecha) > 0 and len(hora) > 0 and len(precio) > 0:
            self.funcion.crear_funcion(self.bdd, sala, peli, butac, fecha, hora, precio)
            messagebox.showinfo('Aviso', 'Función agregada exitosamente!')
            self.master.F_funcion.input_fill()
            self.Cancelar()
        else:
            messagebox.showerror('Error', 'Debe completar todos los campos!')

    def Cancelar(self):
        self.destroy()
        self.master.deiconify()



class EditFuncion(Toplevel):
    def __init__(self, master = None, id_funcion = None, base_datos = None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('330x550')
        self.config(bg = '#056595')
        self.title('Editar Función')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.protocol('WM_DELETE_WINDOW', self.Cancelar)
        self.resizable(0,0)

        self.bdd = base_datos
        self.funcion = Funcion()
        self.id_funcion = id_funcion
        self.pelicula = Pelicula()
        self.sala = Sala()
        
        """FRAMES"""
        self.F_cab = tk.Frame(self)     #Cabecera
        self.F_datos = tk.Frame(self)   #Datos de la Funcion
        self.F_boton = tk.Frame(self)   #Botones

        """ELEMENTOS"""
        #Titulo
        self.Cab_principal = ttk.Label(self.F_cab)
        #Sala
        self.Sala_label = ttk.Label(self.F_datos)
        self.Sala_input = ttk.Combobox(self.F_datos)
        #Pelicula
        self.Peli_label = ttk.Label(self.F_datos)
        self.Peli_input = ttk.Entry(self.F_datos)
        #Butacas Disponibles
        self.Butac_label = ttk.Label(self.F_datos)
        self.Butac_input = ttk.Entry(self.F_datos)
        #Fecha
        self.Fecha_label = ttk.Label(self.F_datos)
        self.Fecha_input = ttk.Entry(self.F_datos)
        #Horario
        self.Hora_label = ttk.Label(self.F_datos)
        self.Hora_input = ttk.Entry(self.F_datos)
        #Precio
        self.Precio_label = ttk.Label(self.F_datos)
        self.Precio_input = ttk.Entry(self.F_datos)
        #Botones
        self.Editar_bott = ttk.Button(self.F_boton)
        self.Cancelar_bott = ttk.Button(self.F_boton)

        self.input_fill()
        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()



    def frames_config(self):
        self.F_cab.config(border = 15, bg = '#002B40')
        self.F_datos.config(bg = '#056596')
        self.F_boton.config(bg = '#056596')
    
    def widgets_config(self):
        #Titulo
        self.Cab_principal.config(text = 'Modificá los datos\nde la función', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40', justify = 'center')
        #Sala
        self.Sala_label.config(text = 'Sala', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Sala_input.config(width = 7, state = 'readonly')
        self.Sala_input.bind("<<ComboboxSelected>>", self.combobox_selected)
        #Pelicula
        self.Peli_label.config(text = 'Pelicula', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Peli_input.config(width = 27, state = 'readonly')
        #Butacas Disponibles
        self.Butac_label.config(text = 'Butacas', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Butac_input.config(width = 10, state = 'readonly')
        #Fecha
        self.Fecha_label.config(text = 'Fecha', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Fecha_input.config(width = 27)
        #Horario
        self.Hora_label.config(text = 'Horario', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Hora_input.config(width = 27)
        #Precio
        self.Precio_label.config(text = 'Precio ($)', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Precio_input.config(width = 10)
        #Botones
        self.Editar_bott.config(text = 'Editar Datos', command = self.Editar)
        self.Cancelar_bott.config(text = 'Cancelar', command = self.Cancelar)

    def input_fill(self):
        funciones = self.funcion.mostrar_funciones(self.bdd)
        for func in funciones:
            if func[0] == self.id_funcion:
                self.funcion = Funcion(func[0], func[1], func[2], func[3], func[4], func[5], func[6])

        self.Sala_input.insert(0, f'{self.funcion.sala}')
        self.Peli_input.insert(0, f'{self.funcion.pelicula}')
        self.Butac_input.insert(0, f'{self.funcion.butacas_libres}')
        self.Fecha_input.insert(0, f'{self.funcion.fecha}')
        self.Hora_input.insert(0, f'{self.funcion.horario}')
        self.Precio_input.insert(0, f'{self.funcion.precio}')
        
        pelis = self.pelicula.mostrar_nombres(self.bdd)
        i = 0
        while pelis[i][1] != self.Peli_input.get():
            i += 1
        tipo_peli = pelis[i][2]

        sala_input = []
        salas = self.sala.mostrar_salas(self.bdd)
        for j in range(len(salas)):
            if salas[j][2] == tipo_peli:
                sala_input.append(salas[j][0])
        self.Sala_input.config(values = sala_input)

    def combobox_selected(self, event):
        opc = self.Sala_input.get()
        salas = self.sala.mostrar_salas(self.bdd)
        i = 0
        while salas[i][0] != int(opc):
            i += 1
        self.Butac_input.config(state = 'normal')
        self.Butac_input.delete(0, 'end')
        self.Butac_input.insert(0, f'{salas[i][1]}')
        self.Butac_input.config(state = 'readonly')

    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, rowspan = 2, columnspan = 3)
        self.F_datos.grid(row = 2, column = 0, rowspan = 5, columnspan = 3, pady = 20)
        self.F_boton.grid(row = 7, column = 0, columnspan = 3)

    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0, ipady = 10)
        #Sala
        self.Sala_label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.Sala_input.grid(row = 1, column = 2, padx = 10, pady = 10)
        #Pelicula
        self.Peli_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.Peli_input.grid(row = 1, column = 0, padx = 10, pady = 10)
        #Butacas Disponibles
        self.Butac_label.grid(row = 2, column = 2, padx = 10, pady = 10)
        self.Butac_input.grid(row = 3, column = 2, padx = 10, pady = 10)
        #Fecha
        self.Fecha_label.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.Fecha_input.grid(row = 3, column = 0, padx = 10, pady = 10)
        #Horario
        self.Hora_label.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.Hora_input.grid(row = 5, column = 0, padx = 10, pady = 10)
        #Precio
        self.Precio_label.grid(row = 4, column = 2, padx = 10, pady = 10)
        self.Precio_input.grid(row = 5, column = 2, padx = 10, pady = 10)
        #Botones
        self.Editar_bott.grid(row = 0, column = 0, padx = 20, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 0, column = 2, padx = 20, pady = 10, ipadx = 5, ipady = 5)
    
    def Editar(self):
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, sala = self.Sala_input.get())
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, pelicula = self.Peli_input.get())
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, butacas_libres = self.Butac_input.get())
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, fecha = self.Fecha_input.get())
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, horario = self.Hora_input.get())
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, precio = self.Precio_input.get())
        messagebox.showinfo('Aviso', 'Función editada exitosamente!')
        self.master.F_funcion.input_fill()
        self.Cancelar()

    def Cancelar(self):
        self.destroy()
        self.master.deiconify()