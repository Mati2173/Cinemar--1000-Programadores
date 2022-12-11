from SQL import databases as db

class Funcion:
    def __init__ (self,id,pelicula,horario,precio):
        self.id = id
        self.pelicula = pelicula
        self.horario = horario
        self.precio = precio
        
    @property
    def id(self):
        return self.id

    @id.setter
    def id(self,id):
        self.id = id

    @property
    def pelicula(self):
        return self.pelicula

    @pelicula.setter
    def pelicula(self,pelicula):
        self.pelicula = pelicula


    @property
    def horario(self):
        return self.horario

    @horario.setter
    def horario(self,horario):
        self.horario = horario
        
    @property
    def precio(self):
        return self.precio

    @precio.setter
    def precio(self,precio):
        self.precio = precio
        
    def __str__(self):
        f"{self.id} {self.pelicula} {self.horario} {self.precio}"
        

    def agregarDbFunciones(conn, id_funcion, id_Pelicula, horario, precio): 
        connection = conn
        with connection.cursor() as cursor:
            consulta = "INSERT INTO funciones (pelicula, horario, precio) VALUES (%s, %s, %s, %s);"
            cursor.execute(consulta, (id_Pelicula, horario, precio))
            connection.commit()
            connection.close()
        print("Función agregada correctamente")
        
    def eliminarBdfuncion(conn, id_funcion, id_Pelicula, horario, precio):
        connection = conn
        with connection.cursor() as cursor:
             consulta = "DELETE FROM funciones WHERE(id)"
             cursor.execute(consulta, (id_funcion, id_Pelicula, horario, precio))
             connection.commit()
             connection.close()
        print("Función Eliminada")