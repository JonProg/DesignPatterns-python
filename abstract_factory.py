"""

"""

from abc import ABC, abstractmethod

class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:...

class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:...

class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self):
        print('Carro de luxo ZN está buscando o cliente...')

class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self):
        print('Carro papular ZN está buscando o cliente...')

class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self):
        print('Moto de luxo ZN está buscando o cliente...')

class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self):
        print('Moto popular ZN está buscando o cliente...')

class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self):
        print('Carro de luxo ZS está buscando o cliente...')

class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self):
        print('Carro papular ZS está buscando o cliente...')

class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self):
        print('Moto de luxo ZS está buscando o cliente...')

class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self):
        print('Moto popular ZS está buscando o cliente...')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass

    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular: pass


class ZonaNorteFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()
    
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return MotoLuxoZN()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoPopularZN()
    
    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()


class ZonaSulFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()
    
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return MotoLuxoZS()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoPopularZS()
    
    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZS()


class Cliente:
    def buscar_clientes(self):
        for factory in [ZonaNorteFactory(), ZonaSulFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()

if __name__ == "__main__":
    cliente = Cliente()
    cliente.buscar_clientes()
    
    

