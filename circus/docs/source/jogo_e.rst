.. _jogo_e:


Cena com Muitos Ladrilhos Girados
=================================

Vamos montar a masmorra original, bem maior. Em vez de copiar várias vezes o código,
vamos usar um *dicionário* de *tuplas* e o comando *for*
A folha de ladrilhos continua esta:


.. image:: /_static/DungeonWall.jpg

Procure reproduzir este labirinto:

.. image:: /_static/masmorra.jpg

.. code-block:: python

    from _spy.circus.game import Circus

    A, B, C, D, E, F, G = 0, 128, 256, 256+128, 512, 512+128, 512+256


    class Jogo(Circus):
        """Essa  é a classe Jogo que recebe os poderes da classe Circus necessários para criar um jogo"""
        MOSAICO = {
        (A, A): (5, 90), (B, A): (5, 90), (C, A):(5, 90), (D, A):(5, 90), (E, A):(5, 90), (F, A):(5, 90), (G, A):(5, 90),
        (A, B): (5, 90), (B, B): (5, 90), (C, B):(5, 90), (D, B):(5, 90), (E, B):(5, 90), (F, B):(5, 90), (G, B):(5, 90),
        (C, C): (5, 90), (B, C): (5, 90), (C, C):(5, 90), (D, C):(5, 90), (E, C):(5, 90), (F, C):(5, 90), (G, C):(5, 90),
        (D, D): (5, 90), (B, D): (5, 90), (C, D):(5, 90), (D, D):(5, 90), (E, D):(5, 90), (F, D):(5, 90), (G, D):(5, 90),
        (E, E): (5, 90), (B, E): (5, 90), (C, E):(5, 90), (D, E):(5, 90), (E, E):(5, 90), (F, E):(5, 90), (G, E):(5, 90),
       }  # este é um dicionário de tuplas. Cada chave é a posição do ladrilho e cada tupla dá o ladrilho (5) e o ângulo (90)

        def preload(self):
            """Aqui no preload carregamos os recursos usados no jogo, neste caso a folha de ladrilhos"""
            self.spritesheet("ladrilho", "http://<advinha!>", 128, 128, 12)

        def create(self):
            """Aqui colocamos cada ladrilho indicando a posição na tela e depois selecionando o ladrilho"""
            for (x, y), (frame, angle) in self.MOSAICO.items():
               # coloque o resto aqui

    if __name__ == "__main__":
        Jogo()

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

.. note::
   Observe que ao colocar a âncora no centro do ladrilho, este centro também servirá para posicionar o ladrilho.
   Ajuste as cordenadas para que tudo fique correto.
