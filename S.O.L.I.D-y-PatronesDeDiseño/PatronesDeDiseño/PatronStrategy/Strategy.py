from datetime import datetime

class Tarea:
    def __init__(self, titulo, prioridad, fecha, estado):
        self.titulo = titulo
        self.prioridad = prioridad
        self.fecha = fecha
        self.estado = estado
    def __repr__(self):
        return f"{self.titulo} - {self.prioridad} - {self.fecha} - {self.estado}"

"""
Se implemta la clase tarea, la cual contiene como dice su nombre las tareas por realizar junto con su nombre, prioridad
su fecha y su estado. 
"""
class OrdenamientoEstrategias:
    def ordenar(self, tareas):
        pass
"""
Se crea la clase solicitada de ordenamiento de estrategias, la cual funciona como una interfaz basica de las estrategias 
de ordenamiento. 
"""

class OrdenarPorFecha(OrdenamientoEstrategias):
    def ordenar(self, tareas):
        return sorted(tareas, key=lambda t: t.fecha)

class OrdenarPorPrioridad(OrdenamientoEstrategias):
    def ordenar(self, tareas):
        return sorted(tareas, key=lambda t: t.prioridad)

class OrdenarPorEstado(OrdenamientoEstrategias):
    def ordenar(self, tareas):
        orden_estado = {"pendiente": 1, "en progreso": 2, "completada": 3}
        return sorted(tareas, key=lambda t: orden_estado.get(t.estado, 99))

"""
Se implementan las clases para ordenar las tareas por fechas, prioridad y estado.
se utiliza la funcion "sorted" que nos ayuda a ordenar la lista de tareas.
key=lamda le dice al codigo que debe utilizar para poder ordenar la lista por ejemplo t.fecha

"""

class ContextoOrdenador:
    def __init__(self, estrategia):
        self._estrategia = estrategia  

    def set_estrategia(self, estrategia):
        self._estrategia = estrategia  

    def ordenar(self, tareas):
        return self._estrategia.ordenar(tareas)  
"""
Se crea la clase de "ContextoOrdenador" que es la que usa las estrategias de ordenamiento.
se implemeta la funcion de set_estrategias para intercambiar en cualquier momento, sin necesidad de modificar el codigo.

"""

if __name__ == "__main__":
    tareas = [
        Tarea("Crear codigo para implementar factory method", datetime(2025, 3, 1), 2, "pendiente"),
        Tarea("Crear lista de compras del supermecado", datetime(2025, 4, 27), 1, "en progreso"),
        Tarea("Crear codigo del patron Strategy", datetime(2025, 4, 28), 1, "completada"),
        Tarea("Enviar prueba de los principios SOLID junto con los patrones de diseño", datetime(2025, 5, 2), 3, "pendiente"),
    ]

    ordenador = ContextoOrdenador(OrdenarPorFecha())
    print("Ordenadas por fecha:")
    for tarea in ordenador.ordenar(tareas):
        print(tarea)

    ordenador.set_estrategia(OrdenarPorPrioridad())
    print("Ordenadas por prioridad:")
    for tarea in ordenador.ordenar(tareas):
        print(tarea)

    ordenador.set_estrategia(OrdenarPorEstado())
    print("Ordenadas por estado:")
    for tarea in ordenador.ordenar(tareas):
        print(tarea)
"""
Se crea una lista de tarea para comprobar la funcionalidad del codigo,
Se crea un inicializador con las estrategias a utilizar 
luego se cambia el orden para mostrar las estrategias.

"""