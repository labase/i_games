.. _jogo_g:


Colocando Mais Personagens
==========================

Vamos criar outros monstros.
A operação *[f(x) for x in <Coleção>]* gera uma lista varrendo
a Coleção dada e executando a função f(x) para cada x na Coleção.


.. image:: /_static/monstersheets.png

.. code-block:: python

   from _spy.circus.game import Circus, Actor

   MONSTROS = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]


   class Jogo(Circus):
      """Essa  é a classe Jogo que recebe os poderes da classe Circus de poder criar um jogo"""
      def __init__(self):
         super().__init__()  # super é invocado aqui para preservar os poderes recebidos do Circus
         self.ladrilho_monstro = "monstro"
         self.monstro = [Monstro(self.ladrilho_monstro, frame, x, y) for frame, x, y in MONSTROS]

      def preload(self):
         """Aqui no preload carregamos a imagem masmorra e a folha de ladrilhos dos monstros"""
         self.image("fundo", "http://<descubra um jeito de achar a url que vai ser posta aqui>")
         self.spritesheet(self.ladrilho_monstro, "http://<advinha!>", 64, 63, 16*12)

      def create(self):
         """Aqui colocamos a imagem masmorra na tela do jogo"""
         self.sprite("fundo")


   class Monstro(Actor):
      """Essa  é a classe Monstro que controla os personagens do jogo"""
      def __init__(self, nome, frame, x, y):
         super().__init__()
         self.nome, self.frame, self.x, self.y = nome, frame, x, y

      def create(self):
         """Aqui colocamos o sprite do monstro e selecionamos o frame que o representa"""
         self.monstro = "<troque isto pela criação do sprite, use self.nome, self.x e self.y>"
         "escolha aqui o frame e use self.frame"
         self.monstro.anchor.setTo(0.5, 0.5)

   if __name__ == "__main__":
     Jogo()

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

