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
from mocker import MockerTestCase, Mocker,KWARGS, ARGS, ANY, CONTAINS, MATCH, expect

#from unittest import TestCase
from quarto import Quarto

class TestQuarto(MockerTestCase):
  """Testes unitários para o Quarto"""

  def setUp(self):
    self.mock_gui = Mocker()
    self.mg = self.mock_gui.mock()
    self.ma = self.mock_gui.mock()

  def tearDown(self):
    self.mock_gui.restore()
    self.mock_gui.verify()
    self.mock_avt = None
    self.app = None

  def test_init(self):
    expect(self.mg.rect( KWARGS))
    self.mock_gui.replay()
    self.app = Quarto(self.mg)

if __name__ == '__main__':
    import unittest
    unittest.main()