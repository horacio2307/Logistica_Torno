from tkinter import*
from tkinter import messagebox
from random import*
import smtplib

class user:
    def __init__ (self, _nombre, _correo, _largo, _ancho, _profundo, _proceso_termico, _proceso_maquinado, _paqueteria, _card, _code, _cash):
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
        self.cash = _cash
        self.folio = self.numero_folio()
        self.flag_maquinado = False
        self.flag_termico = False
        if self.proceso_maquinado != "":
            self.flag_maquinado = True
        if self.proceso_termico != "":
            self.flag_termico = True
        self.username = "monicasarahicardosopatino9@gmail.com"
        self.password = "cardoso19"
        self.x = True
        
    def numero_folio(self):

        global Folios

        no_folio = randint(0,1000)

        while no_folio in Folios:
        
            no_folio = randint(0,1000)
            
        return no_folio
 
    def validation(self):

        numeros = self.ancho.isdigit() and self.largo.isdigit() and self.profundo.isdigit()
        paqueteria = self.paqueteria != ""
        proceso = self.proceso_maquinado != "" or self.proceso_termico != ""
        number_tarjeta = self.card.isdigit()
        number_codigo = self.code.isdigit()
        efectivo = self.cash or (number_tarjeta and number_codigo)
        datos = self.nombre != "" #and self.correo != ""
        c_mail = "@" in self.correo

        if not datos:
            messagebox.showerror(title="Error",message="Verifique los datos porfavor")

        elif not c_mail:
            messagebox.showerror(title="Error",message="Verifique el correo porfavor")

        elif not numeros:
            messagebox.showerror(title="Error",message="Verifique las dimensiones")

        elif not paqueteria:
            messagebox.showerror(title="Error",message="Seleccione una paqueteria")

        elif not proceso:
            messagebox.showerror(title="Error",message="Seleecione un proceso")
        
        elif not efectivo:
            messagebox.showerror(title="Error",message="Verifique su metodo de pago porfavor")
         
        if numeros and paqueteria and proceso and efectivo and datos : 
            return True
        
        else: 
            return False

    def Venatana_usuario(self):
        self.frame = Tk()
        self.frame.geometry("450x220")
        self.frame.title("Datos")
        main_title = Label(self.frame ,text = "!Bienvenido, es un gusto atenderle!", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
        main_title.pack()

        texto_name = "nombre: " + str(self.nombre)
        Label(self.frame, text = texto_name, bg = "white").pack()
        texto_correo = "correo: " + str(self.correo)
        Label(self.frame, text = texto_correo, bg = "white").pack()
        if self.flag_maquinado:
            texto_maquinado = str(self.proceso_maquinado) + " en proceso"
            Label(self.frame, text = texto_maquinado, bg = "white").pack()
        
        if self.flag_termico:
            texto_termico = str(self.proceso_termico) + " en proceso"
            Label(self.frame, text = texto_termico, bg = "white").pack()

        if ((self.flag_maquinado or self.flag_termico) == False):
            Label(self.frame, text = "Producto Terminado", bg = "white").pack()

        Boton_close = Button(self.frame, text="Cerrar",width="30",height="2",bg="red", command = self.close_user)
        Boton_close.pack(side=BOTTOM)
    
    def Venatana_gerente(self):
        self.ceo = Tk()
        self.ceo.title("Datos")
        self.ceo.geometry("450x220")
        main_title = Label(self.ceo ,text = "!Bienvenido!", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
        main_title.pack()    

        if self.flag_maquinado:

           self.B_maquinado = Button(self.ceo,text = "Finalizar " + str(self.proceso_maquinado), width="15",height="2",bg="white", command = self.mail_maquinado)
           self.B_maquinado.pack()

        if self.flag_termico:

           self.B_termico = Button(self.ceo,text = "Finalizar " + str(self.proceso_termico), width="15",height="2",bg="white", command = self.mail_termico)
           self.B_termico.pack()
    
        if self.x == True:
            
            self.B_end = Button(self.ceo,text = "Finalizar", width="10",height="2",bg="green", command = self.mail_end)
            self.B_end.pack()


        Boton_close = Button(self.ceo, text="Cerrar",width="30",height="2",bg="red",  command = self.close_ceo)
        Boton_close.pack(side=BOTTOM)        

        if self.x ==FALSE:
            Label(self.ceo, text = "Producto Terminado", bg = "white").pack() 

    def mail_maquinado(self):
        self.B_maquinado.config(state=DISABLED)
        self.flag_maquinado = False
        Subject = str(self.proceso_maquinado) + " terminado"
        message = "Hola!, su pieza finalizo el " + str(self.proceso_maquinado)
        message="Subject: {}\n\n{}".format(Subject,message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.username,self.password)
        server.sendmail(self.username,self.correo,message)
        server.quit()

    def mail_termico(self):
        self.B_termico.config(state=DISABLED)
        self.flag_termico = False
        Subject = str(self.proceso_termico) + " terminado"
        message = "Hola!, su pieza finalizo el " + str(self.proceso_termico)
        message="Subject: {}\n\n{}".format(Subject,message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.username,self.password)
        server.sendmail(self.username,self.correo,message)
        server.quit()

    def mail_end(self):
        global w_gerente

        self.x=False
        if self.flag_maquinado == True:
            self.mail_maquinado()
        if self.flag_termico == True:
            self.mail_termico()

        self.B_end.config(state=DISABLED)
        Subject = "Pieza finalizada"
        message = "Su pieza ha terminado todos los procesos"
        message="Subject: {}\n\n{}".format(Subject,message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.username,self.password)
        server.sendmail(self.username,self.correo,message)
        server.quit()

    def close_user(self):
        self.frame.destroy()

    def close_ceo(self):
        global w_gerente
        w_gerente.deiconify()
        self.ceo.destroy()

def datos_usuario():
    global w_usuario, Enviar, Tarjeta_entry, Codigo_entry, Nombre, Correo, Largo, Ancho, Profundo, No_Tarjeta, Codigo
    global Estado_Maquinado, Estado_Termico, Selec_Paqueteria, Validar, bandera
    #Limpiado Variables
    Estado_Termico = ""
    Estado_Maquinado = ""
    Selec_Paqueteria = ""
    bandera = False
    w_usuario = Toplevel(ventana)
    w_usuario.geometry("650x550")
    w_usuario.title("Registro")
    main_title = Label(w_usuario ,text = "!Bienvenido, es un gusto atenderle!", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    main_title.pack()
    ventana.iconify()
    w_usuario.deiconify()

    # Define Label Fields 
    Label_Nombre = Label(w_usuario, text = "Nombre", bg = "white")
    Label_Nombre.place(x = 22, y = 70)
    Label_Correo = Label(w_usuario,text = "Correo", bg = "white")
    Label_Correo.place(x = 22, y = 130)
    Label_Largo = Label(w_usuario, text = "Largo (cm)", bg = "white")
    Label_Largo.place(x = 22, y = 190)
    Label_Ancho = Label(w_usuario,text = "Ancho (cm)", bg = "white")
    Label_Ancho.place(x = 22, y = 250)
    Label_Profundo = Label(w_usuario, text = "Profundo (cm)", bg = "white")
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
    Termico = Button(w_usuario,text="Termico", width = "15",height ="2", bg ="green",command=PushTermico)
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

    Botonx = Button(w_usuario,text="Cerrar",width="30",height="2",bg="red", command=cerrar_usuario)
    Botonx.pack(side=BOTTOM)

def datos_gerente():
    global w_gerente, Label_usuario ,Boton_usuario, Folio_entry, Contraseña, Folio_check
    ventana.iconify()
    w_gerente = Toplevel(ventana)
    w_gerente.geometry("450x220")
    w_gerente.title("Gerente")
    main_title = Label(w_gerente ,text = "!Bienvenido!", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    main_title.pack()

    Contraseña = StringVar()
    Folio_check = StringVar()

    Label1 = Label(w_gerente, text="Ingrese la contraseña", bg = "white")
    Label1.place(x=0,y=50)

    Contraseña_entry = Entry(w_gerente,textvariable=Contraseña, width="20", show="*")
    Contraseña_entry.place(x=120,y=52)

    Boton_Enviar = Button(w_gerente, text = "Verificar", width = "5", height = "1", bg = "white", command = sub_info_gerente)
    Boton_Enviar.place(x=245, y=50)

    Label_usuario = Label(w_gerente,text="Ingrese el folio           ",bg = "white",state=DISABLED)
    Label_usuario.place(x=0, y= 100)

    Folio_entry = Entry(w_gerente,textvariable=Folio_check, width="20",state=DISABLED)
    Folio_entry.place(x=120, y=100)

    Boton_usuario = Button(w_gerente,text="Buscar",width="5", height = "1", bg ="white",state=DISABLED,command=buscar_gerente)
    Boton_usuario.place(x=245, y=100)    
   
    Boton1 = Button(w_gerente,text="Cerrar",width="30",height="2",bg="red", command=Cerrar_Gerente)
    Boton1.pack(side=BOTTOM)

def sub_info_gerente():
    global Label_usuario ,Boton_usuario, Folio_entry, Contraseña

    password = Contraseña.get()

    if password == "12345":

        Label_usuario.config(state=NORMAL)
        Boton_usuario.config(state=NORMAL)
        Folio_entry.config(state=NORMAL)

    else:

        messagebox.showerror(title="Fail",message="Contraseña Incorrecta")
    
def buscar_gerente():
    global Folio_check, posicion, w_gerente

    w_gerente.iconify()
    buscar_folio = Folio_check.get()

    i = 0

    posicion = -1

    for number in Folios:

        if number == int(buscar_folio) :
                        
            posicion = i
            
            Usuarios[posicion].Venatana_gerente()


        i+=1

    if posicion == -1 :
        messagebox.showinfo(title="Folio",message="No se encontro el folio")

def cerrar_usuario():
    global w_usuario
    w_usuario.destroy()
    ventana.deiconify()

def Cerrar_Gerente():

    global w_gerente
    ventana.deiconify()
    w_gerente.destroy()

def send_data():
    global w_usuario, Tarjeta_entry, Codigo_entry, aux, Enviar
    messagebox.showinfo(title="Folio",message="Su folio es {}".format(aux.folio))
    Folios.append(aux.folio)
    Enviar.config(state=DISABLED)

def validacion():
    global Enviar, Nombre, Correo, Largo, Ancho, Profundo, No_Tarjeta, Codigo, bandera
    global Estado_Maquinado, Estado_Termico, Selec_Paqueteria, aux, Validar
    global Tarjeta_entry, Codigo_entry

    name = Nombre.get()
    mail = Correo.get()
    loong = str(Largo.get())
    Anchoo = str(Ancho.get())
    deep = str(Profundo.get())
    number_card = str(No_Tarjeta.get())
    code_card = str(Codigo.get())

    aux=user(name,mail,loong,Anchoo,deep,Estado_Termico,Estado_Maquinado,Selec_Paqueteria,number_card,code_card,bandera)
    #Si es validado se agrega a la lista 
    if (aux.validation()==True):
        Usuarios.append(aux)
        Validar.config(state=DISABLED)
        Enviar.config(state=NORMAL)
        Tarjeta_entry.config(state=DISABLED)
        Codigo_entry.config(state=DISABLED)

def Cash():

    global Tarjeta_entry, Codigo_entry, No_Tarjeta, Codigo, bandera
    #No_Tarjeta="0"
    #Codigo="0"
    Tarjeta_entry.config(state=DISABLED)
    Codigo_entry.config(state=DISABLED)
    bandera = True

def PushFedex():
    global Selec_Paqueteria
    Selec_Paqueteria = "Fedex"

def PushDHL():
    global Selec_Paqueteria
    Selec_Paqueteria = "DHL"

def PushEstafeta():
    global Selec_Paqueteria
    Selec_Paqueteria = "Estafeta"

def PushMaquinado():
    global w_usuario, window_maquinado, Estado_Maquinado
    w_usuario.iconify()
    window_maquinado = Toplevel(w_usuario)
    window_maquinado.title("Maquinado")
    window_maquinado.geometry("200x200")
    Label(window_maquinado,text = "Seleccione un maquinado", bg = "#56CD63", fg = "black", width = "500", height = "2").pack()
    Button(window_maquinado,text="Torneado",width = "30", height = "2", bg = "white",command=PushTorneado).pack()
    Button(window_maquinado,text="Fresado",width = "30", height = "2", bg = "white",command=PushFresado).pack()
    Button(window_maquinado,text="Rectificado",width = "30", height = "2", bg = "white",command=PushRectificado).pack()
    Button(window_maquinado,text="Taladrado",width = "30", height = "2", bg = "white",command=PushTaladrado).pack()

def PushTorneado():
    global w_usuario, window_maquinado, Estado_Maquinado
    Estado_Maquinado = "Torneado"
    w_usuario.deiconify()
    window_maquinado.destroy()

def PushFresado():
    global w_usuario, window_maquinado, Estado_Maquinado
    Estado_Maquinado = "Fresado"
    w_usuario.deiconify()
    window_maquinado.destroy()

def PushRectificado():
    global w_usuario, window_maquinado, Estado_Maquinado
    Estado_Maquinado = "Rectificado"
    w_usuario.deiconify()
    window_maquinado.destroy()

def PushTaladrado():
    global w_usuario, window_maquinado, Estado_Maquinado
    Estado_Maquinado = "Taladrado"
    w_usuario.deiconify()
    window_maquinado.destroy()

def PushTermico():
    global w_usuario, window_termico
    w_usuario.iconify()
    window_termico = Toplevel(w_usuario)
    window_termico.title("Proceso Termico")
    window_termico.geometry("200x200")
    Label(window_termico,text = "Seleccione un proceso termico", bg = "#56CD63", fg = "black", width = "500", height = "2").pack()
    Button(window_termico,text="Temple",width = "30", height = "2", bg = "white",command=PushTemple).pack()
    Button(window_termico,text="Revenido",width = "30", height = "2", bg = "white",command=PushRevenido).pack()
    Button(window_termico,text="Normalizado",width = "30", height = "2", bg = "white",command=PushNormalizado).pack()
    Button(window_termico,text="Recocido",width = "30", height = "2", bg = "white",command=PushRecocido).pack()

def PushTemple():
    global w_usuario, window_termico, Estado_Termico
    Estado_Termico = "Temple"
    w_usuario.deiconify()
    window_termico.destroy()

def PushRevenido():
    global w_usuario, window_termico, Estado_Termico
    Estado_Termico = "Revenido"
    w_usuario.deiconify()
    window_termico.destroy()

def PushNormalizado():
    global w_usuario, window_termico, Estado_Termico
    Estado_Termico = "Normalizado"
    w_usuario.deiconify()
    window_termico.destroy

def PushRecocido():
    global w_usuario, window_termico, Estado_Termico
    Estado_Termico = "Recocido"
    w_usuario.deiconify()
    window_termico.destroy

def log():
    global login, find_folio
    ventana.iconify()
    login = Toplevel(ventana)
    login.geometry("450x220")
    login.title("Usuario")
    main_title = Label(login ,text = "!Bienvenido!", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    main_title.pack()
    
    find_folio = StringVar()
    
    Labelx = Label(login, text="Ingrese su No. folio", bg = "white")
    Labelx.place(x=0,y=50)

    find_entry = Entry(login,textvariable=find_folio, width="20")
    find_entry.place(x=120,y=52)

    Botonx_Enviar = Button(login, text = "Verificar", width = "5", height = "1", bg = "white", command = look_for_folio)
    Botonx_Enviar.place(x=245, y=50)

    B = Button(login,text="Cerrar",width="30",height="2",bg="red", command=close_login)
    B.pack(side=BOTTOM)

def close_login():

    global login

    login.destroy()
    ventana.deiconify()

def look_for_folio():

    global find_folio

    x_folio = find_folio.get()
    pos_aux = -1
    pivote = 0
    for y in Folios:

        if y == int(x_folio):
            pos_aux = pivote
            #messagebox.showinfo(title="Great",message="Folio en posicion {}".format(pos_aux+1))
            Usuarios[pivote].Venatana_usuario()
        pivote += 1

    if pos_aux == -1:
        messagebox.showwarning(title="Error", message="Folio {} no encontrado".format(x_folio))

def Cerrar():
    ventana.destroy()


#Variables
Usuarios = []
Folios = []
Estado_Termico = ""
Estado_Maquinado = ""
Selec_Paqueteria = ""
bandera = False

#Ventanas
ventana = Tk()
ventana.title("!Machine APP!")
ventana.geometry("250x225")
main_title = Label(text = "!Bienvenido!", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()


Verificar = Button(ventana, text = "Log in", width = "30", height = "2", bg = "white", command = log)
Verificar.pack()
Gerente = Button(ventana,text="Gerente", width = "30", height = "2", bg = "white",command=datos_gerente)
Gerente.pack()
Usuario = Button(ventana,text="Registrar", width = "30", height = "2", bg = "white", command=datos_usuario)
Usuario.pack()
Salir = Button(ventana,text="Salir",width="30",height="2",bg="red", command=Cerrar)
Salir.pack()

ventana.mainloop()