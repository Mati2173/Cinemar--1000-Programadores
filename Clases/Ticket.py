from SQL import databases as db

class Ticket():
    def __init__(self, dni_comprador = 0, pelicula = '', cant_butacas = 0, fecha = '', horario = '', precio = 0, id = None):
        self.id = id
        self.dni_comprador = dni_comprador
        self.pelicula = pelicula
        self.cant_butacas = cant_butacas
        self.fecha = fecha
        self.horario = horario
        self.precio = precio
    
    def cargar_ticket(self, bdd):
        bdd.insert('tickets',
                    'comprador, pelicula, cant_butacas, fecha, horario, precio', 
                    f'{self.dni_comprador}, {self.pelicula}, {self.cant_butacas}, "{self.fecha}", "{self.horario}", {self.precio}')
    
    def all_tickets(self, bdd):
        lista = []
        tickets =  bdd.select_all('tickets', 'id_ticket, comprador, pelicula, cant_butacas, fecha, horario, precio')

        for i in range(len(tickets)):
            lista.append(tickets[i])
        
        return lista
    
    def __str__(self):
        ticket = f'ID Ticket: {self.id}\nComprador: {self.dni_comprador}\nCantidad de Butacas: {self.cant_butacas}'
        ticket += f'Fecha: {self.fecha}\nHorario: {self.horario}\nPrecio: ${self.precio}'
        return ticket