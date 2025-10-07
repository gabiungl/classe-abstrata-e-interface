from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def emitir_som(self):
        pass

    def descrever(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos"


class IVoador(ABC):
    @abstractmethod
    def voar(self):
        pass


class INadador(ABC):
    @abstractmethod
    def nadar(self):
        pass


class Mamifero(Animal):
    pass


class Ave(Animal):
    pass


class Leao(Mamifero):
    def emitir_som(self):
        return "Rugido"


class Pinguim(Ave, INadador):
    def emitir_som(self):
        return "Gack"

    def nadar(self):
        return "O pinguim está nadando"


class Aguia(Ave, IVoador):
    def emitir_som(self):
        return "Piau!"

    def voar(self):
        return "A águia está voando"
