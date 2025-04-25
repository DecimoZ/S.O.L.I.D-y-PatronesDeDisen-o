from PatronesDeDiseño.FactoryMethod.Tarea import Tarea

class TareaNormal(Tarea):
    def __init__(self, Descripcion):
        self.descripcion = Descripcion
        
    def Ingresar(self, Tarea):
        print(f"ingreso una tarea normal {Tarea} con la descripcion de: ")
        print(self.descripcion)
        
    def mostrar(self):
        return f"Tarea normal: {self.descripcion}"