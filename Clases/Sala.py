from SQL import databases as db

class Sala:
    def __init__ (self,id,cantidaddebutacas,tipo,funciones):
        self.id = id
        self.cantidaddebutacas = cantidaddebutacas
        self.tipo = tipo
        self.funciones = funciones
        
    @property
    def id (self):
        return self.id

    @id.setter
    def id(self,id):
        self.id = id

    @property
    def cantidaddebutacas (self):
        return self.cantidaddebutacas

    @cantidaddebutacas.setter
    def cantidaddebutacas(self,cantidaddebutacas):
        self.cantidaddebutacas = cantidaddebutacas


    @property
    def tipo (self):
        return self.tipo

    @tipo.setter
    def tipo(self,tipo):
        self.tipo = tipo
        
    @property
    def funciones (self):
        return self.funciones

    @funciones.setter
    def funciones(self,funciones):
        self.funciones = funciones
        
    def __str__(self):
        return f"{self.cantidaddebutacas} {self.tipo} {self.funciones}"
    
        
    def mostrar_lista(self):
        return [self.id, self.cantidaddebutacas, self.tipo, self.funciones]
    
