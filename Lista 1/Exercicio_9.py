# coding=utf-8
# Exercicio_9 - Luiz Henrique Zeferino Junior

def valores(dinheiro_hora, horas_trabalho):
    salario_bruto= dinheiro_hora*dinheiro_hora*30
    ir=(salario_bruto * 11/100.0)
    inss=(salario_bruto * 8/100.0)
    sindicato=(salario_bruto * 5/100.0)
    desconto=ir+inss+sindicato
    salario_liquido=salario_bruto-desconto

    print 'Salário bruto: %.2f' %salario_bruto
    print 'IR: %.2f' %ir
    print 'INSS: %.2f' %inss
    print 'sindicato: %.2f' %sindicato
    print 'salario_liquido: %.2f'   %salario_liquido

dinheiro_hora, horas_trabalho=input('Diga R$ por hora: '),\
input('Diga horas trabalhadas: ')

valores(dinheiro_hora, horas_trabalho)