# coding=utf-8
# Exercicio_1 - Luiz Henrique Zeferino Junior

import unittest
from should_dsl import should
from exercicio_1 import Pessoa

class TestExercicio1(unittest.TestCase):

    def setUp(self):
        self.Pessoa = Pessoa(170, 65, 18)

    def test_valores(self):
        self.Pessoa.altura |should| equal_to(170)
        self.Pessoa.peso |should| equal_to(65)
        self.Pessoa.idade |should| equal_to(18)

    def test_envelhecer(self):
        self.Pessoa.idade = 20
        self.Pessoa.altura = 170
        self.Pessoa.envelhecer()
        self.Pessoa.idade |should| equal_to(21)
        self.Pessoa.altura |should| equal_to(171.5)

        self.Pessoa.idade = 24
        self.Pessoa.altura = 183
        self.Pessoa.envelhecer()
        self.Pessoa.idade |should| equal_to(25)
        self.Pessoa.altura |should| equal_to(183)

    def test_engordar(self):
        self.Pessoa.peso = 70
        self.Pessoa.engordar(10)
        self.Pessoa.peso |should| equal_to(80)

    def test_emagrecer(self):
        self.Pessoa.peso = 70
        self.Pessoa.emagrecer(10)
        self.Pessoa.peso |should| equal_to(60)