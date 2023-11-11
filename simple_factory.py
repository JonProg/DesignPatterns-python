from abc import ABC, abstractmethod

class Conta(ABC):
  def __init__(self, numero):
    self.numero = numero

    @abstractmethod
    def sacar(self, value) -> None: ...

class ContaCorrente(Conta):
  def sacar(self, value):
    print(f'Sacando {value} da conta corrente')

class ContaPoupanca(Conta):
    def sacar(self,value):
        print(f'Sacando {value} da conta poupança')

class ContaFactory():
    @staticmethod
    def create_account(tipo:str, numero) -> Conta:
        if tipo == 'CC':
            return ContaCorrente(numero)
        elif tipo == 'CP':  
            return ContaPoupanca(numero)
        else:
            raise ValueError("Tipo de conta inválido")

conta_cc = ContaFactory.create_account('CC', 500)
conta_cp = ContaFactory.create_account('CP', 350)

conta_cc.sacar(100)
conta_cp.sacar(100)

"""

Muito interessante para quando queremos desacoplar classes
e utilizar um factory no lugar.

Sendo as factories úteis quando precisamos criar objetos, mas não queremos
que o código cliente saiba qual classe concreta está sendo instanciada.
Isso permite que o código seja mais flexível e extensível no futuro

"""