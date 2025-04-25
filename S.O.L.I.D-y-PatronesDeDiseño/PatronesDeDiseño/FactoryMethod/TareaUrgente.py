from PatronesDeDiseño.FactoryMethod.Tarea import Tarea

class TareaUrgente(Tarea):

    def __init__(self,Descripcion):
        self.descripcion = Descripcion

    def Ingresar(self, Tarea):
        print(f"ingreso una tarea urgente {Tarea} con la descripcion de: ")
        print(self.descripcion)