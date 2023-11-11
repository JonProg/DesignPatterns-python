from abc import ABC, abstractmethod

class DataBase(ABC):

    @abstractmethod
    def inserir(self, data):...

    @abstractmethod
    def deletar(self, data):...