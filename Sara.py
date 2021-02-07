from tkinter import*

def send_data():
    w_usuario.iconify()
def validacion():
    Enviar.config(state=NORMAL)

def datos_usuario():

    w_usuario.deiconify()
    # Define Label Fields 
    Label_Nombre = Label(w_usuario, text = "Nombre", bg = "white")
    Label_Nombre.place(x = 22, y = 70)
    Label_Correo = Label(w_usuario,text = "Correo", bg = "white")
    Label_Correo.place(x = 22, y = 130)
    Label_Largo = Label(w_usuario, text = "Largo", bg = "white")
    Label_Largo.place(x = 22, y = 190)
    Label_Ancho = Label(w_usuario,text = "Ancho", bg = "white")
    Label_Ancho.place(x = 22, y = 250)
    Label_Profundo = Label(w_usuario, text = "Profundo", bg = "white")
    Label_Profundo.place(x = 22, y = 310)
    
    # Get and store data from users
    Nombre = StringVar()
    Correo = StringVar()
    Largo = StringVar()
    Ancho = StringVar()
    Profundo = StringVar()
    
    Nombre_entry = Entry(w_usuario ,textvariable = Nombre, width = "40")
    Correo_entry = Entry(w_usuario ,textvariable = Correo, width = "40")
    Largo_entry = Entry(w_usuario ,textvariable = Largo, width = "40")
    Ancho_entry = Entry(w_usuario ,textvariable = Ancho, width = "40")
    Profundo_entry = Entry(w_usuario, textvariable = Profundo, width = "40")
    
    Nombre_entry.place(x = 22, y = 100)
    Correo_entry.place(x = 22, y = 160)
    Largo_entry.place(x = 22, y = 220)
    Ancho_entry.place(x = 22, y = 280)
    Profundo_entry.place(x =22, y = 340)
    
    #Procesos
    Procesos = Label(w_usuario,text = "Procesos", bg= "white")
    Maquinado = Button(w_usuario,text="Maquinado", width = "15",height ="2", bg ="green")
    Termico = Button(w_usuario,text="Termico", width = "15",height ="2", bg ="green")
    Procesos.place(x=22, y=370)
    Maquinado.place(x=22, y=400)
    Termico.place(x=22, y=460)

    #Entrega


    #Pago


    #Salir
    Enviar.config(state=DISABLED)
    Enviar.place(x=450, y=400)
    Validar.place(x=450, y=460)


def datos_gerente():
    ventana.iconify()
    w_gerente = Toplevel(ventana)
    w_gerente.geometry("650x550")
    w_gerente.title("Gerente")

def Cerrar():
    ventana.destroy()

ventana = Tk()
ventana.geometry("650x550")
main_title = Label(text = "!Bienvenido!", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()
w_usuario = Toplevel(ventana)
w_usuario.geometry("650x550")
w_usuario.title("Usuario")
main_title = Label(w_usuario ,text = "!Bienvenido!", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()


Gerente = Button(ventana,text="Gerente", width = "30", height = "2", bg = "white",command=datos_gerente)
Gerente.place(x = 235, y = 220)
Usuario = Button(ventana,text="Usuario", width = "30", height = "2", bg = "white", command=datos_usuario)
Usuario.place(x = 235, y = 320)
Salir = Button(ventana,text="Salir",width="30",height="2",bg="red", command=Cerrar)
Salir.place(x=235,y=420)
Enviar = Button(w_usuario,text="Enviar",width = "15", height="2", bg= "gray",command=send_data)
Validar = Button(w_usuario,text="Validar",width="15",height="2", bg = "gray",command=validacion)

w_usuario.iconify()
ventana.mainloop()
