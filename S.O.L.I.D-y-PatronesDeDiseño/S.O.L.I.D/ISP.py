from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def animal(self):
        pass

class Caminar(ABC):
    @abstractmethod
    def caminar(self):
        pass

class Nadar(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Volar(ABC):
    @abstractmethod
    def volar(self):
        pass

class Perro(Animal, Caminar, Nadar):
    def animal(self):
        print("Soy un perro")

    def caminar(self):
        print("El perro está caminando")

    def nadar(self):
        print("El perro está nadando")

boby = Perro()
boby.caminar
boby.nadar


"""
El metodo inncesario para esta clase es el de "Nadar"
"""


"""
El principio de segregación de interfaces nos dice que ninguna clase debe estar obligada a implementar métodos que no necesita.
En este ejemplo, en lugar de tener una sola interfaz Animal con muchos métodos (como caminar, nadar, volar), se han separado en interfaces más pequeñas.
La clase Perro implementa solo las interfaces que necesita (Caminar, Nadar), evitando la implementación de métodos innecesarios como volar.
Así, el código cumple con el principio ISP al proporcionar interfaces específicas.

"""