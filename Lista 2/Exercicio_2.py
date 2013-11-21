# coding=utf-8
# Exercicio_2 - Luiz Henrique Zeferino Junior

def troco(valor_conta, valor_pago):
    troco=valor_pago-valor_conta
    return troco

def troco_minimo_notas(troco):
    if (troco/50) != 0:
        notas=troco/50
        troco=troco%50
        print '%d nota(s) de 50 reais' %notas
    if (troco/20) != 0:
        notas=troco/20
        troco=troco%20
        print '%d nota(s) de 20 reais' %notas
    if (troco/10) != 0:
        notas=troco/10
        troco=troco%10
        print '%d nota(s) de 10 reais' %notas
    if (troco/5) != 0:
        notas=troco/5
        troco=troco%5
        print '%d nota(s) de 5 reais' %notas
    if (troco/2) != 0:
        notas=troco/2
        troco=troco%2
        print '%d nota(s) de 2 reais' %notas
    if (troco/1) != 0:
        notas=troco/1
        troco=troco%1
        print '%d nota(s) de 1 real' %notas

valor_conta=input('Diga quanto deu a conta: ')
valor_pago=input('Diga quanto foi pago: ')
troco_minimo_notas(troco(valor_conta, valor_pago))