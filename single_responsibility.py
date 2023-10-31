
class ClassEnemys():
    def __init__(self, life, name, attack) -> None:
        self.life = life
        self.name = name
        self.attack = attack


class ClassPlayers():
    def __init__(self, life, name, attack) -> None:
        self.life = life
        self.name = name
        self.attack = attack
    
    def attack_enemy(self,enemy:ClassEnemys):
        enemy.life -= self.attack
        self.__message_game()

    def __message_game(self) -> None:
        print(f'O inimigo sofreu um dano de {self.attack}')


samurai = ClassPlayers(700,'Sekiro',50)
orc = ClassEnemys(800,'Orc',20)

samurai.attack_enemy(orc)
print(orc.life)

