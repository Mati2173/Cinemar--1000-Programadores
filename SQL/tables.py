import databases as db

cm = db.DataBase("cinemar.db")

cm.create_table("personas",
                "id_persona INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "nombre TEXT(20),"+
                "apellido TEXT(20),"+
                "dni TEXT(8),"+
                "email TEXT(35),"+
                "telefono INTEGER"
                )

cm.create_table("cuentas",
                "id_cuenta INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "usuario TEXT(20),"+
                "password TEXT(20),"+
                "admin INTEGER(1) DEFAULT 1,"+
                "FOREIGN KEY(id_cuenta) REFERENCES personas(id_persona)")

cm.create_table("peliculas",
                "id_pelicula INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "nombre TEXT(20),"+
                "duracion INTEGER,"+
                "genero TEXT(20),"+
                "tipo INTEGER(1),"+ #2 (2D) O 3 (3D)
                "director TEXT(50),"+
                "actores TEXT(200),"+
                "sinopsis TEXT(500)") 

cm.create_table("funciones",
                "id_funcion INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "butacas_libres INTEGER,"+
                "pelicula INTEGER,"+
                "horario TEXT(8),"+ #HH:MM:SS   
                "precio REAL,"+
                "FOREIGN KEY(pelicula) REFERENCES peliculas(id_pelicula)")

cm.create_table("salas",
                "id_sala INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "cant_butacas INTEGER,"+
                "tipo INTEGER(1),"+ #2 (2D) O 3 (3D))
                "funcion INTEGER,"+
                "FOREIGN KEY(funcion) REFERENCES funciones(id_funcion)")

cm.create_table("tickets",
                "id_ticket INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "comprador INTEGER,"+
                "pelicula INTEGER,"+
                "cant_butacas INTEGER,"+
                "fecha TEXT(10),"+  #YYYY-MM-DD
                "horario TEXT(8),"+ #HH:MM:SS   
                "precio REAL,"+
                "FOREIGN KEY(pelicula) REFERENCES peliculas(id_pelicula),"+
                "FOREIGN KEY(comprador) REFERENCES personas(id_persona)")

cm.create_table("descuentos",
                "id_descuento INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "dia TEXT(10),"+
                "porcentaje INTEGER(3) DEFAULT 0")
cm.close()