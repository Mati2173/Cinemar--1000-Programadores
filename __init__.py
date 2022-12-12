from Clases.Descuento import Descuento
from SQL.databases import DataBase
db = DataBase("cinemar.db")

descuento = Descuento()
descuento.modificar_desc(db,"Lunes",20)

