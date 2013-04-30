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
from tabuleiro import Tabuleiro
from mao import Mao
def main(doc):
  print('Quarto 0.1.0')

class Quarto:
    """Base do jogo com tabuleiro e duas maos."""
    def __init__(self, gui):
        """Constroi as partes do Jogo. """
        self.build_base(gui)
        #self.build_tabuleiro(gui)
        #self.build_mao(gui)
        
    def build_base(self,gui):
        """docs here"""
        #gui.rect(x=10, y= 10, width=800, heigth=600)
    def build_tabuleiro(self,gui):
        """docs here"""
        self.tabuleiro =Tabuleiro(gui)
    def build_mao(self,gui):
        """docs here"""
        self.mao1 =Mao(gui)
        #gui.rect(x=10, y= 10, width=800, heigth=600)
    #: TODO - put all the rest

