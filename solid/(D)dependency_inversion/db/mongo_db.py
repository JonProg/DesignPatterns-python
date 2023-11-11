from .interface import DataBase

class MongoDb(DataBase):

    def inserir(self, data):
        print(f'Inserindo o valor [{data}] no banco Mongo DB')
    
    def deletar(self, data):
        print(f'Deletando o valor [{data}] do banco Mongo DB')