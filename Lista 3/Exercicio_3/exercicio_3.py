# coding=utf-8
# Exercicio_3 - Luiz Henrique Zeferino Junior

import random

class Cartas(object):

    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    @property
    def nome(self):
        if self.valor == 14:
            return 'Ás'
        elif self.valor == 12:
            return 'Rainha'
        elif self.valor == 13:
            return 'Rei'        
        elif self.valor == 11:
            return 'Valete'        
        else:
            return str(self.valor)

    def __repr__(self):
        return self.nome + ' de ' + self.naipe

class Baralho(object):

    def __init__(self):
        self.cartas = []
        self._encher_baralho()

    def _encher_baralho(self):
        for naipe in ['Paus', 'Ouro', 'Copas', 'Espadas']:
            for valor in range(2, 15):
                self.cartas.append(Cartas(naipe, valor))

    def embaralhar(self):
        random.shuffle(self.cartas)

    def pegar_carta(self):
        try:
            return self.cartas.pop(-1)
        except IndexError:
            raise BaralhoVazio('Não tem mais carta no baralho.')

    def mostrar_cartas(self):
        lista_de_cartas = ''
        for carta in self.cartas:
            lista_de_cartas += repr(carta) +'\n'
        return lista_de_cartas


class Mesa(object):
    def __init__(self, baralhos):
        if len(baralhos) != 2:
            raise Exception('É preciso ter dois jogadores.')
        self.baralhos = baralhos
        self.lixo = []
        self.jogadores = []
        self.tira1 = []
        self.tira2 = []

    def pegar_carta(self):
            escolha = random.choice([0, 1])
            baralho = self.baralhos[escolha]
            try:
                return baralho.pegar_carta()
            except BaralhoVazio:
                baralho = self.baralhos[escolha ^ 1]
                return baralho.pegar_carta()

    def colocar_para_o_lixo(self, carta):
        self.lixo.append(carta)

    def cadastrar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def distribuir_carta(self):
        self.baralhos[0].embaralhar()
        self.baralhos[1].embaralhar()
        for i in range(0,11):
            for jogador in self.jogadores:
                jogador.cartas_do_jogador.append(self.pegar_carta())
            self.tira1.append(self.pegar_carta())
            self.tira2.append(self.pegar_carta())


class Jogador(object):

    def __init__(self, mesa):
        self.mesa = mesa
        self.mesa.cadastrar_jogador(self)
        self.cartas_do_jogador = []

    def escolher_carta(self):
        self.cartas_do_jogador.append(self.mesa.pegar_carta())

    def jogar_carta(self, naipe, valor):
        for carta in self.cartas_do_jogador:
            if carta.naipe == naipe and carta.valor == valor:
                carta_para_jogar = self.cartas_do_jogador.index(carta)
                self.mesa.colocar_para_o_lixo(self.cartas_do_jogador.pop(carta_para_jogar))
                break

    def mostrar_cartas_do_jogador(self):
        lista_de_cartas = ''
        for carta in self.cartas_do_jogador:
            lista_de_cartas += repr(carta) + '\n'
        return lista_de_cartas

class BaralhoVazio(Exception):
    pass