class Descuento:
    def __init__ (self,id,dia,porcentaje):
        self.__id = id
        self.__dia = dia
        self.__porcentaje = porcentaje

    @property
    def id (self):
        return self.__id

    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def dia (self):
        return self.__dia

    @dia.setter
    def dia(self,dia):
        self.__dia = dia


    @property
    def porcentaje (self):
        return self.__porcentaje

    @porcentaje.setter
    def porcentaje(self,porcentaje):
        self.__porcentaje = porcentaje


    