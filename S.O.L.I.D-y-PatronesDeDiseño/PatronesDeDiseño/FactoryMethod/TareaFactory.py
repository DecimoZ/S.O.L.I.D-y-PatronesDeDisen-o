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