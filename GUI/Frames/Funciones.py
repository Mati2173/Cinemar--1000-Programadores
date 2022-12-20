import tkinter as tk
from tkinter import ttk, messagebox
from GUI.Formularios.Funcion import FormFuncion, EditFuncion
from Clases.Funcion import Funcion

class FuncionAdm(tk.Frame):
    def __init__(self, ventana_padre = None, master = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.ventana_padre = ventana_padre
        self.bdd = base_datos
        self.funcion = Funcion()

        """WIDGETS"""
        #Titulo
        self.Cab_principal = ttk.Label(self)
        #Tabla
        self.Tabla = ttk.Treeview(self)
        #Editar
        self.Edit_label = ttk.Label(self)
        self.Edit_input = ttk.Combobox(self)
        self.Edit_bott = ttk.Button(self)
        #Añadir
        self.Add_label = ttk.Label(self)
        self.Add_bott = ttk.Button(self)
        #Eliminar
        self.Elim_label = ttk.Label(self)
        self.Elim_input = ttk.Combobox(self)
        self.Elim_bott = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()
        self.input_fill()



    def Tabla_config(self):
        self.Tabla.config(columns = (1,2,3,4,5,6))
        self.Tabla.column('#0', width = 70, anchor = 'center')
        self.Tabla.heading('#0', text = 'ID Función', anchor = 'center')
        self.Tabla.column('#1', width = 70, anchor = 'center')
        self.Tabla.heading('#1', text = 'Sala', anchor = 'center')
        self.Tabla.column('#2', width = 180, anchor = 'center')
        self.Tabla.heading('#2', text = 'Pelicula', anchor = 'center')
        self.Tabla.column('#3', width = 100, anchor = 'center')
        self.Tabla.heading('#3', text = 'Butacas Libres', anchor = 'center')
        self.Tabla.column('#4', width = 90, anchor = 'center')
        self.Tabla.heading('#4', text = 'Fecha', anchor = 'center')
        self.Tabla.column('#5', width = 70, anchor = 'center')
        self.Tabla.heading('#5', text = 'Horario', anchor = 'center')
        self.Tabla.column('#6', width = 70, anchor = 'center')
        self.Tabla.heading('#6', text = 'Precio', anchor = 'center')

    def widgets_config(self):
        #Titulo
        self.Cab_principal.config(text = '   Funciones   ', foreground = '#FFFFFF', font = ('Segoe UI Black', 36), background = '#002B40', justify = 'center')
        #Tabla
        self.Tabla_config()
        #Editar
        self.Edit_label.config(text = 'Editar Función', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Edit_input.config(width = 5, state = 'readonly')
        self.Edit_bott.config(text = 'Editar', command = self.Editar)
        #Añadir
        self.Add_label.config(text = 'Agregar Función', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Add_bott.config(text = 'Agregar', command = self.Agregar)
        #Eliminar
        self.Elim_label.config(text = 'Eliminar Función', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Elim_input.config(width = 5, state = 'readonly')
        self.Elim_bott.config(text = 'Eliminar', command = self.Eliminar)

    def input_fill(self):
        self.Tabla.delete(*self.Tabla.get_children())
        funciones = self.funcion.mostrar_funciones(self.bdd)
        ids = []

        for func in funciones:
            self.Tabla.insert('', 'end', text = f'{func[0]}', values = (func[1], func[2], func[3], func[4], func[5], func[6]))
            ids.append(func[0])
        
        self.Edit_input.config(values = ids)
        self.Elim_input.config(values = ids)

    def widgets_grid(self):
        #Titulo
        self.Cab_principal.grid(row = 0, column = 0, columnspan = 8, pady = 20, ipady = 10)
        #Tabla
        self.Tabla.grid(row = 1, column = 0, rowspan = 5, columnspan = 5, padx = 20, pady = (0, 20))
        #Editar
        self.Edit_label.grid(row = 2, column = 5, columnspan = 3)
        self.Edit_input.grid(row = 3, column = 5, columnspan = 2)
        self.Edit_bott.grid(row = 3, column = 7, columnspan = 1)
        #Añadir
        self.Add_label.grid(row = 6, column = 1)
        self.Add_bott.grid(row = 7, column = 1, pady = 10)
        #Eliminar
        self.Elim_label.grid(row = 6, column = 4, columnspan = 2)
        self.Elim_input.grid(row = 7, column = 4)
        self.Elim_bott.grid(row = 7, column = 5, pady = 10)

    def Editar(self):
        func = self.Edit_input.get()
        if len(func) > 0:
            self.Edit_input.set('')
            self.ventana_padre.withdraw()
            ventana = EditFuncion(self.ventana_padre, int(func), self.bdd)
            ventana.mainloop()
        else:
            messagebox.showerror('Error', 'Debe seleccionar una función!')
            
    def Agregar(self):
        self.ventana_padre.withdraw()
        ventana = FormFuncion(self.ventana_padre, self.bdd)
        ventana.mainloop()

    def Eliminar(self):
        func = self.Elim_input.get()
        if len(func) > 0:
            self.funcion.eliminar_funcion(self.bdd, int(func))
            self.input_fill()
            self.Elim_input.set('')
            messagebox.showinfo('Aviso', 'Funcion eliminada exitosamente!')
        else:
            messagebox.showerror('Error', 'Debe seleccionar una función!')