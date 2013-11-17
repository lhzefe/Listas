# coding=utf-8
# Exercicio_6 - Luiz Henrique Zeferino Junior

def validar_data(dia, mes, ano):
    dia, mes, ano = int(dia), int(mes), int(ano)
    if (dia>0 and dia<31 and mes>0 and mes<13 and ano>=0 and ano<10000):
        return True
    else:
        return False

def data_por_extenso(data):
    meses = ['janeiro',
             'fevereiro',
             'março',
             'abril', 
             'maio', 
             'junho', 
             'julho', 
             'agosto', 
             'setembro', 
             'outubro', 
             'novembro', 
             'dezembro']
    dia, mes, ano = int(data[0:2]), int(data[2:4]), int(data[4:8])
    print dia,'de',meses[mes-1],'de',ano

dia = raw_input('Digite o dia(DD): ')
mes = raw_input('Digite o mes(MM): ')
ano = raw_input('Digite o ano(AAAA): ')

validar_data(dia, mes, ano)

if validar_data(dia, mes, ano) == True:
    data = dia + mes + ano
    data_por_extenso(data)
else:
    print 'Null'