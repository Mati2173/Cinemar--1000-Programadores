import tkinter as tk
from tkinter import ttk, messagebox
from Clases.Descuento import Descuento

class DescuentoAdm(tk.Frame):
    def __init__(self, master = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.bdd = base_datos
        self.descuento = Descuento()

        """WIDGETS"""
        #Titulo
        self.Cab_principal = ttk.Label(self)
        #Tabla
        self.Tabla = ttk.Treeview(self)
        #Editar
        self.Edit_label = ttk.Label(self)
        self.Dia_label = ttk.Label(self)
        self.Dia_input = ttk.Combobox(self)
        self.Porc_label = ttk.Label(self)
        self.Porc_input = ttk.Entry(self)
        self.Editar_bott = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()
        self.input_fill()



    def Tabla_config(self):
        self.Tabla.config(columns = (1,2))
        self.Tabla.column('#0', width = 90, anchor = 'center')
        self.Tabla.heading('#0', text = 'ID Descuento')
        self.Tabla.column('#1', width = 120, anchor = 'center')
        self.Tabla.heading('#1', text = 'Dia')
        self.Tabla.column('#2', width = 100, anchor = 'center')
        self.Tabla.heading('#2', text = 'Porcentaje (%)')
    
    def widgets_config(self):
        #Titulo
        self.Cab_principal.config(text = '   Descuentos   ', foreground = '#FFFFFF', font = ('Segoe UI Black', 36), background = '#002B40')
        #Tabla
        self.Tabla_config()
        #Editar
        self.Edit_label.config(text = 'Edita un descuento', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Dia_label.config(text = 'Dia', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Dia_input.config(width = 10, state = 'readonly')
        self.Porc_label.config(text = 'Porcentaje', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Porc_input.config(width = 13)
        self.Editar_bott.config(text = 'Editar', command = self.Editar)

    def input_fill(self):
        self.Tabla.delete(*self.Tabla.get_children())

        descuentos = self.descuento.mostrar_desc(self.bdd)
        dias = []
        for desc in descuentos:
            self.Tabla.insert('', 'end', text = f'{desc[0]}', values = (desc[1], desc[2]))
            dias.append(desc[1])
        
        self.Dia_input.config(values = dias)
    
    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0, column = 0, columnspan = 8, pady = 20, ipady = 10)
        #Tabla
        self.Tabla.grid(row = 1, column = 0, rowspan = 4, columnspan = 5, padx = 60, pady = (0,20))
        #Editar
        self.Edit_label.grid(row = 1, column = 5, columnspan = 2)
        self.Dia_label.grid(row = 2, column = 5)
        self.Dia_input.grid(row = 2, column = 6)
        self.Porc_label.grid(row = 3, column = 5, padx = (0, 10))
        self.Porc_input.grid(row = 3, column = 6)
        self.Editar_bott.grid(row = 4, column = 5, columnspan = 2)

    def Editar(self):
        dia = self.Dia_input.get()
        por = self.Porc_input.get()

        if len(dia) > 0 and len(por) > 0:
            self.descuento.modificar_desc(self.bdd, dia, por)
            self.input_fill()
            self.Porc_input.delete(0, 'end')
            self.Dia_input.set('')
            messagebox.showinfo('Aviso', 'Descuento modificado exitosamente!')
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')