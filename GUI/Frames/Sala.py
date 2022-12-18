import tkinter as tk
from tkinter import ttk, messagebox
from Clases.Sala import Sala

class SalaAdm(tk.Frame):
    def __init__(self, master = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.bdd = base_datos
        self.sala = Sala()

        """WIDGETS"""
        #Titulo
        self.Cab_principal = ttk.Label(self)
        #Tabla
        self.Tabla = ttk.Treeview(self)
        #Eliminar
        self.Elim_label = ttk.Label(self)
        self.Elim_input = ttk.Combobox(self)
        self.Elim_bott = ttk.Button(self)
        #Añadir
        self.Add_label = ttk.Label(self)
        self.NumSala_label = ttk.Label(self)
        self.NumSala_input = ttk.Entry(self)
        self.Butac_label = ttk.Label(self)
        self.Butac_input = ttk.Entry(self)
        self.Tipo_label = ttk.Label(self)
        self.Tipo_input = ttk.Combobox(self)
        self.Add_bott = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()
        self.input_fill()



    def Tabla_config(self):
        self.Tabla.config(columns = (1,2))
        self.Tabla.column('#0', width = 70, anchor = 'center')
        self.Tabla.heading('#0', text = 'ID Sala')
        self.Tabla.column('#1', width = 160, anchor = 'center')
        self.Tabla.heading('#1', text = 'Cantidad de Butacas')
        self.Tabla.column('#2', width = 70, anchor = 'center')
        self.Tabla.heading('#2', text = 'Tipo')
    
    def input_fill(self):
        self.Tabla.delete(*self.Tabla.get_children())
        salas = self.sala.mostrar_salas(self.bdd)
        id_salas = []

        for sala in salas:
            self.Tabla.insert('', 'end', text = f'{sala[0]}', values = (sala[1], sala[2]))
            id_salas.append(sala[0])
        
        self.Elim_input.config(values = id_salas)
    
    def widgets_config(self):
        #Titulo
        self.Cab_principal.config(text = '     Salas     ', foreground = '#FFFFFF', font = ('Segoe UI Black', 36), background = '#002B40')
        #Tabla
        self.Tabla_config()
        #Eliminar
        self.Elim_label.config(text = 'Elimina una sala', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Elim_input.config(width = 5)
        self.Elim_bott.config(text = 'Eliminar', command = self.Eliminar)
        #Añadir
        self.Add_label.config(text = 'Agregar una nueva sala', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.NumSala_label.config(text = 'Sala', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.NumSala_input.config(width = 6)
        self.Butac_label.config(text = 'Butacas', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Butac_input.config(width = 6)
        self.Tipo_label.config(text = 'Tipo', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Tipo_input.config(width = 3, state = 'readonly', values = ['2D', '3D'])
        self.Add_bott.config(text = 'Agregar', command = self.Agregar)
    
    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0, column = 0, columnspan = 8, pady = 20, ipady = 10)
        #Tabla
        self.Tabla.grid(row = 1, column = 0, rowspan = 4, columnspan = 5, padx = 60, pady = (0, 20))
        #Eliminar
        self.Elim_label.grid(row =  2, column = 5, columnspan = 3)
        self.Elim_input.grid(row = 3, column = 5)
        self.Elim_bott.grid(row = 3, column = 7)
        #Añadir
        self.Add_label.grid(row = 5, column = 0, columnspan = 8, pady = 10)
        self.NumSala_label.grid(row = 6, column = 2)
        self.NumSala_input.grid(row = 7, column = 2)
        self.Butac_label.grid(row = 6, column = 3)
        self.Butac_input.grid(row = 7, column = 3)
        self.Tipo_label.grid(row = 6, column = 4)
        self.Tipo_input.grid(row = 7, column = 4)
        self.Add_bott.grid(row = 7, column = 5)

    def Agregar(self):
        id = self.NumSala_input.get()
        butac = self.Butac_input.get()
        tipo = self.Tipo_input.get()

        if len(id) > 0 and len(butac) > 0 and len(tipo) > 0:
            self.sala.cargar_sala(self.bdd, id, butac, tipo)
            self.input_fill()
            self.NumSala_input.delete(0, 'end')
            self.Butac_input.delete(0, 'end')
            self.Tipo_input.set('')
            messagebox.showinfo('Aviso', 'Sala agregada correctamente')
        else:
            messagebox.showinfo('Aviso', 'Debe rellenar todos los campos!')

    def Eliminar(self):
        id = self.Elim_input.get()

        if len(id) > 0:
            self.sala.eliminar_sala(self.bdd, id)
            self.input_fill()
            self.Elim_input.set('')
            messagebox.showinfo('Aviso', 'Sala eliminada correctamente')
        else:
            messagebox.showinfo('Aviso', 'Debe rellenar todos los campos!')