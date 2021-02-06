from tkinter import*


def datos_usuario():
    ventana.iconify()
    w_usuario = Toplevel(ventana)
    w_usuario.geometry("650x550")
    w_usuario.title("Usuario")

    # Define Label Fields 
    username_label = Label(text = "Username", bg = "#FFEEDD")
    username_label.place(x = 22, y = 70)
    password_label = Label(text = "Password", bg = "#FFEEDD")
    password_label.place(x = 22, y = 130)
    fullname_label = Label(text = "Fullname", bg = "#FFEEDD")
    fullname_label.place(x = 22, y = 190)
    age_label = Label(text = "Age", bg = "#FFEEDD")
    age_label.place(x = 22, y = 250)
    
    # Get and store data from users 
    username = StringVar()
    password = StringVar()
    fullname = StringVar()
    age = StringVar()
    
    username_entry = Entry(w_usuario ,textvariable = username, width = "40")
    password_entry = Entry(textvariable = password, width = "40",  show = "*")
    fullname_entry = Entry(textvariable = fullname, width = "40")
    age_entry = Entry(textvariable = age, width = "40")
    
    username_entry.place(x = 22, y = 100)
    password_entry.place(x = 22, y = 160)
    fullname_entry.place(x = 22, y = 220)
    age_entry.place(x = 22, y = 280)

    
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
Gerente = Button(ventana,text="Gerente", width = "30", height = "2", bg = "white",command=datos_gerente)
Gerente.place(x = 235, y = 220)
Usuario = Button(ventana,text="Usuario", width = "30", height = "2", bg = "white", command=datos_usuario)
Usuario.place(x = 235, y = 320)
Salir = Button(ventana,text="Salir",width="30",height="2",bg="red", command=Cerrar)
Salir.place(x=235,y=420)
ventana.mainloop()