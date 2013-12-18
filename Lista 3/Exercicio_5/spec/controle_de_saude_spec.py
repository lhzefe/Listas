# coding=utf-8
# Exercicio_5 - Luiz Henrique Zeferino Junior

import unittest
from should_dsl import should
from controle_de_saude import Usuario, Alimentos, TreinoExercicio, Treino, Refeicao, Historico, Exercicios, UsuarioTreino

class UsuarioSpec(unittest.TestCase):
    
    def test_creates_a_usuario_object(self):
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        usuario.cod_usuario |should| equal_to('001')
        usuario.nome |should| equal_to('Pedro')
        usuario.peso |should| equal_to('70')
        usuario.altura |should| equal_to('1.70')
        usuario.gordura_corporal |should| equal_to('10')
        usuario.nivel_atividade_fisica |should| equal_to('1')
        usuario.calorias_a_consumir |should| equal_to('5')
        usuario.sexo |should| equal_to('m')
        usuario.valor_metabolico |should| equal_to('1')
        usuario.massa_magra |should| equal_to('15')
        usuario.peso_gordura |should| equal_to('10')
        usuario.peso_gordura_ideal |should| equal_to('5')
        usuario.peso_ideal |should| equal_to('65')
        usuario.peso_a_perder |should| equal_to('5')
        usuario.idade |should| equal_to('20')
        
    def test_inserir_usuario_treino(self):
        treino = Treino('001', 'Joao','100','4 horas','14:00','10-12-2013')
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        usuariotreino = UsuarioTreino('001','001','001',treino,usuario)
        usuario.inserirUsuarioTreino(usuariotreino)
        (usuariotreino in usuario.usuariotreino) |should| equal_to(True) 
    
    def test_verificar_usuario_treino(self):
        treino = Treino('001', 'Joao','100','4 horas','14:00','10-12-2013')
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        usuariotreino = UsuarioTreino('001','001','001',treino, usuario)
        usuario.inserirUsuarioTreino(usuariotreino)
        usuario.verificaUsuarioTreino(usuariotreino) |should| equal_to(True)
 
    def test_inserir_refeicao(self):
        alimentos = Alimentos('001', 'laranja','frutas','1','20','10','20','5')
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        refeicao = Refeicao('001','001','001', 'Arroz', '100','12:00',alimentos,usuario)
        usuario.inserirRefeicao(refeicao)
        (refeicao in usuario.refeicao) |should| equal_to(True) 
    
    def test_verificar_refeicao(self):
        alimentos = Alimentos('001', 'laranja','frutas','1','20','10','20','5')
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        refeicao = Refeicao('001','001','001', 'Arroz', '100','12:00',alimentos,usuario)
        usuario.inserirRefeicao(refeicao)
        usuario.verificaRefeicao(refeicao) |should| equal_to(True)

class AlimentosSpec(unittest.TestCase):
    
    def test_creates_a_alimentos_object(self):
        alimentos = Alimentos('001', 'laranja','frutas','1','20','10','20','5')
        alimentos.cod_alimento |should| equal_to('001')
        alimentos.nome |should| equal_to('laranja')
        alimentos.categoria |should| equal_to('frutas')
        alimentos.quantidade |should| equal_to('1')
        alimentos.calorias |should| equal_to('20')
        alimentos.proteinas |should| equal_to('10')
        alimentos.carboidratos |should| equal_to('20')
        alimentos.gorduras |should| equal_to('5')
        
    def test_inserir_refeicao(self):
        alimentos = Alimentos('001', 'laranja','frutas','1','20','10','20','5')
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        refeicao = Refeicao('001','001','001', 'Arroz', '100','12:00',alimentos,usuario)
        alimentos.inserirRefeicao(refeicao)
        (refeicao in alimentos.refeicao) |should| equal_to(True) 
    
    def test_verificar_refeicao(self):
        alimentos = Alimentos('001', 'laranja','frutas','1','20','10','20','5')
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        refeicao = Refeicao('001','001','001', 'Arroz', '100','12:00',alimentos,usuario)
        alimentos.inserirRefeicao(refeicao)
        alimentos.verificaRefeicao(refeicao) |should| equal_to(True)

class TreinoExercicioSpec(unittest.TestCase):
    
    def test_creates_a_treino_exercicio_object(self):
        treino = Treino('001', 'Joao','100','4 horas','14:00','10-12-2013')
        exercicios = Exercicios('001', 'Supino Reto','100','3','1 minuto','6 minutos')
        treinoexercicio = TreinoExercicio('001','001','001', treino,exercicios)
        treinoexercicio.cod_treinoExercicio|should| equal_to('001')
        treinoexercicio.cod_treino |should| equal_to('001')
        treinoexercicio.cod_exercicio |should| equal_to('001')
        treinoexercicio.treino |should| equal_to(treino)
        treinoexercicio.exercicios |should| equal_to(exercicios)

