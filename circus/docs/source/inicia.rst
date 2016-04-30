.. _modulo_inicia:

Primeiro Cenário do Jogo
========================

Vamos começar importando o browser e o crafty para criar um jogo
baseado na biblioteca Crafty que vai executar no documento "pydiv"


.. code-block:: python

    def main():
        from crafty import Crafty
        from browser import document
        # Cria uma janela de 512x512 para o jogo na divisão do documento pydiv
        jogo = Crafty(512, 512, document["pydiv"])
        #Cria um pano de fundo para o jogo usando a imagem stage-bg
        jogo.e("2D, Canvas, Image")\
            .attr(x=0, y=0, w=512, h=512).image("images/stage-bg.png")

    if __name__ == "__main__":
        main()

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

.. note::
   Ainda é um programa bem simples.
