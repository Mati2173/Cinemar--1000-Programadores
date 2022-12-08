class Sala:
    def __init__ (self,id,cantidaddebutacas,tipo,funciones):
        self.__id = id
        self.__cantidaddebutacas = cantidaddebutacas
        self.__tipo = tipo
        self.__funciones = funciones
        
    @property
    def id (self):
        return self.__id

    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def cantidaddebutacas (self):
        return self.__cantidaddebutacas

    @cantidaddebutacas.setter
    def cantidaddebutacas(self,cantidaddebutacas):
        self.__cantidaddebutacas = cantidaddebutacas


    @property
    def tipo (self):
        return self.__tipo

    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo
        
    @property
    def funciones (self):
        return self.__funciones

    @funciones.setter
    def funciones(self,funciones):
        self.__funciones = funciones