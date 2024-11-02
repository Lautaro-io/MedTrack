import customtkinter as ctk

from src.Modules.dao.DataManager import DataManager
from src.Modules.entities.medicamento import Medicamento
from src.db.datosPacientes import save_med
from tkinter import messagebox


class FormularioVentana(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.data = DataManager()
        self.title("Agregar medicamento.")
        self.geometry("300x300")
        self.center_window()
        self.title = ctk.CTkLabel(self,text="Agregar Medicamento.", font= ("Roboto" , 20 , "bold" ))
        self.title.pack(pady=20)
        self.nombre_medicamento = ctk.CTkEntry(self, placeholder_text="Nombre del Medicamento",width= 200)
        self.nombre_medicamento.pack(pady=20)

        self.descripcion_medicamento = ctk.CTkEntry(self, placeholder_text="Descripción",width= 200)
        self.descripcion_medicamento.pack(pady=10)
        self.guardar_btn = ctk.CTkButton(self, text="Guardar", command=self.guardar,)
        self.guardar_btn.pack(pady=10)

    def guardar(self):
        nombre = self.nombre_medicamento.get()
        descripcion = self.descripcion_medicamento.get()
        n_medicamento = {
            "nombre_medicamento" : nombre,
            "detalle" : descripcion

        }
        self.data.agregar_medicamento(n_medicamento)
        print(save_med(n_medicamento))
        messagebox.showinfo("Exito! ", "Medicamento agregado con exito.")
        self.destroy()

    def center_window(self):
        ancho = 300
        alto = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)

        self.geometry(f"{ancho}x{alto}+{x}+{y}")



