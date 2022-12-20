from SQL import databases as db

class Funcion:
    def __init__ (self,id=0,sala=0,pelicula=" ",butacas_libres=0,fecha=" ",horario=" ",precio=0.0):
        self.id = id
        self.sala = sala
        self.pelicula = pelicula
        self.butacas_libres = butacas_libres
        self.fecha = fecha
        self.horario = horario
        self.precio = precio

    def __str__(self):
        f"{self.id} {self.sala} {self.pelicula} {self.butacas_libres} {self.fecha} {self.horario} {self.precio}"
        
    def crear_funcion(self,bdd ,sala ,pelicula ,butacas_libres ,fecha ,horario ,precio):
        bdd.insert('funciones',
                    'sala,pelicula,butacas_libres,fecha,horario,precio', 
                    f'{sala},"{pelicula}",{butacas_libres},"{fecha}","{horario}",{precio}')
    
    def modificar_funcion(self,bdd,id_funcion,**datos):
        for clave,valor in datos.items():
            if clave == 'sala':
                bdd.update('funciones','sala',f'{valor}',f'id_funcion = {id_funcion}')
            elif clave == 'pelicula':
                bdd.update('funciones','pelicula',f'"{valor}"',f'id_funcion = {id_funcion}')
            elif clave == 'butacas_libres':
                bdd.update('funciones','butacas_libres',f'{valor}',f'id_funcion = {id_funcion}')
            elif clave == 'fecha':
                bdd.update('funciones','fecha',f'"{valor}"',f'id_funcion = {id_funcion}')
            elif clave == 'horario':
                bdd.update('funciones','horario',f'"{valor}"',f'id_funcion = {id_funcion}')
            elif clave == 'precio':
                bdd.update('funciones','precio',f'{valor}',f'id_funcion = {id_funcion}')
    
    def eliminar_funcion(self,bdd,id_funcion):
        bdd.delete('funciones', f'id_funcion = {id_funcion}')
    
    def mostrar_funciones(self, bdd):
        lista=[]
        funcion = bdd.select_all('funciones','id_funcion,sala,pelicula,butacas_libres,fecha,horario,precio')
        for i in range(len(funcion)):
            lista.append(funcion[i])
        return lista

    def mostrar_por_pelicula(self,bdd,peli):
        funciones = self.mostrar_funciones(bdd)
        select = []
        for funcion in funciones:
            if funcion[2] == peli:
                select.append(funcion)
        return select