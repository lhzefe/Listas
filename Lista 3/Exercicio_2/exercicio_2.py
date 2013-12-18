# coding=utf-8
# Exercicio_2 - Luiz Henrique Zeferino Junior

class PaisFronteira(object):
    
    def __init__(self, nome, capital, tamanho, paises_em_fronteira=[]):
        self.nome = nome
        self.capital = capital
        self.tamanho = tamanho
        self.paises_em_fronteira = paises_em_fronteira
        
    def inserir_paises_em_fronteira(self, pais):
        self.paises_em_fronteira.append(pais)
    
    def verificar_fronteira(self):
        return self.paises_em_fronteira        

    def verificar_igualdade(self, pais):
        if self.nome == pais.nome and self.capital == pais.capital:
            return True
        return False
               
    def mostrar_paises_em_fronteira(self, pais):
        paises = []
        for x in pais.paises_em_fronteira:
            if x in self.paises_em_fronteira:
                paises.append(x)
        return paises