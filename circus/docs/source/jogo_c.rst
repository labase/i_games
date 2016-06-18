.. _jogo_c:


Cena com Ladrilhos Girados
==========================

Vamos montar uma outra masmorrra, mas que agora requer que rotacionemos os ladrilhos.
Veja os comando *angle* e *anchor* no código.
A folha de ladrilhos continua esta:


.. image:: /_static/DungeonWall.jpg

Procure reproduzir este labirinto:

.. image:: /_static/masmorra2.jpg

.. code-block:: python

    from _spy.circus.game import Circus


    class Jogo(Circus):
        """Essa  é a classe Jogo que recebe os poderes da classe Circus necessários para criar um jogo"""

        def preload(self):
            """Aqui no preload carregamos os recursos usados no jogo, neste caso a folha de ladrilhos"""
            self.spritesheet("ladrilho", "http://<advinha!>", 128, 128, 12)

        def create(self):
            """Aqui colocamos cada ladrilho indicando a posição na tela e depois selecionando o ladrilho"""
            um_ladrilho = self.sprite("ladrilho", 0, 0)
            um_ladrilho.frame = 5  # este número seleciona o ladrilho que vai ser colocado
            um_ladrilho.anchor.setTo(0.5, 0.5)  # este comando faz com que a rotação seja no centro do ladrilho
            um_ladrilho.angle = 90  # está é a rotação em graus do ladrilho
            um_ladrilho = self.sprite("ladrilho", 0, 0)  # mude a posição do ladrilho
            um_ladrilho.frame = 5  # troque o ladrilho!
            um_ladrilho.anchor.setTo(0.5, 0.5)
            um_ladrilho.angle = 90  # troque o ângulo!
            # Coloque aqui o resto dos ladrilhos

    if __name__ == "__main__":
        Jogo()

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

.. note::
   Observe que ao colocar a âncora no centro do ladrilho, este centro também servirá para posicionar o ladrilho.
   Ajuste as cordenadas para que tudo fique correto.
