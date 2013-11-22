# coding=utf-8
# Exercicio_5 - Luiz Henrique Zeferino Junior

def verifica_data():
    data = raw_input('diga o dia(DD): ')
    data += raw_input('diga o mês(MM): ')
    data += raw_input('diga o ano(AAAA): ')
    dia, mes, ano = int(data[0:2]), int(data[2:4]), int(data[4:8])
    print dia,'/', mes,'/', ano,''
    valida = 'true'
    x=0
    while valida == 'true' and x == 0:
        if (ano%4 == 0 and ano%100!= 0) or\
        ano%400 == 0:
            bissexto = 'true'
        else:
            bissexto = 'false'

        if mes < 1 or mes > 12:
            valida = 'false'

        if dia > 31 or ((mes == 4 or mes ==\
        6 or mes == 9 or mes == 11) and dia > 30):
            valida = 'false'

        if (mes == 2 and bissexto == 'false'\
        and dia > 28) or ( mes == 2 and bissexto\
        == 'true' and dia > 29):
            valida = 'false'
        x+=1

    if valida == 'true':
        print('é uma data válida')
    else:
        print('não é uma data válida')

verifica_data()