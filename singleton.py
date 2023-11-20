"""
O Singleton tem a intenção de garantir que uma classe tenha somente
um instância e fornece i ponto global de acesso para a mesma. 

"""

def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
    
    return get_class


@singleton
class AppSettings:
    def __init__(self) -> None:
        self.tema = 'Tema Darck'
    
if __name__ == "__main__":
    set1 = AppSettings()
    set1.tema = 'TEMA CLARO'

    set2 = AppSettings()
    print(set2.tema)

