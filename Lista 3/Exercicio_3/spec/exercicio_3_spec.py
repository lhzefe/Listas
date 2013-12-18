# coding=utf-8
# Exercicio_3 - Luiz Henrique Zeferino Junior

import unittest
from should_dsl import should, should_not
from exercicio_3 import Cartas, Baralho, Mesa, Jogador, BaralhoVazio

class TestCarta(unittest.TestCase):

    def setUp(self):
        self.carta = Cartas('Ouro', 11)

    def test_criar_carta(self):
        self.carta.valor |should| equal_to(11)
        self.carta.naipe |should| equal_to('Ouro')

    def test_nome_da_carta(self):
        self.carta.nome |should| equal_to('Valete')


class TestBaralho(unittest.TestCase):

    def setUp(self):
        self.baralho = Baralho()

    def test_baralho_de_52_cartas(self):
        len(self.baralho.cartas) |should| equal_to(52)

    def test_embaralhar_baralho(self):
        cartas = list(self.baralho.cartas)
        self.baralho.embaralhar()
        cartas |should_not| equal_to(self.baralho.cartas)

    def test_pegar_carta(self):
        carta = self.baralho.pegar_carta()
        self.baralho.cartas |should_not| contain(carta)

    def test_excecao_para_baralho_vazio(self):
        for valor in range(52):
            self.baralho.pegar_carta()
        (self.baralho.pegar_carta, ) |should| throw(BaralhoVazio)

    def test_mostrar_cartas(self):
        self.baralho.cartas = []
        self.baralho.cartas.append(Cartas('Ouro', 14))
        self.baralho.cartas.append(Cartas('Ouro', 13))
        self.baralho.mostrar_cartas() |should| equal_to('Ás de Ouro\nRei de Ouro\n')


class TestMesa(unittest.TestCase):

    def setUp(self):
        self.mesa = Mesa([Baralho(), Baralho()])

    def test_dois_jogadores(self):
        len(self.mesa.baralhos) |should| equal_to(2)

    def test_pegar_carta_do_jogador(self):
        self.mesa.pegar_carta() |should| be_kind_of(Cartas)

    def test_colocar_no_lixo(self):
        carta = self.mesa.pegar_carta()
        self.mesa.colocar_para_o_lixo(carta)
        self.mesa.lixo |should| contain(carta)

    def test_cadastro_de_jogador(self):
        class Jogador: pass
        self.mesa.cadastrar_jogador(Jogador())

    def test_baralho_vazio(self):
        for i in range(104):
            self.mesa.pegar_carta()
        (self.mesa.pegar_carta, ) |should| throw(BaralhoVazio)

    def test_distribuir_carta(self):
        class Jogador:
            def __init__(self):
                self.cartas_do_jogador = []
        joao = Jogador()
        maria = Jogador()
        self.mesa.cadastrar_jogador(joao)
        self.mesa.cadastrar_jogador(maria)
        self.mesa.distribuir_carta()
        len(joao.cartas_do_jogador) |should| equal_to(11)
        len(maria.cartas_do_jogador) |should| equal_to(11)

class TestJogador(unittest.TestCase):

    def setUp(self):
        mesa = Mesa([Baralho(), Baralho()])
        self.jogador = Jogador(mesa)
        mesa.distribuir_carta()

    def test_jogador_com_onze_cartas(self):
        len(self.jogador.cartas_do_jogador) |should| equal_to(11)

    def test_escolher_carta(self):
        carta = self.jogador.escolher_carta()
        len(self.jogador.cartas_do_jogador) |should| equal_to(12)

    def test_jogar_carta(self):
        carta = self.jogador.cartas_do_jogador[-1]
        self.jogador.jogar_carta(carta.naipe, carta.valor)
        len(self.jogador.cartas_do_jogador) |should| equal_to(10)

    def test_cartas_do_jogador(self):
        self.jogador.cartas_do_jogador = []
        self.jogador.cartas_do_jogador.append(Cartas('Ouro', 14))
        self.jogador.cartas_do_jogador.append(Cartas('Ouro', 13))
        self.jogador.mostrar_cartas_do_jogador() |should| equal_to('Ás de Ouro\nRei de Ouro\n')