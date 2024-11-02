
class Paciente:

    def __init__(self,nombre: str, dni: int, ingreso: str):
        self.nombre = nombre
        self.dni = dni
        self.ingreso = ingreso


    def __str__(self):
        return f"{self.nombre} - {self.dni} - Ingreso : {self.ingreso}"
