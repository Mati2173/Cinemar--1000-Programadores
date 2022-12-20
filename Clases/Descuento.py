from SQL import databases as db
from Clases.Ticket import Ticket
from datetime import datetime

class Descuento:
    def __init__ (self,id=0,dia="",porcentaje=0):
        self.id = id
        self.dia = dia
        self.porcentaje = porcentaje

    def __str__(self):
        return f"{self.id} {self.dia} {self.porcentaje}"
    
    def modificar_desc(self,bdd,dia,porcentaje):
        bdd.update('descuentos', 'porcentaje', f'"{porcentaje}"', f"dia = '{dia}'")
    
    def mostrar_desc(self, bdd):
        lista=[]
        desc = bdd.select_all('descuentos','id_descuento,dia,porcentaje')
        for i in range(len(desc)):
            lista.append(desc[i])
        return lista
    
    def return_porcentaje(self, bdd, dia):
        desc = self.mostrar_desc(bdd)
        i = 0
        while desc[i][1] != dia:
            i += 1
        return desc[i][2]

    def aplica_descuento(self, bdd, dni, fecha):
        dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        fecha_principal = datetime.strptime(fecha, '%Y-%m-%d')
        fecha = datetime.weekday(fecha_principal)
        descuento = self.return_porcentaje(bdd, dias[fecha])
        if descuento > 0:
            cont = 0
            reservas = Ticket().por_comprador(bdd, dni)
            for res in reservas:
                otra_fecha = datetime.strptime(res[4], '%Y-%m-%d')
                diferencia = fecha_principal - otra_fecha
                if 0 <= diferencia.days <= 90:
                    cont += 1
            if cont >= 6:
                return descuento
            else:
                return 0
        else:
            return 0