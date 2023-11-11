from interface import AveVoadora, AveNaoVoadora

class Sabia(AveVoadora):
    def comer(self):
        print('Sabiá está comendo...')
    
    def gritar(self):
        print('PIU PIU PIU')
    
    def voar(self):
        print('Sabiá está voando...')

class Avestruz(AveNaoVoadora):
    def comer(self):
        print('Avestruz está comendo...')
    
    def gritar(self):
        print('Avestruz está gritando...')
        self.__correr
    
    def __correr(self):
        print('Agora o avestruz está correndo...')