class TreinoSpec(unittest.TestCase):
    
    def test_creates_a_treino_object(self):
        treino = Treino('001', 'Joao','100','4 horas','14:00','10-12-2013')
        treino.cod_treino |should| equal_to('001')
        treino.nome |should| equal_to('Joao')
        treino.total_calorias_gastas |should| equal_to('100')
        treino.tempo_total |should| equal_to('4 horas')
        treino.horario |should| equal_to('14:00')
        treino.data |should| equal_to('10-12-2013')
     
    def test_inserir_treino_exercicio(self):
        treino = Treino('001', 'Joao','100','4 horas','14:00','10-12-2013')
        exercicios = Exercicios('001', 'Supino Reto','100','3','1 minuto','6 minutos')
        treinoexercicio = TreinoExercicio('001','001','001',treino,exercicios)
        treino.inserirTreinoExercicio(treinoexercicio)
        (treinoexercicio in treino.treinoexercicio) |should| equal_to(True) 
    
    def test_verificar_treino_exercicio(self):
        treino = Treino('001', 'Joao','100','4 horas','14:00','10-12-2013')
        exercicios = Exercicios('001', 'Supino Reto','100','3','1 minuto','6 minutos')
        treinoexercicio = TreinoExercicio('001','001','001',treino, exercicios)
        treino.inserirTreinoExercicio(treinoexercicio)
        treino.verificaTreinoExercicio(treinoexercicio) |should| equal_to(True)
 
    def test_inserir_usuario_treino(self):
        treino = Treino('001', 'Joao','100','4 horas','14:00','10-12-2013')
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        usuariotreino = UsuarioTreino('001','001','001',treino,usuario)
        treino.inserirUsuarioTreino(usuariotreino)
        (usuariotreino in treino.usuariotreino) |should| equal_to(True) 
    
    def test_verificar_usuario_treino(self):
        treino = Treino('001', 'Joao','100','4 horas','14:00','10-12-2013')
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        usuariotreino = UsuarioTreino('001','001','001',treino, usuario)
        treino.inserirUsuarioTreino(usuariotreino)
        treino.verificaUsuarioTreino(usuariotreino) |should| equal_to(True)

class RefeicaoSpec(unittest.TestCase):
    
    def test_creates_a_refeicao_object(self):
        alimentos = Alimentos('001', 'laranja','frutas','1','20','10','20','5')
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        refeicao = Refeicao('001','001','001', 'Arroz', '100','12:00',alimentos,usuario)
        refeicao.cod_refeicao|should| equal_to('001')
        refeicao.cod_usuario |should| equal_to('001')
        refeicao.cod_alimento |should| equal_to('001')
        refeicao.nome |should| equal_to('Arroz')
        refeicao.total_calorias |should| equal_to('100')
        refeicao.horario |should| equal_to('12:00')
        refeicao.alimentos |should| equal_to(alimentos)
        refeicao.usuario |should| equal_to(usuario)

class HistoricoSpec(unittest.TestCase):
    
    def test_creates_a_historico_object(self):
        historico = Historico('001', '80','30','Em exercicio','110',[])
        historico.cod_historico |should| equal_to('001')
        historico.peso_atual |should| equal_to('80')
        historico.peso_perdido |should| equal_to('30')
        historico.situacao |should| equal_to('Em exercicio')
        historico.saldo_calorias |should| equal_to('110')
        historico.listausuario |should| equal_to([])
        
    def test_inserir_lista_usuario(self):
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        historico = Historico('001', '80','30','Em exercicio','110')
        listausuario = ('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        historico.inserirListaUsuario(listausuario)
        (listausuario in historico.listausuario) |should| equal_to(True) 
    
    def test_verificar_lista_usuario(self):
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        historico = Historico('001', '80','30','Em exercicio','110')
        listausuario = ('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        historico.inserirListaUsuario(listausuario)
        historico.verificaListaUsuario(listausuario) |should| equal_to(True)

class ExerciciosSpec(unittest.TestCase):
    
    def test_creates_a_exercicios_object(self):
        exercicios = Exercicios('001', 'Supino Reto','100','3','1 minuto','6 minutos')
        exercicios.cod_exercicio |should| equal_to('001')
        exercicios.nome |should| equal_to('Supino Reto')
        exercicios.calorias_gastas |should| equal_to('100')
        exercicios.numero_series |should| equal_to('3')
        exercicios.tempo_descanso |should| equal_to('1 minuto')
        exercicios.tempo_exercicio |should| equal_to('6 minutos')
        
    def test_inserir_treino_exercicio(self):
        treino = Treino('001', 'Joao','100','4 horas','14:00','10-12-2013')
        exercicios = Exercicios('001', 'Supino Reto','100','3','1 minuto','6 minutos')
        treinoexercicio = TreinoExercicio('001','001','001', treino, exercicios)
        exercicios.inserirTreinoExercicio(treinoexercicio)
        (treinoexercicio in exercicios.treinoexercicio) |should| equal_to(True) 
    
    def test_verificar_treino_exercicio(self):
        treino = Treino('001', 'Joao','100','4 horas','14:00','10-12-2013')
        exercicios = Exercicios('001', 'Supino Reto','100','3','1 minuto','6 minutos')
        treinoexercicio = TreinoExercicio('001','001','001',treino, exercicios)
        exercicios.inserirTreinoExercicio(treinoexercicio)
        exercicios.verificaTreinoExercicio(treinoexercicio) |should| equal_to(True)

class UsuarioTreinoSpec(unittest.TestCase):
    
    def test_creates_a_usuario_treino_object(self):
        treino = Treino('001', 'Joao','100','4 horas','14:00','10-12-2013')
        usuario = Usuario('001', 'Pedro','70','1.70','10','1','5','m','1','15','10','5','65','5','20')
        usuariotreino = UsuarioTreino('001','001','001', treino, usuario)
        usuariotreino.cod_usuarioTreino|should| equal_to('001')
        usuariotreino.cod_treino |should| equal_to('001')
        usuariotreino.cod_usuario |should| equal_to('001')
        usuariotreino.treino |should| equal_to(treino)
        usuariotreino.usuario |should| equal_to(usuario)