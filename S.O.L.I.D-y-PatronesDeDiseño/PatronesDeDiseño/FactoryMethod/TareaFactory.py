from PatronesDeDiseño.FactoryMethod.Tarea import Tarea
from PatronesDeDiseño.FactoryMethod.TareaNormal import TareaNormal
from PatronesDeDiseño.FactoryMethod.TareaProgramada import TareaProgramada
from PatronesDeDiseño.FactoryMethod.TareaUrgente import TareaUrgente

class TareaFactory:
    @staticmethod
    def CrearTarea(Ingresar_tarea, descripcion):
        if Ingresar_tarea == "normal":
            return TareaNormal(descripcion)
        elif Ingresar_tarea == "programada":
            return TareaProgramada(descripcion)
        elif Ingresar_tarea == "urgente":
            return TareaUrgente(descripcion)
        else:
            raise ValueError("Debe ingresar una tarea que sea normal, programada o urgente")

"""
Esta parte del codigo se usa para crear diferentes tipos de tareas según lo que ingrese el usuario 
(normal, programada o urgente). Según el tipo de tarea, se crea una instancia correspondiente de la clase adecuada. 
Si el tipo de tarea no es válido, lanza un error. Es una forma de centralizar la creación de objetos y 
hacer que el código sea más flexible y fácil de extender.


"""