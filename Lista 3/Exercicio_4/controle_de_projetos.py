# coding=utf-8
# Exercicio_4 - Luiz Henrique Zeferino Junior

class Projeto:
    def __init__(self,codigo,titulo,relatorio,data_de_submissao,resumo,
                situacao,avaliadorprojeto=[],listapesquisador=[],
                integrantesprojeto=[],listaedital=[],bolsistaprojeto=[]):
        self.codigo = codigo
        self.titulo = titulo
        self.relatorio = relatorio
        self.data_de_submissao = data_de_submissao
        self.resumo = resumo
        self.situacao = situacao
        self.avaliadorprojeto = avaliadorprojeto
        self.listapesquisador = listapesquisador
        self.integrantesprojeto = integrantesprojeto
        self.listaedital = listaedital
        self.bolsistaprojeto = bolsistaprojeto
        
    def inserirAvaliadorProjeto(self,avaliadorprojeto):
        self.avaliadorprojeto.append(avaliadorprojeto)
    
    def verificaAvaliadorProjeto(self,avaliadorprojeto):
        return avaliadorprojeto in self.avaliadorprojeto

    def inserirListaPesquisador(self,listapesquisador):
        self.listapesquisador.append(listapesquisador)
    
    def verificaListaPesquisador(self,listapesquisador):
        return listapesquisador in self.listapesquisador

    def inserirIntegrantesProjeto(self,integrantesprojeto):
        self.integrantesprojeto.append(integrantesprojeto)
    
    def verificaIntegrantesProjeto(self,integrantesprojeto):
        return integrantesprojeto in self.integrantesprojeto

    def inserirListaEdital(self,listaedital):
        self.listaedital.append(listaedital)
    
    def verificaListaEdital(self,listaedital):
        return listaedital in self.listaedital
 
    def inserirBolsistaProjeto(self,bolsistaprojeto):
        self.bolsistaprojeto.append(bolsistaprojeto)
    
    def verificaBolsistaProjeto(self,bolsistaprojeto):
        return bolsistaprojeto in self.bolsistaprojeto

class Avaliador:
    def __init__(self,codigo,nome,avaliadorprojeto=[]):
        self.codigo = codigo
        self.nome = nome
        self.avaliadorprojeto = avaliadorprojeto
        
    def inserirAvaliadorProjeto(self,avaliadorprojeto):
        self.avaliadorprojeto.append(avaliadorprojeto)
    
    def verificaAvaliadorProjeto(self,avaliadorprojeto):
        return avaliadorprojeto in self.avaliadorprojeto

class AvaliadorProjeto:

    def __init__(self,data_comeco,data_entrega,parecer,nota,avaliador,projeto):
        self.data_comeco = data_comeco
        self.data_entrega = data_entrega
        self.parecer = parecer
        self.nota = nota
        self.avaliador = avaliador
        self.projeto = projeto

class Bolsista:
    def __init__(self,codigo,nome,matricula,cpf,curso,periodo,data_de_nascimento,endereco,bolsistaprojeto=[]):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.curso = curso
        self.periodo = periodo
        self.data_de_nascimento = data_de_nascimento
        self.endereco = endereco      
        self.bolsistaprojeto = bolsistaprojeto
        
    def inserirBolsistaProjeto(self,bolsistaprojeto):
        self.bolsistaprojeto.append(bolsistaprojeto)
    
    def verificaBolsistaProjeto(self,bolsistaprojeto):
        return bolsistaprojeto in self.bolsistaprojeto

class BolsistaProjeto:

    def __init__(self,data_inicio,data_fim,cargo,setor,bolsista,projeto):  
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.cargo = cargo
        self.setor = setor
        self.bolsista = bolsista
        self.projeto = projeto

class Edital:
    def __init__(self,codigo,nome,data_de_inicio,data_de_termino):
        self.codigo = codigo
        self.nome = nome
        self.data_de_inicio = data_de_inicio
        self.data_de_termino = data_de_termino

class Integrantes:
    def __init__(self,codigo,nome,cpf,telefone,endereco,email,integrantesprojeto=[]):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email        
        self.integrantesprojeto = integrantesprojeto
    
    def inserirIntegrantesProjeto(self,integrantesprojeto):
        self.integrantesprojeto.append(integrantesprojeto)
    
    def verificaIntegrantesProjeto(self,integrantesprojeto):
        return integrantesprojeto in self.integrantesprojeto

class IntegrantesProjeto:

    def __init__(self,data_inicio,data_fim,cargo,setor,integrantes,projeto):
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.cargo = cargo
        self.setor = setor
        self.integrantes = integrantes
        self.projeto = projeto

class Pesquisador:
    def __init__(self,codigo,nome,cpf,telefone,endereco,email):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email