from PatronesDeDiseño.FactoryMethod.Tarea import Tarea

class TareaProgramada:
    def __init__(self,Descripcion):
        self.descripcion = Descripcion

    def Ingresar(self, Tarea):
        print(f"ingreso una tarea programada {Tarea} con la descripcion de: ")
        print(self.descripcion)