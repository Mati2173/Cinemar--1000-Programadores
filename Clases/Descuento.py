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
    
    def mostrar_desc(self, bdd):
        lista=[]
        desc = bdd.select_all('descuentos','id_descuento,dia,porcentaje')
        for i in range(len(desc)):
            lista.append(desc[i])
        return lista