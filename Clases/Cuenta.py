from SQL import databases as db
from Clases.Persona import Persona
import csv

class Cuenta(Persona):
    def __init__(self, apellido = '', nombre = '', dni = '', email = '', telefono = 0, id = None, usuario = '', password = '', admin = 1):
        Persona.__init__(self, apellido, nombre, dni, email, telefono, id)
        self.usuario = usuario
        self.password = password
        self.admin = admin
    
    def usuario_setter(self, bdd):
        usuario = input('\nNombre de usuario: ')
        if bdd.count('cuentas', 'usuario', f'usuario = "{usuario}"') == 1:
            print('\nNombre de usuario ya existente!')
            self.usuario_setter(bdd)
        else:
            self.usuario = usuario
    
    def password_setter(self):
        self.password = input('\nContraseña: ')

    def cargar_cuenta(self, bdd):
        Persona.cargar_persona(self, bdd)
        bdd.insert('cuentas',
                'usuario, password, admin',
                f'"{self.usuario}", "{self.password}", {self.admin}')
    
    def registrarse(self, bdd):
        Persona.crear_persona(self, bdd)
        self.usuario_setter(bdd)
        self.password_setter()

        self.cargar_cuenta(bdd)
        print('\nCuenta Registrada Exitosamente!')
    
    def iniciar_sesion(self, bdd, username, password):
        user = bdd.select('cuentas', 'id_cuenta, usuario, password, admin', f'usuario = "{username}"')
        if user != None:
            if user[2] == password:
                per = bdd.select('personas', 'id_persona, apellido, nombre, dni, email, telefono', f'id_persona = "{user[0]}"')
                Cuenta.__init__(self,per[1], per[2], per[3], per[4], per[5], user[0], user[1], user[2], user[3])
                print('\nInicio de Sesión Exitoso!')
                return True
            else:
                print('\nContraseña incorrecta!')
        else:
            print('\nEl usuario ingresado no existe!')
        return False
    
    def cerrar_sesion(self):
        Cuenta.__init__(self)
        print('\nSesión Cerrada Exitosamente!')
    
    def all_usuarios(self, bdd):
        lista = []
        cuentas = bdd.select_all('cuentas', 'usuario, password')
        personas = bdd.select_all('personas', 'id_persona, apellido, nombre, dni, email, telefono')

        for i in range(len(cuentas)):
            cuenta = personas[i] + cuentas[i]
            lista.append(cuenta)
        
        return lista

    def csv_all_usuarios(self, bdd):     
        with open('Cuentas.csv', 'w', newline = '\n') as fichero:
            writer = csv.writer(fichero, delimiter = ',')

            texto = self.all_usuarios(bdd)
            texto.insert(0, ('ID_Persona', 'Apellido', 'Nombre', 'DNI', 'Email', 'Telefono','Nombre de Usuario', 'Contraseña'))

            for cuenta in texto:
                writer.writerow(cuenta)

    def eliminar(self, bdd, id_cuenta):
        bdd.delete('cuentas', f'id_cuenta = {id_cuenta}')
        bdd.delete('personas', f'id_persona = {id_cuenta}')
       
    def modificar(self, bdd, id_cuenta, **datos):
        for clave, valor in datos.items():
            if clave == 'apellido':
                bdd.update('personas', 'apellido', f'"{valor}"', f'id_cuenta = {id_cuenta}')
            elif clave == 'nombre':
                bdd.update('personas', 'nombre', f'"{valor}"', f'id_cuenta = {id_cuenta}')
            elif clave == 'dni':
                bdd.update('personas', 'dni', f'"{valor}"', f'id_cuenta = {id_cuenta}')
            elif clave == 'email':
                bdd.update('personas', 'email', f'"{valor}"', f'id_cuenta = {id_cuenta}')
            elif clave == 'telefono':
                bdd.update('personas', 'telefono', f'"{valor}"', f'id_cuenta = {id_cuenta}')
            elif clave == 'usuario':
                bdd.update('cuentas', 'usuario', f'"{valor}"', f'id_cuenta = {id_cuenta}')
            elif clave == 'password':
                bdd.update('cuentas', 'password', f'"{valor}"', f'id_cuenta = {id_cuenta}')
            elif clave == 'admin':
                bdd.update('cuentas', 'admin', f'"{valor}"', f'id_cuenta = {id_cuenta}')
    
    def __str__(self):
        if self.admin == 1:
            cuenta = '\nCuenta: Cliente'
        else:
            cuenta = '\nCuenta: Administrador'
        cuenta += Persona.__str__(self)
        cuenta += f'\nNombre de usuario: {self.usuario}\tContraseña: {self.password}'
        return cuenta


# Path: Sql\main.py
if __name__ == '__main__':
    bdd = db.DataBase('cinemar.db')
    usuario = Cuenta()

    usuario.registrarse(bdd)

    bdd.close()