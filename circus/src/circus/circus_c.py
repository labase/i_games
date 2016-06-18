from _spy.circus.game import Circus, Actor
from random import random

DIR = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


class Jogo(Circus):
    """Essa  é a classe Jogo que recebe os poderes da classe Circus de poder criar um jogo"""

    def __init__(self):
        super().__init__()  # super é invocado aqui para preservar os poderes recebidos do Circus
        self.ladrilho_monstro = "monstro"
        self.monstro = Monstro(self.ladrilho_monstro, 20, 100, 100)

    def preload(self):
        """Aqui no preload carregamos a imagem masmorra e a folha de ladrilhos dos monstros"""
        self.image("fundo", "https://s19.postimg.org/uhvf97m4z/masmorra.jpg")
        self.spritesheet(self.ladrilho_monstro, "https://s19.postimg.org/ldsev0v6b/monstersheets.png", 64, 63, 16 * 12)

    def create(self):
        """Aqui colocamos a imagem masmorra na tela do jogo"""
        self.sprite("fundo")
        self.startSystem()
        # self.game.physics.startSystem(self.gamer.PHASER.Physics.ARCADE)
        print(self.gamer.PHASER)


class Monstro(Actor):
    """Essa  é a classe Monstro que controla os personagens do jogo"""

    def __init__(self, nome, frame, x, y):
        super().__init__()
        self.nome, self.frame, self.x, self.y = nome, frame, x, y
        self.first = True
        self.direction = 0
        self.monstro = None

    def create(self):
        """Aqui colocamos o sprite do monstro e selecionamos o frame que o representa"""
        self.monstro = self.sprite(self.nome, self.x, self.y)
        self.monstro.frame = self.frame
        self.monstro.anchor.setTo(0.5, 0.5)
        self.monstro.animations.add('mon', [self.frame, self.frame + 1, self.frame + 2, ], 4, True)
        self.monstro.play('mon')
        self.enable(self.monstro)
        # self.monstro.body.setCircle(28)

    def update(self):
        player = self.monstro

        def redirect():
            self.first = False
            self.direction = d = int(random() * 8.0)
            x, y = DIR[d]
            return x * 150, y * 150

        player.angle = (self.direction * 45 + 270) % 360
        if int(random() + 0.02) or self.first:
            player.body.velocity.x, player.body.velocity.y = redirect()


if __name__ == "__main__":
    Jogo()
