import datetime
from Cliente import Cliente


class Cuenta:
    """Function printing python version."""
    numCuenta = 0
    saldo = 0
    titular = Cliente
    autorizado = Cliente
    movimientos = []
       
    def __init__(self, cliente1, fecha = datetime.date):
        self.fecha_apertura = fecha
        self.titular = cliente1             
           