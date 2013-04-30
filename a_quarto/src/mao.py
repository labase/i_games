"""
############################################################
Quarto - Mao
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/02
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
from peca import Peca
class Mao:
    """Espaco do jogo onde as pecas iniciam"""
    def __init__(self, gui):
        
        self.pecas = []
        self.build(gui)
    def build(self, gui):
        self.pecas = [Peca(gui) for i in range(8)]
