from SQL import databases as db

class Persona():
    def __init__(self, apellido = '', nombre = '', dni = '', email = '', telefono = 0, id = None):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.telefono = telefono
        self.id = id
    
    def apellido_setter(self):
        ap = input('\nApellido/s: ')
        self.apellido = ap.title()
    
    def nombre_setter(self):
        nm = input('\nNombre/s: ')
        self.nombre = nm.title()
    
    def dni_setter(self, bdd):
        try:
            dni = int(input('\nDNI: '))
        except:
            print('\nDNI no válido!')
            self.dni_setter(bdd)
        else:
            if bdd.count('personas', 'dni', f'dni = "{dni}"') == 1:
                print('\nDNI ya registrado!')
                self.dni_setter(bdd)
            else:
                self.dni = dni

    def email_setter(self, bdd):
        email = input('\nCorreo Electrónico: ')
        if bdd.count('personas', 'email', f'email = "{email}"') == 1:
            print('\nCorreo Electrónico ya registrado!')
            self.email_setter(bdd)
        else:
            self.email = email

    def telefono_setter(self, bdd):
        try:
            telefono = int(input('\nNumero de Telefono: '))
        except:
            print('\nNúmero de telefono no válido!')
            self.telefono_setter(bdd)
        else:
            if bdd.count('personas', 'telefono', f'telefono = "{telefono}"') == 1:
                print('\nNúmero ya registrado!')
                self.telefono_setter(bdd)
            else:
                self.telefono = telefono
    
    def crear_persona(self, bdd):
        print('Ingrese sus datos:')
        self.apellido_setter()
        self.nombre_setter()
        self.dni_setter(bdd)
        self.email_setter(bdd)
        self.telefono_setter(bdd)
    
    def cargar_persona(self, bdd):
        bdd.insert('personas',
                    'nombre, apellido, dni, email, telefono', 
                    f'"{self.nombre}", "{self.apellido}", "{self.dni}", "{self.email}", {self.telefono}')
    
    def __str__(self):
        persona = f'\nDNI: {self.dni}\tApellido y nombre: {self.apellido.upper()}, {self.nombre}'
        persona += f'\nTelefono: {self.telefono}\tCorreo Electrónico: {self.email}'
        return persona