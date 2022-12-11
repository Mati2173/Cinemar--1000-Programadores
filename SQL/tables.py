import databases as db

cm = db.DataBase("cinemar.db")
'''''
cm.create_table("personas",
                "id_persona INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "apellido TEXT(20),"+
                "nombre TEXT(20),"+
                "dni TEXT(8),"+
                "email TEXT(35),"+
                "telefono INTEGER"
                )

cm.create_table("cuentas",
                "id_cuenta INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "usuario TEXT(20),"+
                "password TEXT(20),"+
                "admin INTEGER(1) DEFAULT 1,"+  #CLIENTE: 1 // ADMINISTRADOR: 2
                "FOREIGN KEY(id_cuenta) REFERENCES personas(id_persona)")

cm.create_table("peliculas",
                "id_pelicula INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "nombre TEXT(20),"+
                "duracion INTEGER,"+    #En minutos
                "genero TEXT(20),"+
                "tipo TEXT(2),"+    #(2D o 3D)
                "director TEXT(50),"+
                "actores TEXT(200),"+
                "sinopsis TEXT(500)") 

cm.create_table("funciones",
                "id_funcion INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "sala INTEGER,"+    #ID_Sala
                "pelicula TEXT(20),"+   #Nombre Pelicula
                "butacas_libres INTEGER,"+
                "horario TEXT(8),"+ #Formato --> HH:MM:SS   
                "precio REAL,"+
                "FOREIGN KEY(sala) REFERENCES salas(id_sala),"+
                "FOREIGN KEY(pelicula) REFERENCES peliculas(nombre)")

cm.create_table("salas",
                "id_sala INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "cant_butacas INTEGER,"+
                "tipo TEXT(2)")    #(2D o 3D)

cm.create_table("tickets",
                "id_ticket INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "comprador TEXT(20),"+  #Nombre Cliente
                "pelicula TEXT(20),"+   #Nombre Pelicula
                "cant_butacas INTEGER,"+    #Butacas compradas
                "fecha TEXT(10),"+  #Formato --> YYYY-MM-DD
                "horario TEXT(8),"+ #Formato --> HH:MM:SS   
                "precio REAL,"+
                "FOREIGN KEY(pelicula) REFERENCES peliculas(nombre),"+
                "FOREIGN KEY(comprador) REFERENCES personas(nombre)")

cm.create_table("descuentos",
                "id_descuento INTEGER PRIMARY KEY AUTOINCREMENT,"+  #ID del día
                "dia TEXT(10),"+    #Lunes, Martes, ...
                "porcentaje INTEGER(3) DEFAULT 0")  
'''
cm.insert("descuentos","dia,porcentaje","'Lunes','20'")
cm.insert("descuentos","dia,porcentaje","'Martes','15'")
cm.insert("descuentos","dia,porcentaje","'Miercoles','20'")
cm.insert("descuentos","dia,porcentaje","'Jueves','15'")
cm.insert("descuentos","dia,porcentaje","'Viernes','20'")
cm.insert("descuentos","dia,porcentaje","'Sabado','20'")
cm.insert("descuentos","dia,porcentaje","'Domingo','10'")


cm.close()