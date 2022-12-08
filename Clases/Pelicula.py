class Pelicula:
    def __init__ (self,id,nombre,duracion,genero,tipo,director,actores,sinopsis):
        self.__id = id
        self.__nombre = nombre
        self.__duracion = duracion
        self.__genero = genero
        self.__tipo = tipo
        self.__director = director
        self.__actores = actores
        self.__sinopsis = sinopsis
        
    @property
    def id (self):
        return self.__id

    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def nombre (self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre


    @property
    def duracion (self):
        return self.__duracion

    @duracion.setter
    def duracion(self,duracion):
        self.__duracion = duracion
        
    @property
    def genero (self):
        return self.__genero

    @genero.setter
    def genero(self,genero):
        self.__genero = genero
        
    @property
    def tipo (self):
        return self.__tipo

    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo
        
    @property
    def director (self):
        return self.__director

    @director.setter
    def director(self,director):
        self.__director = director
        
    @property
    def actores (self):
        return self.__actores

    @actores.setter
    def actores(self,actores):
        self.__actores = actores
        
    @property
    def sinopsis(self):
        return self.__sinopsis

    @sinopsis.setter
    def sinopsis(self,sinopsis):
        self.__sinopsis = sinopsis


    