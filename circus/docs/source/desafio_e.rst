.. _desafio_e:

Matar o monstro com if
======================

Operadores condicionais analisam se uma condição está sendo satisfeita para que algo possa ser realizado.
Os mais utilizados são if e else. If significa "se" e else "caso contrário"

Esses operadores detrminam a condição.A condição determinada por else só será analisada se a condição determinada pelo if
for falsa. Após definir a condição, devemos usar dois pontos e na linha de baixo determinar o que será realizado.

Um exemplo:

.. code-block:: python

    if x == 2:
       y = 3
    else:
       y = 1

Iremos agora criar uma função matar_monstro para matar o monstro se o personagem passar por cima dele. UTilize if para
isso. Se o herói não encostar no mosntro, o personagem não deve morrer. A função deve retornar True ou False. Utilize
como parâmetros a posição do herói e do monstro (posição_heroi = (heroi_x, heroi_y). posição_monstro = (monstro_x, monstro_y)

.. note::

    Dica: Um personagem encosta no outro quando suas posições são iguais.

.. code-block:: python

    from circus.circus import circus

    # def matar_monstro():
    #     if posição_heroi == posição_mostro:
    #        return True
    #     else:
    #        return False

    circus(5, matar_monstro)
