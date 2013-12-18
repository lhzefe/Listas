# coding=utf-8
# Exercicio_4 - Luiz Henrique Zeferino Junior

import unittest
from should_dsl import should
from controle_de_projetos import Projeto, Avaliador, AvaliadorProjeto, Pesquisador, Integrantes, IntegrantesProjeto, Edital, Bolsista, BolsistaProjeto

class ProjetoSpec(unittest.TestCase):
    
    def test_creates_a_projeto_object(self):
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando',[],[],[],[],[])
        projeto.codigo |should| equal_to('001')
        projeto.titulo |should| equal_to('Banco de Dados')
        projeto.relatorio |should| equal_to('Descritivo')
        projeto.data_de_submissao |should| equal_to('10-01-2014')
        projeto.resumo |should| equal_to('Descricao de Bancos')
        projeto.situacao |should| equal_to('Avaliando')
        projeto.avaliadorprojeto |should| equal_to([])
        projeto.listapesquisador |should| equal_to([])
        projeto.integrantesprojeto |should| equal_to([])
        projeto.listaedital |should| equal_to([])
        projeto.bolsistaprojeto |should| equal_to([])
   
    def test_inserir_avaliador_projeto(self):
        avaliador = Avaliador('001', 'Joao')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        avaliadorprojeto = AvaliadorProjeto('10-10-2013' ,'10-10-2014','Adequado','7.0', avaliador, projeto)
        projeto.inserirAvaliadorProjeto(avaliadorprojeto)
        (avaliadorprojeto in projeto.avaliadorprojeto) |should| equal_to(True) 
    
    def test_verificar_avaliador_projeto(self):
        avaliador = Avaliador('001', 'Joao')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        avaliadorprojeto = AvaliadorProjeto('10-10-2013' ,'10-10-2014','Adequado','7.0', avaliador, projeto)        
        projeto.inserirAvaliadorProjeto(avaliadorprojeto)
        projeto.verificaAvaliadorProjeto(avaliadorprojeto) |should| equal_to(True)
        
    def test_inserir_lista_pesquisador(self):
        pesquisador = Pesquisador('001', 'Pedro', '34567897754', '27778990', 'Rua das granjas', 'granja@hotmail.com')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando') 
        listapesquisador = ('001', 'Pedro', '34567897754', '27778990', 'Rua das granjas', 'granja@hotmail.com')    
        projeto.inserirListaPesquisador(listapesquisador)
        (listapesquisador in projeto.listapesquisador) |should| equal_to(True) 
    
    def test_verificar_lista_pesquisador(self):
        pesquisador = Pesquisador('001', 'Pedro', '34567897754', '27778990', 'Rua das granjas', 'granja@hotmail.com')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        listapesquisador = ('001', 'Pedro', '34567897754', '27778990', 'Rua das granjas', 'granja@hotmail.com')    
        projeto.inserirListaPesquisador(listapesquisador)
        projeto.verificaListaPesquisador(listapesquisador) |should| equal_to(True)
        
    def test_inserir_integrantes_projeto(self):
        integrantes = Integrantes('001', 'Gabriel','34589076621','27899990','Rua dos Andradas 10','gabrielpmonteiro@hotmail.com')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        integrantesprojeto = IntegrantesProjeto('10-02-2013' ,'10-05-2014','Analista','Analista', integrantes, projeto) 
        projeto.inserirIntegrantesProjeto(integrantesprojeto)
        (integrantesprojeto in projeto.integrantesprojeto) |should| equal_to(True) 
    
    def test_verificar_integrantes_projeto(self):
        integrantes = Integrantes('001', 'Gabriel','34589076621','27899990','Rua dos Andradas 10','gabrielpmonteiro@hotmail.com')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        integrantesprojeto = IntegrantesProjeto('10-02-2013' ,'10-05-2014','Analista','Analista', integrantes, projeto)                
        projeto.inserirIntegrantesProjeto(integrantesprojeto)
        projeto.verificaIntegrantesProjeto(integrantesprojeto) |should| equal_to(True)
  
    def test_inserir_lista_edital(self):
        edital = Edital('001', 'Selecao','10-10-2013','10-10-2014')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        listaedital = ('001', 'Selecao','10-10-2013','10-10-2014')
        projeto.inserirListaEdital(listaedital)
        (listaedital in projeto.listaedital) |should| equal_to(True) 
    
    def test_verificar_lista_edital(self):
        edital = Edital('001', 'Selecao','10-10-2013','10-10-2014')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')      
        listaedital = ('001', 'Selecao','10-10-2013','10-10-2014')      
        projeto.inserirListaEdital(listaedital)
        projeto.verificaListaEdital(listaedital) |should| equal_to(True)
  
    def test_inserir_bolsista_projeto(self):
        bolsista = Bolsista('001', 'Joao', '0101', '45678903345', 'Sistemas de Informacao', '4', '10-10-1980','Rua das couves')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        bolsistaprojeto = BolsistaProjeto('10-06-2013' ,'10-06-2014','bolsista','dgti', bolsista, projeto)
        projeto.inserirBolsistaProjeto(bolsistaprojeto)
        (bolsistaprojeto in projeto.bolsistaprojeto) |should| equal_to(True)     
    
    def test_verificar_bolsista_projeto(self):
        bolsista = Bolsista('001', 'Joao', '0101', '45678903345', 'Sistemas de Informacao', '4', '10-10-1980','Rua das couves')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        bolsistaprojeto = BolsistaProjeto('10-06-2013' ,'10-06-2014','bolsista','dgti', bolsista, projeto)
        projeto.inserirBolsistaProjeto(bolsistaprojeto)
        projeto.verificaBolsistaProjeto(bolsistaprojeto) |should| equal_to(True)

