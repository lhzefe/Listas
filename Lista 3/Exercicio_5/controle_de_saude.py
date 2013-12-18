# coding=utf-8
# Exercicio_5 - Luiz Henrique Zeferino Junior

class Usuario(object):

    def __init__(self,cod_usuario,nome,peso,altura,gordura_corporal,
                nivel_atividade_fisica,calorias_a_consumir,sexo,
                valor_metabolico,massa_magra,peso_gordura,
                peso_gordura_ideal,peso_ideal,peso_a_perder,idade,
                usuariotreino=[],refeicao=[]):
        self.cod_usuario = cod_usuario
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.gordura_corporal = gordura_corporal
        self.nivel_atividade_fisica = nivel_atividade_fisica
        self.calorias_a_consumir = calorias_a_consumir
        self.sexo = sexo
        self.valor_metabolico = valor_metabolico
        self.massa_magra = massa_magra
        self.peso_gordura = peso_gordura
        self.peso_gordura_ideal = peso_gordura_ideal
        self.peso_ideal = peso_ideal
        self.peso_a_perder = peso_a_perder
        self.idade = idade 
        self.usuariotreino = usuariotreino    
        self.refeicao = refeicao
        
    def inserirUsuarioTreino(self,usuariotreino):
        self.usuariotreino.append(usuariotreino)
    
    def verificaUsuarioTreino(self,usuariotreino):
        return usuariotreino in self.usuariotreino
        
    def inserirRefeicao(self,refeicao):
        self.refeicao.append(refeicao)
    
    def verificaRefeicao(self,refeicao):
        return refeicao in self.refeicao    
        
class Alimentos(object):

    def __init__(self,cod_alimento,nome,categoria,quantidade,calorias,
                proteinas,carboidratos,gorduras,refeicao=[]):
        self.cod_alimento = cod_alimento
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.calorias = calorias
        self.proteinas = proteinas
        self.carboidratos = carboidratos
        self.gorduras = gorduras
        
        self.refeicao = refeicao    
    
    def inserirRefeicao(self,refeicao):
        self.refeicao.append(refeicao)
    
    def verificaRefeicao(self,refeicao):
        return refeicao in self.refeicao   

class TreinoExercicio(object):

    def __init__(self,cod_treinoExercicio ,cod_treino ,cod_exercicio,
                treino, exercicios ):
    
        self.cod_treinoExercicio = cod_treinoExercicio        
        self.cod_treino = cod_treino        
        self.cod_exercicio = cod_exercicio        
        self.treino = treino        
        self.exercicios = exercicios

class Treino(object):

    def __init__(self,cod_treino,nome,total_calorias_gastas,tempo_total,
                horario,data,treinoexercicio=[],usuariotreino=[]):
        self.cod_treino = cod_treino
        self.nome = nome
        self.total_calorias_gastas = total_calorias_gastas
        self.tempo_total = tempo_total
        self.horario = horario
        self.data = data
        self.treinoexercicio = treinoexercicio
        self.usuariotreino = usuariotreino
        
    def inserirTreinoExercicio(self,treinoexercicio):
        self.treinoexercicio.append(treinoexercicio)
    
    def verificaTreinoExercicio(self,treinoexercicio):
        return treinoexercicio in self.treinoexercicio

    def inserirUsuarioTreino(self,usuariotreino):
        self.usuariotreino.append(usuariotreino)
    
    def verificaUsuarioTreino(self,usuariotreino):
        return usuariotreino in self.usuariotreino
        
class Refeicao(object):

    def __init__(self,cod_refeicao ,cod_usuario ,cod_alimento ,nome,
                total_calorias,horario,alimentos,usuario):
    
        self.cod_refeicao = cod_refeicao        
        self.cod_usuario = cod_usuario        
        self.cod_alimento = cod_alimento        
        self.nome = nome        
        self.total_calorias = total_calorias
        self.horario = horario
        self.alimentos = alimentos
        self.usuario = usuario

class Historico(object):

    def __init__(self,cod_historico,peso_atual,peso_perdido,situacao,
                saldo_calorias,listausuario=[]):
        self.cod_historico = cod_historico
        self.peso_atual = peso_atual
        self.peso_perdido = peso_perdido
        self.situacao = situacao
        self.saldo_calorias = saldo_calorias
        self.listausuario = listausuario
    
    def inserirListaUsuario(self,listausuario):
        self.listausuario.append(listausuario)
    
    def verificaListaUsuario(self,listausuario):
        return listausuario in self.listausuario

class Exercicios(object):

    def __init__(self,cod_exercicio,nome,calorias_gastas,numero_series,
                tempo_descanso,tempo_exercicio, treinoexercicio=[]):
        self.cod_exercicio = cod_exercicio
        self.nome = nome
        self.calorias_gastas = calorias_gastas
        self.numero_series = numero_series
        self.tempo_descanso = tempo_descanso
        self.tempo_exercicio = tempo_exercicio
    
        self.treinoexercicio = treinoexercicio
        
    def inserirTreinoExercicio(self,treinoexercicio):
        self.treinoexercicio.append(treinoexercicio)
    
    def verificaTreinoExercicio(self,treinoexercicio):
        return treinoexercicio in self.treinoexercicio

class UsuarioTreino(object):

    def __init__(self,cod_usuarioTreino ,cod_treino ,cod_usuario ,treino, usuario ):
        self.cod_usuarioTreino = cod_usuarioTreino        
        self.cod_treino = cod_treino        
        self.cod_usuario = cod_usuario        
        self.treino = treino        
        self.usuario = usuario