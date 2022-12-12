from SQL import databases as db

class Descuento:
    def __init__ (self,id=0,dia="",porcentaje=0):
        self.id = id
        self.dia = dia
        self.porcentaje = porcentaje

    def __str__(self):
        return f"{self.id} {self.dia} {self.porcentaje}"
    
    def modificar_desc(self,bdd,dia,porcentaje):
        bdd.update('descuentos', 'porcentaje', f'"{porcentaje}"', f"dia = '{dia}'")