class AvaliadorSpec(unittest.TestCase):
    
    def test_creates_a_avaliador_object(self):
        avaliador = Avaliador('001', 'Joao',[])
        avaliador.codigo |should| equal_to('001')
        avaliador.nome |should| equal_to('Joao')
        avaliador.avaliadorprojeto |should| equal_to([])
        
    def test_inserir_avaliador_projeto(self):
        avaliador = Avaliador('001', 'Joao')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        avaliadorprojeto = AvaliadorProjeto('10-10-2013' ,'10-10-2014','Adequado','7.0', avaliador, projeto)
        avaliador.inserirAvaliadorProjeto(avaliadorprojeto)
        (avaliadorprojeto in avaliador.avaliadorprojeto) |should| equal_to(True) 
    
    def test_verificar_avaliador_projeto(self):
        avaliador = Avaliador('001', 'Joao')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        avaliadorprojeto = AvaliadorProjeto('10-10-2013' ,'10-10-2014','Adequado','7.0', avaliador, projeto)
        avaliador.inserirAvaliadorProjeto(avaliadorprojeto)
        avaliador.verificaAvaliadorProjeto(avaliadorprojeto) |should| equal_to(True)
        
class AvaliadorProjetoSpec(unittest.TestCase):
    
    def test_creates_a_avaliador_projeto_object(self):
    
        avaliador = Avaliador('001', 'Joao')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        
        avaliadorprojeto = AvaliadorProjeto('10-10-2013' ,'10-10-2014','Adequado','7.0', avaliador, projeto)
        
        avaliadorprojeto.data_comeco|should| equal_to('10-10-2013')
        avaliadorprojeto.data_entrega |should| equal_to('10-10-2014')
        avaliadorprojeto.parecer|should| equal_to('Adequado')
        avaliadorprojeto.nota |should| equal_to('7.0')
        avaliadorprojeto.avaliador |should| equal_to(avaliador)
        avaliadorprojeto.projeto |should| equal_to(projeto)

class BolsistaSpec(unittest.TestCase):
    
    def test_creates_a_bolsista_object(self):
        bolsista = Bolsista('001', 'Joao', '0101', '45678903345', 'Sistemas de Informacao', '4', '10-10-1980','Rua das couves',[])
        bolsista.codigo |should| equal_to('001')
        bolsista.nome |should| equal_to('Joao')
        bolsista.matricula |should| equal_to('0101')
        bolsista.cpf |should| equal_to('45678903345')
        bolsista.curso |should| equal_to('Sistemas de Informacao')
        bolsista.periodo |should| equal_to('4')
        bolsista.data_de_nascimento |should| equal_to('10-10-1980')
        bolsista.endereco |should| equal_to('Rua das couves')
        bolsista.bolsistaprojeto |should| equal_to([])
        
    def test_inserir_bolsista_projeto(self):
        bolsista = Bolsista('001', 'Joao', '0101', '45678903345', 'Sistemas de Informacao', '4', '10-10-1980','Rua das couves')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        bolsistaprojeto = BolsistaProjeto('10-06-2013' ,'10-06-2014','bolsista','dgti', bolsista, projeto)
        bolsista.inserirBolsistaProjeto(bolsistaprojeto)
        (bolsistaprojeto in bolsista.bolsistaprojeto) |should| equal_to(True) 
    
    
    def test_verificar_bolsista_projeto(self):
        bolsista = Bolsista('001', 'Joao', '0101', '45678903345', 'Sistemas de Informacao', '4', '10-10-1980','Rua das couves')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        bolsistaprojeto = BolsistaProjeto('10-06-2013' ,'10-06-2014','bolsista','dgti', bolsista, projeto)
        bolsista.inserirBolsistaProjeto(bolsistaprojeto)
        bolsista.verificaBolsistaProjeto(bolsistaprojeto) |should| equal_to(True)

