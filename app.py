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


