class ServicioNotificacion: #Clase base 
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def enviar(self):
        raise NotImplementedError("Este método debe ser implementado por una clase hija")

"""
Con la funcion "enviar" defino un metodo abstracto, el cual me permite heredar de esta clase a otra su propia 
version del metodo enviar con esto puedo extender la clase base cumpliendo con el principio abierto y cerrado 
"""
class Email(ServicioNotificacion):
    def enviar(self):
        print(f"Notificación enviada por Email: {self.mensaje}")


class SMS(ServicioNotificacion):
    def enviar(self):
        print(f"Notificación enviada por SMS: {self.mensaje}")

email = Email("facturacion de aiep ya fue procesada para su pago")
sms = SMS("Su pago se a realizado con exito ")

email.enviar()
sms.enviar()

"""
Se refactoriza el código para cumplir con el principio de abierto/cerrado, creando una clase base llamada 
ServicioNotificacion, la cual contiene el método 'enviar'. De esta forma, podemos extender la funcionalidad 
creando nuevas clases hijas sin modificar la clase base, cumpliendo así con el principio de abierto/cerrado.
"""