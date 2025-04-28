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

"""
Se implementa el patron "Decorator" el cual nos ayuda a extender la funcionalidad de nuestra clase tarea para asi no alterar
nuestra clase base tarea, que fue creada con el patron factory method

Para este caso se implemento el patron factory method junto con el patron decorator, el cual creamos dos subclases el decorador en si
y el "tarea con adjunto" el cual nos permite agregar un archivo como lo sugerido en el documento, por su puesto profesor logre
implementar un codigo que si agregue un archivo, pero lo intente.

"""