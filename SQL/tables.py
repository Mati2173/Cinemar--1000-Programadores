import databases as db

cm = db.DataBase("cinemar.db")

cm.insert("peliculas","nombre,duracion,genero,tipo,director,actores,sinopsis","'Black Adam','170','Acción','3','Jaume Collet-Serra','Dwayne Johnson, Sarah Shahi, Pierce Brosnan, Viola Davis, Aldis Hodge, Noah Centineo, Chico Kenzari, Quintessa Swindell, Uli Latukefu, Bodhi Sabongui, Mo Amer, Tang Nguyen, Joseph Gatt, Angel Rosario Jr., Chaim Girafi, Jalon Christian, Cameron Moir, Rahiem Riley, Tre Ryan, Stephan Jones, Donny Carrington, D.J. Stavropoulos, Odelya Halevi, Natalie Burn','Casi 5.000 años después de haber sido dotado de los poderes omnipotentes de los antiguos dioses - y encarcelado con la misma rapidez -, Black Adam (Johnson) es liberado de su tumba terrenal, listo para desatar su forma única de justicia en el mundo moderno.'")

cm.close()