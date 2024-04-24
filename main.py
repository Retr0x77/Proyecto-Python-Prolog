from tkinter import *
from pyswip import Prolog
prolog = Prolog()

#Logica

def guardar_nombre():
    Nombre = Entrada.get()
    Nombre = Nombre.lower()
    
    prolog.consult("BD.pl")
    try:
        aprobado=bool(list(prolog.query("pasa_curso("+Nombre+")")))
        destacado=bool(list(prolog.query("alumno_destacado("+Nombre+")")))
        if aprobado ==True:
            BtnAprobado.select()
        else:
            BtnAprobado.deselect()
            
        if destacado ==True:
            BtnDestacado.select()
        else:
           BtnDestacado.deselect()
    except Exception as e:    
        messagebox.showerror("Se ha producido un error", (str(e)))

#GUI
root = Tk()

root.title("Consultar Estudiantes Aprobados y Destacados")
root.resizable(False, False)
root.geometry("490x120+400+150")

marco1=Frame()
marco1.grid(row= 0, column=0, sticky=NW)
marco1.config(width= 350,height=75)

NombreLb=Label(marco1, text="Nombre del Estudiante:", font=("Calibri", 14),  padx=12, pady=4)
NombreLb.pack(anchor=NW)
Entrada=Entry(marco1,font=("Roboroto", 12), bg="White", width=35)
Entrada.pack(padx=12)

marco2=Frame()
marco2.grid(row= 1, column=1)
marco2.config(width= 150,height=150)

marco3=Frame()
marco3.grid(row= 0, column=1, sticky="s")
marco3.config(width= 150,height=75)


btn=Button(marco2, bg="#D9D9D9", text="Consultar", foreground="Black",  relief=SOLID, width=15, borderwidth=0, height=2, command=guardar_nombre)
btn.pack()

marco4=Frame()
marco4.grid(row= 1, column=0, sticky=NW)
marco4.config(width= 350,height=150)

Aprobado=Label(marco4, text="Pasa de grado:", font=("Calibri", 12), padx=12,)
Aprobado.pack(side="left")
BtnAprobado= Checkbutton(marco4, height=2, pady=0, state="disabled")
BtnAprobado.pack(side="left")

Destacado=Label(marco4, text="Destacado:", font=("Calibri", 12), padx=12,)
Destacado.pack(side="left")
BtnDestacado= Checkbutton(marco4, height=2, pady=0, state="disabled")
BtnDestacado.pack(side="left")

root.mainloop()