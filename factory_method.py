"""
Factory method é um padrão de criação que permite definir um interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O factory
method permite adiar a instanciação para as subclasses, garantindo o baixo 
acoplamento entre classes. 

"""


from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:...

class CarroLuxo(Veiculo):
    def buscar_cliente(self):
        print('Carro de luxo está buscando o cliente...')

class CarroPopular(Veiculo):
    def buscar_cliente(self):
        print('Carro papular está buscando o cliente...')

class MotoLuxo(Veiculo):
    def buscar_cliente(self):
        print('Moto de luxo está buscando o cliente...')

class MotoPopular(Veiculo):
    def buscar_cliente(self):
        print('Moto popular está buscando o cliente...')


class VeiculoFactory(ABC):
    def __init__(self,type) -> None:
        self.carro = self.get_veiculo(type)
    @staticmethod
    @abstractmethod
    def get_veiculo(type:str) -> Veiculo: pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteFactory(VeiculoFactory):
    @staticmethod
    def get_veiculo(type: str) -> Veiculo:
        if type == 'luxo':
            return CarroLuxo()
        if type == 'popular':
            return CarroPopular()
        if type == 'moto':
            return MotoPopular()
        if type == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veiculo não existe'


class ZonaSulFactory(VeiculoFactory):
    @staticmethod
    def get_veiculo(type: str) -> Veiculo: #Nosso factory_method
        if type == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo não existe'


if __name__ == "__main__":
    from random import choice

    veiculos_disponiveis_zona_norte = ['luxo','popular','moto','moto_luxo']
    veiculos_disponiveis_zona_sul = ['popular']

    print('ZONA NORTE')
    for i in range(10):
        carro = ZonaNorteFactory(
            choice(veiculos_disponiveis_zona_norte)
        )
        carro.buscar_cliente()

    print('ZONA SUL')
    for i in range(10):
        carro2 = ZonaSulFactory(
            choice(veiculos_disponiveis_zona_sul)
        )
        carro2.buscar_cliente()
    
    

