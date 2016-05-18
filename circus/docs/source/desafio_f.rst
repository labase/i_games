.. _desafio_f:

Criando Vários Monstros
=======================

O comando *for* caminha em uma lista e executa o conjunto de comandos indicado para cada elemento.
Em Python o for é escrito assim: *for <elemento> in <lista>:*.
Se cada elemento da lista for outra lista, você pode colocar vários elementos separados por vírgualas, veja:

*for <elemento0>, <elemento1> in <lista com listas>:*

Complete a lista de elementos com coordenadas para diversos monstros
 e chame a função *posiciona_monstro()* para cada um deles.

.. code-block:: python

    from circus.circus import posiciona_monstro

    # lista_de_posições = [(0, 0, 0), (<>), <>]

    # for <> :
    #     <>

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

.. note::

    Na tripla ordenada (0, 1, 2) o 0 serve para usar a figura de monstro 0, o 1 para colocar o monstro na posição x=1 e o 2 na posição y=2.
