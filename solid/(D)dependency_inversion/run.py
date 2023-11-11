from db.interface import DataBase
from db.mongo_db import MongoDb
from db.mysql_db import MysqlDb

class User():
    def __init__(self,database:DataBase) -> None:
        self.__database = database
    
    def armazenar_dado(self,dado:any):
        return self.__database.inserir(dado)

    def deletar_dado(self,dado:any):
        return self.__database.inserir(dado)

user_mongo = User(MongoDb())
user_mysql = User(MysqlDb())

user_mongo.armazenar_dado('Olha que legal')
user_mysql.armazenar_dado('Olha que bacana')


"""
O Princípio da Inversão da Dependência (PID) diz que módulos de alto nível não devem
depender de módulos de baixo nível. Ambos devem depender de abstrações.
Igualmente ao nosso exemplo onde temos uma classe de usuário que não depende 
diretamente de uma classe de banco de dados,más sim de uma interface
que representa o banco de dados abstratamente.

Isso permite que você substitua implementações facilmente.
Por exemplo, você pode começar usando um banco de dados SQL real e depois
mudar para um banco de dados em memória para testes, sem alterar o código da
classe de usuário.

"""