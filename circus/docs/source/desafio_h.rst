.. _desafio_h:

Criando uma Câmara com Dicionário
=================================

Uma lista é um conjunto de coisas, pode ser um conjunto de números, letras, palavras ou qualquer outro objeto.
Em Python a lista é escrita assim: *{<umnome: umvalo>,  <outronome: outrovalor>}*.

Use os ladrilhos nomeados de A a L para montar a câmara mostrada abaixo, consulte o exercício A.
Descubra quais posições os nomes misteriosos indicam.

.. image:: /_static/masmorra2.jpg

.. code-block:: python

    from circus.circus import circus

    MASMORRA = {'Cahuitz': 'AN', 'Cauha': 'AN', 'Coycol': 'AN',
     'Huatlya': 'AN', 'Micpe': 'AN', 'Nenea': 'AN',
     'Pallotl': 'AN', 'Tetlah': 'AN', 'Zitllo': 'AN'}


    circus(3, MASMORRA)

.. moduleauthor:: Gabriel Bastos <gab-bass@poli.ufrj.br> / Philipe  < ? >

.. note::

    No texto "AN" a primeira letra determina o ladrilho e a segunda se está girada para Norte, Leste, Sul ou Oeste.
