class Cliente:
    """Clase cliente para la cuenta"""  
    def __init__(self, apellido ,nom , direcc, ntlf,dni):
        self.nombre = nom
        self.apellidos = apellido
        self.direccion = direcc
        self.num_tlf = ntlf
        self.dni = dni
        