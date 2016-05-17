.. _desafio_b:

Criando uma Câmara com Listas
=============================

Uma lista é um conjunto de coisas, pode ser um conjunto de números, letras, palavras ou qualquer outro objeto.
Em Python a lista é escrita assim: *[<uma coisa>, <outra coisa>]*.

Use os ladrilhos nomeados de A a L para montar a câmara mostrada abaixo, consulte o exercício anterior.

.. image:: /_static/masmorra.jpg

.. code-block:: python

    from circus.circus import circus



    MASMORRA = [[ "AN", "AN", "AN", "AN", "AN", "AN"]
                [ "AN", "AN", "AN", "AN", "AN", "AN"]
                [ "AN", "AN", "AN", "AN", "AN", "AN"]
                [ "AN", "AN", "AN", "AN", "AN", "AN"]
                [ "AN", "AN", "AN", "AN", "AN", "AN"]
                ]

    circus(2)

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

.. note::

    No texto "AN" a primeira letra determina o ladriho e a segunda se está girada para Norte, Leste, Sul ou Oeste.
