# coding=utf-8
# Exercicio_1 - Luiz Henrique Zeferino Junior

class Pessoa(object):

    def __init__(self, altura, peso, idade):
        self.altura = altura
        self.peso = peso
        self.idade = idade
        
    def envelhecer(self):
        self.idade += 1
        if self.idade <= 21:
            self.altura += 1.5
        else:
            self.altura

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg