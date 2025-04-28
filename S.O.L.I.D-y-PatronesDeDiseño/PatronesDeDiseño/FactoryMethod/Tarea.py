class Tarea:
    def Ingresar(self,Tarea):
        raise NotImplementedError("Se debe ingresar una tarea que corresponda")
    
    def mostrar(self):
        return f"descripcion de la tarea"
    
"""
Esta es mi clase tarea, la cual funciona como la clase base de la jerarquia de las tareas, junto con el metodo "Ingresar"
que debera ser implementado por las otras subclases, junto con un metodo "mostrar", esta clase servira como plantilla para la 
creacion de mis clases posteriores.
"""