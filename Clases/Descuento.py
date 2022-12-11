class Descuento:
    def __init__ (self,id,dia,porcentaje):
        self.id = id
        self.dia = dia
        self.porcentaje = porcentaje

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self,id):
        self.id = id

    @property
    def dia(self):
        return self.dia

    @dia.setter
    def dia(self,dia):
        self.dia = dia


    @property
    def porcentaje(self):
        return self.porcentaje

    @porcentaje.setter
    def porcentaje(self,porcentaje):
        self.porcentaje = porcentaje

    def __str__(self):
        return f"{self.id} {self.dia} {self.porcentaje}"
    
    def modificar_desc(self,bdd,dia,porcentaje,datos**):
        for clave, valor in datos.items():
            if clave == 'dia':
                bdd.update('descuento', 'dia', f'"{valor}"', f'id_descuento = {dia}')
            elif clave == 'dia':
                bdd.update('descuento', 'descuento', f'"{valor}"', f'id_descuento = {porcentaje}')