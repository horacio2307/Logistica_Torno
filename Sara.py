from tkinter import*


class user:
    def __init__ (self, _nombre, _correo, _largo, _ancho, _profundo, _proceso_termico, _proceso_maquinado, _paqueteria, _card, _code):
        self.nombre = _nombre
        self.correo = _correo
        self.largo = _largo
        self.ancho = _ancho
        self.profundo = _profundo
        self.proceso_termico = _proceso_termico
        self.proceso_maquinado = _proceso_maquinado
        self.paqueteria = _paqueteria
        self.card = _card
        self.code = _code

    def validation(self):
        
        flag = False

        return flag

def Cerrar_Gerente():

    global w_gerente
    ventana.deiconify()
    w_gerente.destroy()

def send_data():
    global w_usuario, Tarjeta_entry, Codigo_entry
    w_usuario.destroy()
    ventana.deiconify()

def validacion():
    global Enviar, Nombre, Correo, Largo, Ancho, Profundo, No_Tarjeta, Codigo

    name = Nombre.get()
    mail = Correo.get()
    long = Largo.get()
    Anchoo = Ancho.get()
    deep = Profundo.get()
    number_card = No_Tarjeta.get()
    code_card = Codigo.get()
    

    #if coindicion : 
    Enviar.config(state=NORMAL)

def Cash():

    global Tarjeta_entry, Codigo_entry, No_Tarjeta, Codigo
    No_Tarjeta="0"
    Codigo="0"
    Tarjeta_entry.config(state=DISABLED)
    Codigo_entry.config(state=DISABLED)


def datos_usuario():
    global w_usuario, Enviar, Tarjeta_entry, Codigo_entry, Nombre, Correo, Largo, Ancho, Profundo, No_Tarjeta, Codigo
    w_usuario = Toplevel(ventana)
    w_usuario.geometry("650x550")
    w_usuario.title("Usuario")
    main_title = Label(w_usuario ,text = "!Bienvenido, es un gusto atenderle!", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    main_title.pack()
    ventana.iconify()
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
    Maquinado = Button(w_usuario,text="Maquinado", width = "15",height ="2", bg ="green",command=PushMaquinado)
    Termico = Button(w_usuario,text="Termico", width = "15",height ="2", bg ="green")
    Procesos.place(x=22, y=370)
    Maquinado.place(x=22, y=400)
    Termico.place(x=22, y=460)

    #Entrega
    Metodo_Envio = Label(w_usuario,text="Metodo Envio",bg="white")
    Boton_Fedex = Button(w_usuario,text="Fedex",width="10",height="2",bg="green",command=PushFedex)
    Boton_Estafeta = Button(w_usuario,text="Estafeta",width="10",height="2",bg="green",command=PushEstafeta)
    Boton_DHL = Button(w_usuario,text="DHL",width="10",height="2",bg="green",command=PushDHL)

    Metodo_Envio.place(x=300, y=70)
    Boton_Fedex.place(x=300, y=100)
    Boton_Estafeta.place(x=400, y=100)
    Boton_DHL.place(x=500, y=100)

    #Pago

    Forma_Pago = Label(w_usuario,text="Metodo de pago", bg="white")
    Boton_Efectivo = Button(w_usuario,text="Efectivo",width="10",height="2",bg="green",command=Cash)
    Label_Tarjeta = Label(w_usuario,text="No. Tarjeta",bg="white")
    No_Tarjeta = StringVar()
    Codigo = StringVar()
    Tarjeta_entry = Entry(w_usuario,text="Tarjeta",textvariable=No_Tarjeta, width="20")
    Codigo_entry = Entry(w_usuario,textvariable=Codigo,width="5",show="*")

    Forma_Pago.place(x=300, y=190)
    Label_Tarjeta.place(x=300,y=220)
    Tarjeta_entry.place(x=300,y=250)
    Codigo_entry.place(x=300,y=270)
    Boton_Efectivo.place(x=500, y=250)

    #Salir
    Enviar = Button(w_usuario,text="Enviar",width = "15", height="2", bg= "gray",command=send_data)
    Validar = Button(w_usuario,text="Validar",width="15",height="2", bg = "gray",command=validacion)

    Enviar.config(state=DISABLED)
    Enviar.place(x=450, y=400)
    Validar.place(x=450, y=460)

def PushFedex():

    Selec_Paqueteria = "Fedex"

def PushDHL():

    Selec_Paqueteria = "DHL"

def PushEstafeta():

    Selec_Paqueteria = "Estafeta"

def PushMaquinado():
    global w_usuario, window_maquinado
    w_usuario.iconify()
    window_maquinado = Toplevel(w_usuario)
    window_maquinado.title("Maquinado")
    window_maquinado.geometry("200x200")
    Label(window_maquinado,text = "Seleccione un maquinado", bg = "#56CD63", fg = "black", width = "500", height = "2").pack()
    Button(window_maquinado,text="Torneado",width = "30", height = "2", bg = "white",command=PushTorneado).pack()
    Button(window_maquinado,text="Fresado",width = "30", height = "2", bg = "white").pack()
    Button(window_maquinado,text="Rectificado",width = "30", height = "2", bg = "white").pack()
    Button(window_maquinado,text="Taladrado",width = "30", height = "2", bg = "white").pack()

def PushTorneado():
    global w_usuario, window_maquinado
    Estado_Maquinado = "Torneado"
    w_usuario.deiconify()
    window_maquinado.destroy()



def datos_gerente():
    global w_gerente
    ventana.iconify()
    w_gerente = Toplevel(ventana)
    w_gerente.geometry("650x550")
    w_gerente.title("Gerente")
    main_title = Label(w_gerente ,text = "!Bienvenido!", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    main_title.pack()

    Button(w_gerente,text="Cerrar",width="30",height="2",bg="red", command=Cerrar_Gerente).pack()



def Cerrar():
    ventana.destroy()

#Variables

Usuarios = []
Estado_Termico = ""
Estado_Maquinado = ""
Selec_Paqueteria = ""

#Ventanas
ventana = Tk()
ventana.geometry("250x225")
main_title = Label(text = "!Bienvenido!", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()


Verificar = Button(ventana, text = "Log in", width = "30", height = "2", bg = "white")
Verificar.pack()
Gerente = Button(ventana,text="Gerente", width = "30", height = "2", bg = "white",command=datos_gerente)
#Gerente.place(x = 235, y = 220)
Gerente.pack()
Usuario = Button(ventana,text="Usuario", width = "30", height = "2", bg = "white", command=datos_usuario)
#Usuario.place(x = 235, y = 320)
Usuario.pack()
Salir = Button(ventana,text="Salir",width="30",height="2",bg="red", command=Cerrar)
#Salir.place(x=235,y=420)
Salir.pack()

ventana.mainloop()
