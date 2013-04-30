#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Quarto - Teste
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
import unittest
from quarto import Quarto

class TestQuarto(unittest.TestCase):

    def setUp(self):
        self.app = Quarto(None)

    def test_tabuleiro(self):
        # garante que tem casas no tabuleiro
        self.app.build_tabuleiro(None)
        t = self.app.tabuleiro
        self.assertEqual(len(t.casas),16)
    def test_mao(self):
        # garante que tem pecas na mao
        self.app.build_mao(None)
        m = self.app.mao1
        self.assertEqual(len(m.pecas),8)


if __name__ == '__main__':
    unittest.main()