class BolsistaProjetoSpec(unittest.TestCase):
    
    def test_creates_a_bolsista_projeto_object(self):
        bolsista = Bolsista('001', 'Joao', '0101', '45678903345', 'Sistemas de Informacao', '4', '10-10-1980','Rua das couves')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        bolsistaprojeto = BolsistaProjeto('10-06-2013' ,'10-06-2014','bolsista','dgti', bolsista, projeto)
        bolsistaprojeto.data_inicio|should| equal_to('10-06-2013')
        bolsistaprojeto.data_fim |should| equal_to('10-06-2014')
        bolsistaprojeto.cargo|should| equal_to('bolsista')
        bolsistaprojeto.setor |should| equal_to('dgti')
        bolsistaprojeto.bolsista |should| equal_to(bolsista)
        bolsistaprojeto.projeto |should| equal_to(projeto)

class EditalSpec(unittest.TestCase):
    
    def test_creates_a_edital_object(self):
        edital = Edital('001', 'Selecao','10-10-2013','10-10-2014')
        edital.codigo |should| equal_to('001')
        edital.nome |should| equal_to('Selecao')
        edital.data_de_inicio |should| equal_to('10-10-2013')
        edital.data_de_termino |should| equal_to('10-10-2014')

class IntegrantesSpec(unittest.TestCase):
    
    def test_creates_a_integrantes_object(self):
        integrantes = Integrantes('001', 'Gabriel','34589076621','27899990','Rua dos Andradas 10','gabrielpmonteiro@hotmail.com',[])
        integrantes.codigo |should| equal_to('001')
        integrantes.nome |should| equal_to('Gabriel')
        integrantes.cpf |should| equal_to('34589076621')
        integrantes.telefone |should| equal_to('27899990')
        integrantes.endereco |should| equal_to('Rua dos Andradas 10')
        integrantes.email |should| equal_to('gabrielpmonteiro@hotmail.com')
        integrantes.integrantesprojeto |should| equal_to([])
        
    def test_inserir_integrantes_projeto(self):
        integrantes = Integrantes('001', 'Gabriel','34589076621','27899990','Rua dos Andradas 10','gabrielpmonteiro@hotmail.com')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        integrantesprojeto = IntegrantesProjeto('10-02-2013' ,'10-05-2014','Analista','Analista', integrantes, projeto)
        integrantes.inserirIntegrantesProjeto(integrantesprojeto)
        (integrantesprojeto in integrantes.integrantesprojeto) |should| equal_to(True) 
    
    def test_verificar_integrantes_projeto(self):
        integrantes = Integrantes('001', 'Gabriel','34589076621','27899990','Rua dos Andradas 10','gabrielpmonteiro@hotmail.com')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        integrantesprojeto = IntegrantesProjeto('10-02-2013' ,'10-05-2014','Analista','Analista', integrantes, projeto)
        integrantes.inserirIntegrantesProjeto(integrantesprojeto)
        integrantes.verificaIntegrantesProjeto(integrantesprojeto) |should| equal_to(True)

class IntegrantesProjetoSpec(unittest.TestCase):
    
    def test_creates_a_integrantes_projeto_object(self):
        integrantes = Integrantes('001', 'Gabriel','34589076621','27899990','Rua dos Andradas 10','gabrielpmonteiro@hotmail.com')
        projeto = Projeto('001', 'Banco de Dados','Descritivo','10-01-2014','Descricao de Bancos','Avaliando')
        integrantesprojeto = IntegrantesProjeto('10-02-2013' ,'10-05-2014','Analista','Analista', integrantes, projeto)
        integrantesprojeto.data_inicio|should| equal_to('10-02-2013')
        integrantesprojeto.data_fim |should| equal_to('10-05-2014')
        integrantesprojeto.cargo|should| equal_to('Analista')
        integrantesprojeto.setor |should| equal_to('Analista')
        integrantesprojeto.integrantes |should| equal_to(integrantes)
        integrantesprojeto.projeto |should| equal_to(projeto)

class PesquisadorSpec(unittest.TestCase):
    
    def test_creates_a_pesquisador_object(self):
        pesquisador = Pesquisador('001', 'Pedro', '34567897754', '27778990', 'Rua das granjas', 'granja@hotmail.com')
        pesquisador.codigo |should| equal_to('001')
        pesquisador.nome |should| equal_to('Pedro')
        pesquisador.cpf |should| equal_to('34567897754')
        pesquisador.telefone |should| equal_to('27778990')
        pesquisador.endereco |should| equal_to('Rua das granjas')
        pesquisador.email |should| equal_to('granja@hotmail.com')