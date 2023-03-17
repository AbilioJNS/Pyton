import pickle
from Banco import Banco
from Cliente import Cliente

def nuevo_cliente():
    """Introducimos datos de cliente"""
    nombre = input("introduce en nombre del cliente")
    apellido = input("introduce el apellido del cliente")
    telefono = input("introduce el telefono del cliente")
    direccion = input("introduce la direccion")
    dni = input("introduce el dni del cliente")
    return Cliente(apellido,nombre,direccion,telefono,dni)

if __name__ == "__main__":
    #cliente = nuevo_cliente()
    cliente = nuevo_cliente()
    banco1 = Banco(345,"BBVA")
    banco1.creaCuenta(cliente)
    banco2 = Banco(366,"Caixa")
    banco2.creaCuenta(cliente)
    banco3 = Banco(355,"Santander")
    banco3.creaCuenta(cliente)
    bancos = [banco1,banco2,banco3]
    #pickle.dump(banco,"ficheroBanco.txt",protocol=)
    with open("ficheroBanco.pickle", 'wb') as ficheroBanco:
        pickle.dump(bancos, ficheroBanco, protocol=pickle.HIGHEST_PROTOCOL)
    archivoBancos = open("ficheroBanco.pickle", 'rb') 
    bancosList = pickle.load(archivoBancos)
    for banco in bancosList:
        print(banco.nombre)