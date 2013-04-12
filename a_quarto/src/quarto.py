"""
############################################################
Quarto - Principal - Base
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/09
:Status: This is a "work in progress"
:Revision: 0.1.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
def main(doc):
  print('Quarto 0.1.0')

class Quarto:
    """Base do jogo com tabuleiro e duas maos."""
    def __init__(self):
        """Constroi as partes do Jogo. """
        self.build_base()
        self.build_tabuleiro()
        self.build_mao()
        
    def build_base(self):
        """docs here"""
    #: TODO - put all the rest

