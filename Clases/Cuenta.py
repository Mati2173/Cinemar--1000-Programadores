from SQL import databases as db
from Clases.Persona import Persona
import csv

class Cuenta(Persona):
    def __init__(self, id = None, apellido = '', nombre = '', dni = '', email = '', telefono = 0,  usuario = '', password = '', admin = 1):
        Persona.__init__(self, apellido, nombre, dni, email, telefono, id)
        self.usuario = usuario
        self.password = password
        self.admin = admin
    
    def usuario_setter(self, bdd, usuario):
        if bdd.count('cuentas', 'usuario', f'usuario = "{usuario}"') == 1:
            return '\nNombre de usuario ya existente!'
        else:
            self.usuario = usuario
            return ''
    
    def password_setter(self, passw):
        self.password = passw

    def cargar_cuenta(self, bdd):
        Persona.cargar_persona(self, bdd)
        bdd.insert('cuentas', 'usuario, password, admin', f'"{self.usuario}", "{self.password}", {self.admin}')
    
    def registrarse(self, bdd, apellido, nombre, dni, email, telefono, usuario, passw):
        mensaje = ''
        mensaje += Persona.crear_persona(self, bdd, apellido, nombre, dni, email, telefono)
        mensaje += self.usuario_setter(bdd, usuario)
        self.password_setter(passw)

        if len(mensaje) == 0:
            self.cargar_cuenta(bdd)
            return 'Cuenta Registrada Exitosamente!'
        else:
            return 'Registro Fallido.' + mensaje
    
    def iniciar_sesion(self, bdd, username, password):
        user = bdd.select('cuentas', 'id_cuenta, usuario, password, admin', f'usuario = "{username}"')
        if user != None:
            if user[2] == password:
                #cuenta = bdd.select('personas', 'id_persona, apellido, nombre, dni, email, telefono', f'id_persona = "{user[0]}"') + user
                #Cuenta.__init__(self, cuenta[0], cuenta[1], cuenta[2], cuenta[3], cuenta[4], cuenta[5], cuenta[7], cuenta[8], cuenta[9])
                return 'Inicio de Sesión Exitoso!'
            else:
                return 'Contraseña incorrecta!'
        else:
            return 'El usuario ingresado no existe!'
    
    #def cerrar_sesion(self):
        #Cuenta.__init__(self)
        #print('\nSesión Cerrada Exitosamente!')
    
    def all_cuentas(self, bdd):
        lista = []
        cuentas = bdd.select_all('cuentas', 'usuario, password')
        personas = bdd.select_all('personas', 'id_persona, apellido, nombre, dni, email, telefono')

        for i in range(len(cuentas)):
            cuenta = personas[i] + cuentas[i]
            lista.append(cuenta)
        
        return lista

    def csv_all_cuentas(self, bdd):     
        with open('Cuentas.csv', 'w', newline = '\n') as fichero:
            writer = csv.writer(fichero, delimiter = ',')

            texto = self.all_usuarios(bdd)
            texto.insert(0, ('ID_Persona', 'Apellido', 'Nombre', 'DNI', 'Email', 'Telefono','Nombre de Usuario', 'Contraseña'))

            for cuenta in texto:
                writer.writerow(cuenta)

    def eliminar_cuenta(self, bdd, id_cuenta):
        Persona.eliminar(self, bdd, id_cuenta)
        bdd.delete('cuentas', f'id_cuenta = {id_cuenta}')
       
    def modificar_cuenta(self, bdd, id_cuenta, **datos):
        for clave, valor in datos.items():
            if clave == 'apellido':
                Persona.modificar_persona(self, bdd, id_cuenta, apellido = valor)
            elif clave == 'nombre':
                Persona.modificar_persona(self, bdd, id_cuenta, nombre = valor)
            elif clave == 'dni':
                Persona.modificar_persona(self, bdd, id_cuenta, dni = valor)
            elif clave == 'email':
                Persona.modificar_persona(self, bdd, id_cuenta, email = valor)
            elif clave == 'telefono':
                Persona.modificar_persona(self, bdd, id_cuenta, telefono = valor)
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