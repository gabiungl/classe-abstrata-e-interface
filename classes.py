from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    @abstractmethod
    def emitir_som(self):
        pass

    def descrever(self):
        return f"Nome: {self.__nome}, Idade: {self.__idade} anos"


class IVoador(ABC):
    @abstractmethod
    def voar(self):
        pass


class INadador(ABC):
    @abstractmethod
    def nadar(self):
        pass


class Mamifero(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        return "####"


class Ave(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        return "****"


class Leao(Mamifero):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        return "Rugido"


class Pinguim(Ave, INadador):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        return "Gack"

    def nadar(self):
        return "O pinguim está nadando"


class Aguia(Ave, IVoador):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        return "Pia"

    def voar(self):
        return "A águia está voando"
