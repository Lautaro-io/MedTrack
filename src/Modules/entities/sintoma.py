
class Sintoma():
    nombre:str
    descripcion:str

    def __init__(self, paciente, nombre:str , descripcion:str , fecha:str , hora:str):
        self.paciente = paciente
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"Paciente : {self.paciente} - {self.hora} -{self.fecha}, Sintoma: {self.nombre} - {self.descripcion}"