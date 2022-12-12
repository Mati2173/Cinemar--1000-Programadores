from sqlite3 import databases as db

class Pelicula():
    def __init__ (self,id,nombre,duracion,genero,tipo,director,actores,sinopsis):
        self.id = id
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        self.tipo = tipo
        self.director = director
        self.actores = actores
        self.sinopsis = sinopsis
        
    @property
    def id(self):
        return self.id

    @id.setter
    def id(self,id):
        self.id = id

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self,nombre):
        self.nombre = nombre


    @property
    def duracion(self):
        return self.duracion

    @duracion.setter
    def duracion(self,duracion):
        self.duracion = duracion
        
    @property
    def genero(self):
        return self.genero

    @genero.setter
    def genero(self,genero):
        self.genero = genero
        
    @property
    def tipo(self):
        return self.tipo

    @tipo.setter
    def tipo(self,tipo):
        self.tipo = tipo
        
    @property
    def director(self):
        return self.director

    @director.setter
    def director(self,director):
        self.director = director
        
    @property
    def actores(self):
        return self.actores

    @actores.setter
    def actores(self,actores):
        self.actores = actores
        
    @property
    def sinopsis(self):
        return self.sinopsis

    @sinopsis.setter
    def sinopsis(self,sinopsis):
        self.sinopsis = sinopsis

    def __str__(self):
        return f"{self.id} {self.nombre} {self.duracion} {self.genero} {self.tipo} {self.director} {self.actores} {self.sinopsis}"
    
    def agregar_pelicula():
        print("Ingrese el nombre de la Pelicula: ")
        nombre = input()
        print("Ingrese la duracion de la pelicula: ")
        duracion = input()
        print("Ingrese el genero de la pelicula: ")
        genero = input()
        print("Ingrese el tipo de la pelicula: ")
        tipo = input()
        print("Ingrese el director de la pelicula: ")
        director = input()
        print("Ingrese los actores de la pelicula: ")
        actores = input()
        while actores != 0:
            print("Si no desea agregar más actores ingrese 0 :")
            print("Ingrese los actores de la pelicula: ")
            actores = input()
        print("Ingrese la sipnosis de la pelicula: ")
        sinopsis =  input()
      

    def agregarDbPelicula(conn, nombre, duracion, genero, tipo, director,actores,sinopsis):
        connection = conn
        with connection.cursor() as cursor:
             consulta = "INSERT INTO peliculas (nombre, duracion, genero, tipo, director,actores,sinopsis) VALUES (%s, %s, %s, %s, %s, %s,%s);"
             cursor.execute(consulta, (nombre, duracion, genero, tipo, director,actores,sinopsis))
             connection.commit()
             connection.close()
        print("Pelicula Agregada")
        
    def eliminarDbpelicula(conn, nombre, duracion, genero, tipo, director,actores,sinopsis):
        connection = conn
        with connection.cursor() as cursor:
             consulta = "DELETE FROM Peliculas WHERE(id)"
             cursor.execute(consulta, (nombre, duracion, genero, tipo, director,actores,sinopsis))
             connection.commit()
             connection.close()
        print("Pelicula Eliminada")
        
        