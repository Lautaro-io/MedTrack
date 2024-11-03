from tkinter import PhotoImage
import  customtkinter as ctk
from tkinter import messagebox
from tkcalendar import Calendar

from src.Modules.dao.DataManager import DataManager
from src.Modules.entities.medicamento import Medicamento
from src.Modules.entities.paciente import Paciente
from src.Modules.entities.sintoma import Sintoma
from src.gui.WindowForm import FormularioVentana
from src.gui.assets.SintomForm import SintomForm

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x600")
        self.center_window()
        self.grid_columnconfigure(0,weight=1,uniform="equal")
        self.grid_columnconfigure(1,weight=3,uniform="equal")
        self.rowconfigure(0,weight = 1)

        self.iconbitmap("assets/icon_app.ico")
        self.title("MedTrack")


        self.datos = DataManager()
        self.datos.cargar_datos()
        self.datos.cargar_meds()
        self.datos.cargar_sintomas()

        ##Configuracion y creacion del menu izquierdo
        self.left_menu = ctk.CTkFrame(self,width=200)
        self.left_menu.grid(row= 0 , column = 0, sticky = "nsew")
        self.left_menu.grid_rowconfigure(0, weight=1)
        self.left_menu.grid_rowconfigure(1, weight=1)
        self.left_menu.grid_rowconfigure(2, weight=1)
        self.left_menu.grid_rowconfigure(3, weight=1)


        #Configuracion y creacion del menu derecho
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(1, weight=0)
        self.right_frame.grid_rowconfigure(2, weight=0)
        self.right_frame.grid_rowconfigure(3, weight=0)
        self.right_frame.configure(fg_color="black")

        self.pacienteIcon = PhotoImage(file="assets/P.png")
        self.sintomaIcon = PhotoImage(file="assets/S.png")
        self.medicacionIcon = PhotoImage(file="assets/M.png")
        self.listaIcon = PhotoImage(file="assets/4.png")
        self.addIcon = PhotoImage(file="assets/boton-circular-plus.png")
        self.titleIcon = PhotoImage(file="assets/Health_kepper__3_-removebg-preview.png")
        self.left_menu_widgets()
        self.right_widgets()



    def right_widgets(self):
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(1, weight=0)
        self.right_frame.grid_rowconfigure(2, weight=0)
        self.right_frame.grid_rowconfigure(3, weight=0)
        self.titleApp = ctk.CTkLabel(self.right_frame,text="",image=self.titleIcon ,compound="center", font=("Lato",50,"bold") )
        self.titleApp.grid(row = 0 , column = 0 )
        self.dev =  ctk.CTkLabel(self.right_frame,text="App desarrollada por Lautaro Ildarraz" , font=("Helvetica",11,"bold") )
        self.dev.grid(row =2  , column = 0)




    def left_menu_widgets(self):
        self.left_menu.grid_rowconfigure(0, weight=1)
        self.left_menu.grid_rowconfigure(1, weight=1)
        self.left_menu.grid_rowconfigure(2, weight=1)
        self.left_menu.grid_rowconfigure(3, weight=1)
        self.left_menu.grid_columnconfigure(0, weight=1)
        boton1 = ctk.CTkButton(self.left_menu, text="" ,fg_color="brown4", image=self.pacienteIcon ,compound="left", border_width=0, command=self.show_patients , hover_color="white")
        boton1.grid(row=0, column=0, sticky="nsew",padx = 1, pady = 1)
        boton2 = ctk.CTkButton(self.left_menu, text="",image=self.sintomaIcon,fg_color="brown4" ,compound="left", border_width=0,command=self.set_sintoma, hover_color="white")
        boton2.grid(row=1, column=0, sticky="nsew",padx = 1, pady = 1)
        boton3 = ctk.CTkButton(self.left_menu, text="",image=self.medicacionIcon,fg_color="brown4" ,compound="left", border_width=0, command= self.set_medicamento, hover_color="white")
        boton3.grid(row=2, column=0, sticky="nsew",padx = 1, pady = 1)
        boton4 = ctk.CTkButton(self.left_menu, text="",image=self.listaIcon,fg_color="brown4" ,compound="left", border_width=0 , command= self.resgistros, hover_color="white")
        boton4.grid(row=3, column=0, sticky="nsew",padx = 1, pady = 1)


    def center_window(self):
        ancho = 500
        alto = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def show_patients(self):
        self.clear_frame()
        self.igualar_filas()
        self.titleP = ctk.CTkLabel(self.right_frame,text="Cargar paciente", font= ("Roboto", 18 , "bold"))
        self.titleP.grid(row = 1 , column = 0,pady = 20 )
        self.addButtonM = ctk.CTkButton(self.right_frame,text="Agregar Medicamento",text_color="black" ,image=self.addIcon ,compound="right", border_width=0, width=5 , fg_color= "white", command= self.openFormMed)
        self.addButtonM.grid(row = 7, column = 0,padx = 20,pady = 2)
        self.addButtonS = ctk.CTkButton(self.right_frame, text="Agregar Sintoma", text_color="black",
                                       image=self.addIcon, compound="right", border_width=0, width=5, fg_color="white",
                                       command=self.openSintomForm)
        self.addButtonS.grid(row=8, column=0, pady = 15,padx=2)
        self.frameName = ctk.CTkFrame(self.right_frame , fg_color= "black")
        self.frameName.grid(row = 3 ,column = 0)
        self.nombreE = ctk.CTkEntry(self.frameName, width= 80 , placeholder_text= "Nombre.")
        self.nombreE.grid(row = 0 , column =0, pady = 15, padx = 12)
        self.apellidoE = ctk.CTkEntry(self.frameName, width= 80 , placeholder_text= "Apellido.")
        self.apellidoE.grid(row = 0 , column =1, pady = 15, padx = 12)

        self.dniE = ctk.CTkEntry(self.right_frame, width= 180 , placeholder_text= "Dni del paciente.")
        self.dniE.grid(row = 4 , column =0, pady = 15)

        self.ingresoE = Calendar(self.right_frame)
        self.ingresoE.grid(row = 5 , column =0, pady = 15)

        self.submitBtn = ctk.CTkButton(self.right_frame, text= "Cargar paciente.",command=self.agregar_paciente )
        self.submitBtn.grid(row = 6,column = 0, pady = 15)
        self.dev =  ctk.CTkLabel(self.right_frame,text="App desarrollada por Lautaro Ildarraz" , font=("Helvetica",11,"bold","underline") )
        self.dev.grid(row =10 , column = 0)


    def set_sintoma(self):
        self.clear_frame()
        self.igualar_filas()
        self.datos.sintomas.clear()
        self.datos.cargar_sintomas()
        self.titleS = ctk.CTkLabel(self.right_frame,text="Registrar sintoma", font= ("Roboto", 15 , "bold"))
        self.titleS.grid(row = 0 , column = 0,pady = 20 )
        self.pacientesCB = ctk.CTkComboBox(self.right_frame,width=200, values = [paciente for paciente in self.datos.pacienteslista])
        self.pacientesCB.grid(row = 1 , column = 0,pady = 20 )
        self.pacientesCB.set("Paciente")
        self.sintomasCB =ctk.CTkComboBox(self.right_frame,width=200,values = [sintoma[1] for sintoma in self.datos.sintomas])
        self.sintomasCB.grid(row = 2 , column = 0,pady = 20 )
        self.sintomasCB.set("Sintoma")
        self.dettalleS = ctk.CTkEntry(self.right_frame,placeholder_text="Detalle",width=200)
        self.dettalleS.grid(row = 3 , column =0, pady = 15)
        self.frame_time = ctk.CTkFrame(self.right_frame,width=100, fg_color="black")
        self.frame_time.grid(row = 4 , column = 0, padx = 10 , pady = 10 )
        self.Ltime = ctk.CTkLabel(self.frame_time, text="Hora: ")
        self.Ltime.grid(row = 0 , column =0 )
        self.horasE = ctk.CTkEntry(self.frame_time, width= 50 , placeholder_text= " HH." )
        self.horasE.grid(row = 0 , column =1, pady = 15,padx = 10)
        self.min = ctk.CTkEntry(self.frame_time , width = 50 , placeholder_text= " MM")
        self.min.grid(row= 0 , column = 2,pady = 15, padx =10)
        self.calendar = Calendar(self.right_frame)
        self.calendar.grid(row=5, column=0, pady=(5, 5))
        self.submitBtnS = ctk.CTkButton(self.right_frame, text= "Registrar sintoma." , command= self.agregar_sintoma)
        self.submitBtnS.grid(row = 6,column = 0, pady = 15)
        self.dev =  ctk.CTkLabel(self.right_frame,text="App desarrollada por Lautaro Ildarraz" , font=("Helvetica",11,"bold","underline") )
        self.dev.grid(row =8  , column = 0)


    def set_medicamento(self):
        self.clear_frame()
        self.igualar_filas()
        self.datos.medicamentos.clear()
        self.datos.cargar_meds()
        self.titleM = ctk.CTkLabel(self.right_frame,text="Registrar medicamento", font= ("Roboto", 15 , "bold"))
        self.titleM.grid(row = 0 , column = 0,pady = 20 )
        self.pacientesCB = ctk.CTkComboBox(self.right_frame,width=200,values=[paciente for paciente in self.datos.pacienteslista])
        self.pacientesCB.grid(row = 1 , column = 0,pady = 20 )
        self.pacientesCB.set("Paciente")
        self.medicamentoCB =ctk.CTkComboBox(self.right_frame,width=200,values = [medicamento[1] for medicamento in self.datos.getter_med()])
        self.medicamentoCB.grid(row = 2 , column = 0,pady = 20 )
        self.medicamentoCB.set("Medicamento")
        self.frame_time2 = ctk.CTkFrame(self.right_frame,width=100, fg_color="black")
        self.frame_time2.grid(row=4, column=0, padx=10, pady=10)
        self.Ltimes = ctk.CTkLabel(self.frame_time2, text="Hora: ")
        self.Ltimes.grid(row=0, column=0)
        self.horasEs = ctk.CTkEntry(self.frame_time2, width=50, placeholder_text=" HH.")
        self.horasEs.grid(row=0, column=1, pady=15, padx=10)
        self.mins = ctk.CTkEntry(self.frame_time2, width=50, placeholder_text=" MM")
        self.mins.grid(row=0, column=2, pady=15, padx=10)
        self.detalleE = ctk.CTkEntry(self.right_frame, width= 200 , placeholder_text= "Detalle")
        self.detalleE.grid(row = 3 , column =0, pady = 15)
        self.calendar = Calendar(self.right_frame)
        self.calendar.grid(row=5, column=0, pady=(5, 5))
        self.submitBtnM = ctk.CTkButton(self.right_frame, text= "Registrar medicamento.",command=self.agregar_medicamento)
        self.submitBtnM.grid(row = 6,column = 0, pady = 15)
        self.dev =  ctk.CTkLabel(self.right_frame,text="App desarrollada por Lautaro Ildarraz" , font=("Helvetica",11,"bold","underline") )
        self.dev.grid(row =8  , column = 0)

    def agregar_paciente(self):
        nombre = self.nombreE.get()
        apellido =  self.apellidoE.get()
        nombreCompleto = f"{nombre.capitalize()} {apellido.capitalize()} "
        dni = self.dniE.get()
        ingreso = self.ingresoE.get_date()
        if not nombre or not dni or not ingreso or not apellido:
            messagebox.showerror("Error","Error, complete todos los campos")
        else:

            paciente  = Paciente(nombreCompleto,dni,ingreso)
            self.datos.agregar_paciente(paciente.nombre)
            self.datos.guardar_paciente(paciente)
            messagebox.showinfo("Exito!", "Paciente agregado con exito")


    def agregar_medicamento(self):
        paciente = self.pacientesCB.get()
        fecha = self.calendar.get_date()
        hora = self.horasEs.get()
        min = self.mins.get()
        horaTotal = f"{hora}:{min}"
        medicamento = self.medicamentoCB.get()
        detalle = self.detalleE.get()
        if not hora.isnumeric() or not min.isnumeric() or len(hora) != 2 or len(min) != 2:
            messagebox.showerror("","Hora debe ser numerica")

        else:
            if paciente and medicamento and detalle and fecha and hora and min:
                n_medicamento = Medicamento(paciente,medicamento,detalle,fecha,horaTotal)
                self.datos.add_med_register(n_medicamento)
                messagebox.showinfo("Exito","Medicamento registrado con exito!.")
            else:
                messagebox.showerror("Error", "Campos incompletos.")



    def agregar_sintoma(self):
        paciente = self.pacientesCB.get()
        fecha = self.calendar.get_date()
        hora = self.horasE.get()
        min = self.min.get()
        horaTotal = f"{hora}:{min}"
        sintoma = self.sintomasCB.get()
        detalle = self.dettalleS.get()
        if not hora.isnumeric() or not min.isnumeric() or len(hora) != 2 or len(min) != 2:
            messagebox.showerror("","Hora debe ser numerica")
        else:

            if paciente and sintoma and detalle and fecha and hora and min:
                n_sintoma = Sintoma(paciente,sintoma,detalle,fecha,horaTotal)
                self.datos.add_sint_register(n_sintoma)
                messagebox.showinfo("Exito","Sintoma registrado con exito!.")
            else:
                messagebox.showerror("Error", "Campos incompletos.")

    def resgistros(self):
        self.clear_frame()
        self.igualar_filas()
        self.rTitle = ctk.CTkLabel(self.right_frame,text="Ver registros de un paciente. " , font = ("Roboto" , 20 , "bold"))
        self.rTitle.grid(row = 0 , column = 0 ,pady = 15)
        self.pacientesCB = ctk.CTkComboBox(self.right_frame,width=200 , values = [paciente for paciente in self.datos.pacienteslista])
        self.pacientesCB.grid(row = 1 , column = 0,pady = 20 )
        self.pacientesCB.set("Selecciona un paciente")
        self.buttonR = ctk.CTkButton(self.right_frame,text="Ver registros." , width= 150 ,fg_color="grey" , text_color="black",corner_radius= 5,command=self.show_registros)
        self.buttonR.grid(row =2 , column = 0 , pady = 20)
        self.text_frame = ctk.CTkFrame(self.right_frame)
        self.text_frame.grid(row= 3 , column =0)
        self.info = ctk.CTkLabel(self.text_frame , text="",width=400, wraplength=300)
        self.info.pack( pady =20 )
        self.dev =  ctk.CTkLabel(self.right_frame,text="App desarrollada por Lautaro Ildarraz" , font=("Helvetica",11,"bold","underline") )
        self.dev.grid(row =10  , column = 0)

    def show_registros(self):
        nombre = self.pacientesCB.get()
        print(nombre)
        registros = ""
        for paciente in self.datos.registroMed:
            if paciente.paciente == nombre:
                registros += f"\n{str(paciente)}"
        for paciente in self.datos.registroSint:
            if paciente.paciente == nombre:
                registros += f"\n{str(paciente)}"

        if registros:
            self.info.configure(text=registros, font=("Roboto" , 15 , "bold"))
        else:
            self.info.configure(text="No se encontraron registros para el paciente seleccionado.")

        self.info.update_idletasks()



    def igualar_filas(self):
        self.right_frame.grid_rowconfigure(0, weight=0)
        self.right_frame.grid_rowconfigure(1, weight=0)
        self.right_frame.grid_rowconfigure(2, weight=0)
        self.right_frame.grid_rowconfigure(3, weight=0)

    def clear_frame (self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()

    def openFormMed(self):
        newForm = FormularioVentana(self)
        newForm.mainloop()

    def openSintomForm(self):
        newForm = SintomForm()
        newForm.mainloop()


app = App()
app.mainloop()



