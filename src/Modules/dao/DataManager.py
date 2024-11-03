from src.db.datosPacientes import *
from src.Modules.entities.paciente import Paciente
from tkinter import messagebox


class DataManager:
    def __init__(self):
        self.pacienteslista = []
        self.sintomas =[]
        self.medicamentos = []
        self.registroMed = []
        self.registroSint = []



    def agregar_paciente(self,paciente):
        self.pacienteslista.append(paciente)
        print("Paciente Agregado!")


    def agregar_sintoma(self,sintoma):
        self.sintomas.append(sintoma)
        print("Sintoma Agregado!")


    def agregar_medicamento(self,medicamento):
        self.medicamentos.append(medicamento)
        print("Medicamento Agregado!")

    def getter_med(self):
        return [m for m in self.medicamentos]

    def getter_sis(self):
        return [s for s in self.sintomas]


    def get_sintoma(self,paciente_nombre):
        return [sintoma for sintoma in self.sintomas if sintoma.paciente == paciente_nombre]

    def get_medicamento(self,paciente_nombre):
        return [medicamento for medicamento in self.medicamentos if medicamento.paciente == paciente_nombre]

    def guardar_paciente(self,paciente):
        print(save(paciente))

    def set_medicacion(self,medicamento):
        print(save_med(medicamento))

    def cargar_datos(self):
        res = findAll("pacientes")
        pacienteTotal = res["personas"]

        for paciente in pacienteTotal:
            if len(paciente) == 4:
                _,nombre, dni, ingreso = paciente
                n_paciente = Paciente(nombre, dni, ingreso)
                self.pacienteslista.append(n_paciente.nombre)



    def cargar_meds(self):
        res = findAll("medicamentos")
        totalMeds = res["personas"]
        for m in totalMeds:
            if m not in self.medicamentos:
                self.medicamentos.append(m)
            else:
                messagebox.showerror("Error." , 'El medicamento ya esta en la lista de medicamentos')

    def cargar_sintomas(self):
        res = findAll("sintomas")
        totalS = res["personas"]
        for m in totalS:
            self.sintomas.append(m)
            print("Agregando" , m)


    def add_med_register(self,registro):
        self.registroMed.append(registro)

    def add_sint_register(self,registro):
        self.registroSint.append(registro)

    def cargar_medicamentos(self):
        save_med()
