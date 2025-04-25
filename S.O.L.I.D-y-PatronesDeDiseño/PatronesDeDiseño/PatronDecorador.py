from PatronesDeDiseño.FactoryMethod.Tarea import Tarea

class TareaDecorador(Tarea):
    def __init__(self, tarea):
        self.tarea = tarea

    def mostrar(self):
        return self.tarea.mostrar()

class TareaConAdjunto(TareaDecorador):
    def __init__(self, tarea: Tarea, nombre_archivo: str):
        super().__init__(tarea)
        self.archivo = nombre_archivo

    def mostrar(self):
        return f"{self.tarea.mostrar()} [Archivo adjunto: {self.archivo}]"