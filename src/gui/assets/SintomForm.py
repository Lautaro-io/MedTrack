import customtkinter as ctk

from src.Modules.dao.DataManager import DataManager
from src.Modules.entities.medicamento import Medicamento
from src.db.datosPacientes import save_sintoma
from tkinter import messagebox

class SintomForm(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.data = DataManager()
        self.title("Agregar sintoma.")
        self.geometry("300x300")
        self.center_window()
        self.title = ctk.CTkLabel(self,text="Agregar Sintoma.", font= ("Roboto" , 20 , "bold" ))
        self.title.pack(pady=20)
        self.nombre_sintoma = ctk.CTkEntry(self, placeholder_text="Nombre del Sintoma",width= 200)
        self.nombre_sintoma.pack(pady=20)

        self.descripcion_sintoma = ctk.CTkEntry(self, placeholder_text="Descripción",width= 200)
        self.descripcion_sintoma.pack(pady=10)
        self.guardar_btn = ctk.CTkButton(self, text="Guardar", command=self.guardar)
        self.guardar_btn.pack(pady=10)

    def guardar(self):
        nombreSintoma = self.nombre_sintoma.get()
        detalle = self.descripcion_sintoma.get()
        n_sintoma = {
            "sintoma":nombreSintoma,
            "detalle": detalle
        }
        print(save_sintoma(n_sintoma))
        self.data.agregar_sintoma(nombreSintoma)
        messagebox.showinfo("Exito", "Sintoma agregado.")
        self.destroy()

    def center_window(self):
        ancho = 300
        alto = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)

        self.geometry(f"{ancho}x{alto}+{x}+{y}")



