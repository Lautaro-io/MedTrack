import tkinter as tk
import customtkinter as ctk


class Panel(ctk.CTkFrame):
    def __init__(self,master,title:str,input1:str,input2:str,row:int,rowButton):
        super().__init__(master)
        self.configure(width= 250 , height= 50)
        self.grid(row = row, padx= 50 ,pady = 50,sticky ="ew")
        self.title = ctk.CTkLabel(self,text=title)
        self.title.grid(row=0,column = 0,pady = (0,10))

        self.input1 = ctk.CTkEntry(self,placeholder_text=input1,width=200)
        self.input1.grid(row = 1 , column = 0 ,pady=10)

        self.input2 = ctk.CTkEntry(self,placeholder_text=input2,width=200)
        self.input2.grid(row = 2 , column = 0 ,pady=10)

        self.button = ctk.CTkButton(self,text="Crear", command= self.send_data,width=200)
        self.button.grid(row = rowButton, column = 0,pady= 10)



    def send_data(self):
        data1 = self.input1.get()
        data2 = self.input2.get()

        
