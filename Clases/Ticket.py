from SQL import databases as db

class Ticket():
    def __init__(self, id_comprador = '', id_pelicula = '', cant_butacas = 0, fecha = '', horario = '', precio = 0, id = None):
        self.id = id
        self.id_comprador = id_comprador
        self.id_pelicula = id_pelicula
        self.cant_butacas = cant_butacas
        self.fecha = fecha
        self.horario = horario
        self.precio = precio

    def cargar_ticket(self, bdd):
        bdd.insert('tickets',
                    'comprador, pelicula, cant_butacas, fecha, horario, precio', 
                    f'{self.id_comprador}, {self.id_pelicula}, {self.cant_butacas}, "{self.fecha}", "{self.horario}", {self.precio}')
    
    def all_tickets(self, bdd):
        lista = []
        tickets =  bdd.select_all('tickets', '')