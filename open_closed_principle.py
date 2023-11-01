
class Player():

    def jogar_carta(self, carta):
        carta.ataque()

class DragaoDeOlhosAzuis():
    
    def ataque(self):
        print('Dragão de olhos azuis atacando...')

class RedReign():
    
    def ataque(self):
        print('Red Reign atacando...')

yugi = Player()
card_dragao = DragaoDeOlhosAzuis()
card_reign = RedReign()

yugi.jogar_carta(card_dragao)
yugi.jogar_carta(card_reign)

""" Na programação orientada a objeto, o princípio do aberto/fechado estabelece 
que "entidades de software (classes, módulos, funções, etc.) devem ser abertas 
para extensão, mas fechadas para modificação"

Algo que é demonstrado pela nossa classe onde o jogador pode jogar qualquer carta que 
tenha o metodo ".ataque()" e para forçamos isso teriamos que implementar um classe
abstrata.
"""
