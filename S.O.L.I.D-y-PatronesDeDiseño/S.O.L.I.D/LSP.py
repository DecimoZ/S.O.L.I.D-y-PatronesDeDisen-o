class Ave:
    def Moverse(self):
        return "El ave se está moviendo"

class AveVoladora(Ave):
    def Volar(self):
        return "Ahora puede volar"

class Pinguino(Ave):
    def Nadar(self):
        return "El pingüino está nadando"

class MartinPescador(AveVoladora):
    pass

def PoderVolar(ave_voladora: AveVoladora):
    print(ave_voladora.Volar())

mi_martin_pescador = MartinPescador()

PoderVolar(mi_martin_pescador)

"""
El principio de LSP dice que las clase base o padre puede ser remplazada por alguna 
clase hija y el codigo deberia poder seguir funcionando, en el caso del codigo que nos 
proporciono la violacion a este principio se encuentra cuando vemos que la clase hija "pingüino" 
tiene la funcion de volar, como sabemos que esta ave no tiene esa capacidad, por ende la clase hija
no puede reemplazar a la clase padre que es "Ave" 
"""

"""
Al refactorizar el código, creé una clase hija llamada AveVoladora que hereda de Ave, 
con el objetivo de diferenciar entre las aves que pueden volar y las que no. De esta forma, 
solo las clases que realmente pueden volar heredan la función Volar(), 
cumpliendo así con el Principio de Sustitución de Liskov. Esto evita que clases como Pinguino hereden 
métodos que no deberían tener.

"""