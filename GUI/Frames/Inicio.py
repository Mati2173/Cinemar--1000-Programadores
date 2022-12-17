import tkinter as tk

class Inicio(tk.Frame):
    def __init__(self, master = None, admin = 0):
        tk.Frame.__init__(self, master)
        self.master = master

        if admin == 1:
            self.img_Bienvenido = tk.PhotoImage(file = "GUI\Assets\HomeCli.png")
        else:
            self.img_Bienvenido = tk.PhotoImage(file = "GUI\Assets\HomeAdm.png")
        
        """WIDGETS"""
        self.Inicio_label = tk.Label(self)

        self.widgets_config()
        self.widgets_grid()



    def widgets_config(self):
        self.Inicio_label.config(image = self.img_Bienvenido, border = 0)
    
    def widgets_grid(self):
        self.Inicio_label.grid(row = 0, column = 0, columnspan = 8)