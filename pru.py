import smtplib

Subject = "Prueba python"
message = "Hola amix, un mensaje desde Python!"
message="Subject: {}\n\n{}".format(Subject,message)
username = "monicasarahicardosopatino9@gmail.com"
password = "cardoso19"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
server.sendmail(username,"horaciopena007@gmail.com",message)
server.quit()
print ("Correo enviado exitosamente")