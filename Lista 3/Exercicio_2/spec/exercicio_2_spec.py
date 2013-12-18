# coding=utf-8
# Exercicio_2 - Luiz Henrique Zeferino Junior

import unittest
from should_dsl import should
from exercicio_2 import PaisFronteira

class TestPaisFronteira(unittest.TestCase):

    def setUp(self):
        self.pais = PaisFronteira("polonia", "varsóvia", "517000", [])

    def test_criar_pais(self):
        self.pais.nome |should| equal_to("polonia")
        self.pais.capital |should| equal_to("varsóvia")
        self.pais.tamanho |should| equal_to ("517000")
        self.pais.paises_em_fronteira |should| equal_to([])
        
        
    def test_inserir_pais_em_fronteira(self):
        self.polonia = PaisFronteira("polonia", "varsóvia", "517000", [])
        self.alemanha = PaisFronteira("alemanha", "berlim", "357051", [])
        self.polonia.inserir_paises_em_fronteira(self.alemanha) 
        paises = [] 
        paises.append(self.alemanha)
        self.polonia.paises_em_fronteira |should| equal_to(paises) 
            
    def test_verificar_fronteira(self):
        self.polonia = PaisFronteira("polonia", "varsóvia", "517000", [])
        self.alemanha = PaisFronteira("alemanha", "berlim", "357051", [])
        self.franca = PaisFronteira("frança", "paris", "543965", [])
        self.polonia.inserir_paises_em_fronteira(self.alemanha)
        self.polonia.inserir_paises_em_fronteira(self.franca)
        paises = []
        paises.append(self.alemanha)
        paises.append(self.franca)
        self.polonia.verificar_fronteira() |should| equal_to(paises)
        
    def test_verificar_igualdade(self):
        self.polonia = PaisFronteira("polonia", "varsóvia", "517000", [])
        self.alemanha = PaisFronteira("alemanha", "berlim", "357051", [])
        self.alemanha.verificar_igualdade(self.polonia) |should| equal_to(False)
        
    def test_mostrar_paises_em_fronteira(self):
        self.polonia = PaisFronteira("polonia", "varsóvia", "517000", [])
        self.alemanha = PaisFronteira("alemanha", "berlim", "357051", [])
        self.franca = PaisFronteira("frança", "paris", "543965", [])   
        self.austria = PaisFronteira("austria", "viena", "83879", [])
        paises = []
        paises.append(self.franca)
        self.polonia.inserir_paises_em_fronteira(self.franca)
        self.polonia.inserir_paises_em_fronteira(self.alemanha)
        self.alemanha.inserir_paises_em_fronteira(self.franca)        
        self.alemanha.inserir_paises_em_fronteira(self.austria)
        self.polonia.mostrar_paises_em_fronteira(self.alemanha) |should| equal_to(paises)
        
