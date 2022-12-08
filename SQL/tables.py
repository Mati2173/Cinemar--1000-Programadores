import databases as db

cm = db.DataBase("cinemar.db")

cm.insert("peliculas","nombre,duracion,genero,tipo,director,actores,sinopsis","'Rapidos y furiosos 9','143','Acción','3','Justin Lin','Vin Diesel, Michelle Rodriguez, Jordana Brewster, Tyrese Gibson, Ludacris, John Cena, Charlize Theron, Helen Mirren, Kurt Russell, Sung Kang, Lucas Black, Finn Cole, Vinnie Bennett, Nathalie Emmanuel, Martyn Ford, Alexander Wraith, Bow Wow, Michael Rooker, Cardi B, Don Omar, Ozuna, Bad Bunny, JD Pardo, Anna Sawai, Thue Ersted Rasmussen, Shea Whigham, Jim Parrack, Igby Rigney, Siena Agudong, Jason Statham, Sophia Bui, Amber Sienna','Dom Toretto vive una vida tranquila junto a Letty y su hijo, pero el peligro siempre regresa a su vida. En esta ocasión, el equipo se enfrenta a un complot mundial orquestado por el asesino más temible del mundo: el hermano de Dom.'",)


cm.close()