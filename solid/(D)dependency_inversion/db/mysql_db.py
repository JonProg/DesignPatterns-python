from .interface import DataBase

class MysqlDb(DataBase):

    def inserir(self, data):
        print(f'Inserindo o valor [{data}] no banco MySQL')
    
    def deletar(self, data):
        print(f'Deletando o valor [{data}] do banco MySQL')