class Reporte:
    def __init__(self, reporte=""):
        self.reporte = reporte

    def Guardar_reporte(self):
        self.reporte = input("Escriba su reporte: ")
        print("Reporte Guardado: " + self.reporte)
        return self.reporte

class Envio_reporte:
    def __init__(self, correo="", reporte=""):
        self.correo = correo
        self.reporte = reporte

    def Enviar(self):
        self.correo = input("Escriba su correo: ")
        print("Su reporte ha sido enviado con el correo " + self.correo + " y el reporte fue: " + self.reporte)


nuevo_reporte = Reporte()
contenido_reporte = nuevo_reporte.Guardar_reporte()


envio = Envio_reporte(reporte=contenido_reporte)
envio.Enviar()

"""
Logre identificar que la clase Generador de reporte aparte de guardarla, tambien la envia 
por correo asi violando el principio de responsabilidad unica, para poder corregir el codigo, se separa la clase de generar 
reporte con la de enviar asi cumpliendo con el principio SRP.
"""