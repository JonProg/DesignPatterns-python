from abc import ABC, abstractmethod

class AveVoadora(ABC):
    @abstractmethod
    def voar(self):
        raise "Should implement voar method"
    
    @abstractmethod
    def comer(self):
        raise "Should implement comer method"
    
    @abstractmethod
    def gritar(self):
        raise "Should implement gritar method"


class AveNaoVoadora(ABC):
    @abstractmethod
    def comer(self):
        raise "Should implement comer method"
    
    @abstractmethod
    def gritar(self):
        raise "Should implement gritar method"


"""

Manter os módulos focados em uma única responsabilidade ajuda a reduzir
acoplamentos e aumentar a coesão dentro do código. Isso torna o software mais
modular e independente, facilitando a manutenção e evolução no futuro.

"""
    