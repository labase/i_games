from circus.circus_a import Circus


class Jogo(Circus):
    """Essa  é a classe Jogo que recebe os poderes da classe Circus de poder criar um jogo"""

    def preload(self):
        """Aqui no preload carregamos os recursos usados no jogo, neste caso a imagem masmorra"""
        self.image("fundo", "http://i-games.readthedocs.io/en/latest/_images/masmorra.jpg")

    def create(self):
        """Aqui colocamos a imagem masmorra na tela do jogo"""
        self.sprite("fundo")

if __name__ == "__main__":
    Jogo()
