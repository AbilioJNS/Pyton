from Cuenta import Cuenta

class Banco:
    """Function printing python version."""
    cuenta = Cuenta

    def __init__(self,sucursal,nombre):
        self.sucursal = sucursal
        self.nombre = nombre

    def creaCuenta(self,cliente):
        self.cuenta = Cuenta(cliente)
    