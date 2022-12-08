class Funcion:
    def __init__ (self,id,pelicula,horario,precio):
        self.__id = id
        self.__pelicula = pelicula
        self.__horario = horario
        self.__precio = precio
        
    @property
    def id (self):
        return self.__id

    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def pelicula (self):
        return self.__pelicula

    @pelicula.setter
    def pelicula(self,pelicula):
        self.__pelicula = pelicula


    @property
    def horario (self):
        return self.__horario

    @horario.setter
    def horario(self,horario):
        self.__horario = horario
        
    @property
    def precio (self):
        return self.__precio

    @precio.setter
    def precio(self,precio):
        self.__precio = precio