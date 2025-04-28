import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PatronesDeDiseño.FactoryMethod.Tarea import Tarea
from PatronesDeDiseño.FactoryMethod.TareaNormal import TareaNormal
from PatronesDeDiseño.FactoryMethod.TareaProgramada import TareaProgramada
from PatronesDeDiseño.FactoryMethod.TareaUrgente import TareaUrgente
from PatronesDeDiseño.FactoryMethod.TareaFactory import TareaFactory
from PatronesDeDiseño.PatronDecorador import TareaConAdjunto

def main():
    tipo = input("Ingrese el caracter de la tarea a realizar: ").lower()
    descripcion =input("ingrese una descripcion: ")
    


    try:
        tarea = TareaFactory.CrearTarea(tipo,descripcion)
        tarea.Ingresar("")
    except ValueError as e:
        print(e)
        return
    
     
    adjunto = input("¿Desea agregar un archivo? (s/n): ").lower()
    print(f"Respuesta sobre el adjunto: {adjunto}")  

    if adjunto == "s":
        archivo = input("Ingrese el nombre del archivo adjunto: ")
        print(f"Archivo ingresado: {archivo}")  
        tarea = TareaConAdjunto(tarea, archivo)

    print("Resultado final de la tarea:")
    print(tarea.mostrar())
        
if __name__ == "__main__":
    main()


"""
Este código le pide al usuario que ingrese el tipo y la descripción de una tarea, y luego crea la tarea correspondiente 
usando la fábrica TareaFactory. Si la tarea es válida, le pregunta al usuario si desea agregar un archivo adjunto. 
Si acepta, se agrega el archivo usando el decorador TareaConAdjunto. Finalmente, muestra la descripción de la tarea, 
con o sin el archivo adjunto, dependiendo de lo que haya decidido el usuario.

"""