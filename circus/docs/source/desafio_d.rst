.. _desafio_d:

Fazer o herói andar com  uma função
===================================

Uma função é um conjunto de operações realizadas com um  parâmetro dado.
Utilizamos def para criar uma função e return para retornar o resultado dela.

Exemplo: Quando queremos saber o troco que receberemos quando compramos algo, diminuímos o dinheiro dado pelo preço do
produto. Poderíamos então escrever a função troco:

.. code-block:: python

    def troco(pagamento, preço)
         return (preço - pagamento)

Pagamento e preço são os parâmetros da função. Eles devem ser informados para que ela possa ser calculada.
Agora que a função está definida, podemos chamar troco(30,20), e o valor retornado será 10.

Para o nosso jogo, vamos criar uma função andar, que determina se o herói irá andar ao precionarmos as setas do teclado.
Retorne **True** se você quiser que a ação seja verdadeira. Se não quiser que o herói ande, retorne **False**.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

.. note::

    Dica: Nem toda função precisa de parâmetro

.. code-block:: python

    from circus.circus import circus


    # def andar():
    #    return True

    circus(4, andar)
