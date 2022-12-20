import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
from Clases.Funcion import Funcion
from Clases.Ticket import Ticket
from Clases.Descuento import Descuento
from SQL import databases as db

class FormReserva(Toplevel):
    def __init__(self, master = None, comprador = None, pelicula = None, base_datos = None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('500x650')
        self.config(bg = '#056595')
        self.title('Realiza tu Reserva')
        self.iconbitmap('GUI\Assets\Pochoclos.ico')
        self.protocol('WM_DELETE_WINDOW', self.Cancelar)
        self.resizable(0,0)

        self.bdd = base_datos
        self.comprador = comprador
        self.pelicula = pelicula
        self.funcion = Funcion()
        self.all_funciones = self.funcion.mostrar_por_pelicula(self.bdd, self.pelicula)
        self.ticket = Ticket()
        
        """FRAMES"""
        self.F_cab = tk.Frame(self)     #Cabecera
        self.F_datos = tk.Frame(self)   #Datos de la Reserva
        self.F_boton = tk.Frame(self)   #Botones
        
        """WIDGETS"""
        #Titulo
        self.Cab_principal = ttk.Label(self.F_cab)
        #Comprador
        self.Compr_label = ttk.Label(self.F_datos)
        self.Compr_input = ttk.Entry(self.F_datos)
        #Pelicula
        self.Peli_label = ttk.Label(self.F_datos)
        self.Peli_input = ttk.Entry(self.F_datos)
        #Fecha
        self.Fecha_label = ttk.Label(self.F_datos)
        self.Fecha_input = ttk.Combobox(self.F_datos)
        #Horario
        self.Hora_label = ttk.Label(self.F_datos)
        self.Hora_input = ttk.Combobox(self.F_datos)
        #Butacas Seleccionadas
        self.Butac_label = ttk.Label(self.F_datos)
        self.Butac_input = ttk.Combobox(self.F_datos)
        #Precio
        self.Precio_label = ttk.Label(self.F_datos)
        self.Precio_entry = ttk.Entry(self.F_datos)
        #Descuento
        self.Desc_label = ttk.Label(self.F_datos)
        self.Desc_input = ttk.Entry(self.F_datos)
        #Botones
        self.Reservar_bott = ttk.Button(self.F_boton)
        self.Cancelar_bott = ttk.Button(self.F_boton)

        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()



    def frames_config(self):
        self.F_cab.config(border = 15, bg = '#002B40')
        self.F_datos.config(bg = '#056595')
        self.F_boton.config(bg = '#056595')
    
    def widgets_config(self):
        self.input_insert()
        #Titulo
        self.Cab_principal.config(text = 'Completá los datos y reservá\ntu entrada', foreground = '#FFFFFF', font = ('Segoe UI Black', 25), background = '#002B40', justify = 'center')
        #Comprador
        self.Compr_label.config(text = 'Comprador', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Compr_input.config(width = 30, state = 'readonly')
        #Pelicula
        self.Peli_label.config(text = 'Pelicula', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Peli_input.config(width = 30, state = 'readonly')
        #Fecha
        self.Fecha_label.config(text = 'Fecha', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Fecha_input.config(width = 27, state = 'readonly')
        self.Fecha_input.bind("<<ComboboxSelected>>", self.fecha_selected)
        #Horario
        self.Hora_label.config(text = 'Horario', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Hora_input.config(width = 27, state = 'readonly')
        self.Hora_input.bind("<<ComboboxSelected>>", self.hora_selected)
        #Butacas Seleccionadas
        self.Butac_label.config(text = 'Cantidad de Butacas', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Butac_input.config(width = 27, state = 'readonly')
        self.Butac_input.bind("<<ComboboxSelected>>", self.butac_selected)
        #Precio
        self.Precio_label.config(text = 'Precio ($)', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Precio_entry.config(width = 30, state = 'readonly')
        #Descuento
        self.Desc_label.config(text = 'Descuento (%)', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Desc_input.config(width = 30, state = 'readonly')
        #Botones
        self.Reservar_bott.config(text = 'Reservar', command = self.Reservar)
        self.Cancelar_bott.config(text = 'Cancelar', command = self.Cancelar)

        
    def input_insert(self):
        self.Compr_input.insert(0, self.comprador)
        self.Peli_input.insert(0, self.pelicula)
        self.Desc_input.insert(0, '0')
        self.Precio_entry.insert(0, '0.00')
        self.fecha_fill()
    
    def fecha_fill(self):
        fechas = []
        for i in range(len(self.all_funciones)):
            if self.all_funciones[i][4] not in fechas:
                fechas.append(self.all_funciones[i][4])
        self.Fecha_input.config(values = fechas)
    
    def hora_fill(self, fecha):
        horarios = []
        for i in range(len(self.all_funciones)):
            if self.all_funciones[i][4] == fecha:
                horarios.append(self.all_funciones[i][5])
        self.Hora_input.config(values = horarios)
    
    def butac_fill(self, fecha, hora):
        butacas = []
        for i in range(len(self.all_funciones)):
            if self.all_funciones[i][4] == fecha and self.all_funciones[i][5] == hora:
                cant = self.all_funciones[i][3]
        for i in range(1,cant+1):
            butacas.append(i)
        self.Butac_input.config(values = butacas)

    def precio_fill(self, fecha, hora, butac):
        i = 0
        while self.all_funciones[i][4] != fecha and self.all_funciones[i][5] != hora:
            i += 1
        precio = int(self.all_funciones[i][6]) * int(butac)
        desc = int(self.Desc_input.get())
        precio -= ((desc/100)*precio)
        self.Precio_entry.config(state = 'normal')
        self.Precio_entry.delete(0, 'end')
        self.Precio_entry.insert(0, f'{precio}')
        self.Precio_entry.config(state = 'readonly')

    def descuento_fill(self):
        desc = Descuento().aplica_descuento(self.bdd, self.comprador, self.Fecha_input.get())
        if desc > 0:
            messagebox.showinfo('Recompensa', f'Felicidades!\n\nPor venir al cine más de 5 veces en 3 meses, tenés como recompensa un descuento en tus entradas ({desc}%)\n\nGracias por elegirnos!')
        self.Desc_input.config(state = 'normal')
        self.Desc_input.delete(0, 'end')
        self.Desc_input.insert(0, f'{desc}')
        self.Desc_input.config(state = 'readonly')

    def fecha_selected(self, event):
        opc = self.Fecha_input.get()
        self.hora_fill(opc)
    
    def hora_selected(self, event):
        opc = self.Hora_input.get()
        self.butac_fill(self.Fecha_input.get(), opc)
    
    def butac_selected(self, event):
        opc = self.Butac_input.get()
        self.descuento_fill()
        self.precio_fill(self.Fecha_input.get(), self.Hora_input.get(), opc)

    def frames_grid(self):
        self.F_cab.grid(row = 0, column = 0, rowspan = 2, columnspan = 3)
        self.F_datos.grid(row = 2, column = 0, rowspan = 7, columnspan = 3, pady = 20)
        self.F_boton.grid(row = 9, column = 0, columnspan = 3)

    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0, ipady = 10)
        #Comprador
        self.Compr_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.Compr_input.grid(row = 0, column = 1, padx = 10, pady = 10)
        #Pelicula
        self.Peli_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.Peli_input.grid(row = 1, column = 1, padx = 10, pady = 10)
        #Fecha
        self.Fecha_label.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.Fecha_input.grid(row = 2, column = 1, padx = 10, pady = 10)
        #Horario
        self.Hora_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.Hora_input.grid(row = 3, column = 1, padx = 10, pady = 10)
        #Butacas Seleccionadas
        self.Butac_label.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.Butac_input.grid(row = 4, column = 1, padx = 10, pady = 10)
        #Precio
        self.Precio_label.grid(row = 5, column = 0, padx = 10, pady = 10)
        self.Precio_entry.grid(row = 5, column = 1, padx = 10, pady = 10)
        #Descuento
        self.Desc_label.grid(row = 6, column = 0, padx = 10, pady = 10)
        self.Desc_input.grid(row = 6, column = 1, padx = 10, pady = 10)
        #Botones
        self.Reservar_bott.grid(row = 0, column = 0, padx = 20, pady = 10, ipadx = 5, ipady = 5)
        self.Cancelar_bott.grid(row = 0, column = 2, padx = 20, pady = 10, ipadx = 5, ipady = 5)
        
    def Reservar(self):
        comp = self.Compr_input.get()
        peli = self.Peli_input.get()
        butac = self.Butac_input.get()
        fecha = self.Fecha_input.get()
        hora = self.Hora_input.get()
        precio = self.Precio_entry.get()

        if len(butac) > 0 and len(fecha) > 0 and len(hora) > 0:
            i = 0
            while i < len(self.all_funciones):
                if self.all_funciones[i][4] == fecha and self.all_funciones[i][5] == hora:
                    break
                i += 1
            funcion = self.all_funciones[i]
            self.funcion.modificar_funcion(self.bdd, funcion[0], butacas_libres = int(funcion[3]) - int(butac))
            self.ticket = Ticket(comp, peli, butac, fecha, hora, precio)
            self.ticket.cargar_ticket(self.bdd)
            messagebox.showinfo('Aviso', 'Reserva realizada exitosamente!')
            self.master.F_reserva.fill_Tickets()
            self.Cancelar()
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')

    def Cancelar(self):
        self.destroy()
        self.master.deiconify()