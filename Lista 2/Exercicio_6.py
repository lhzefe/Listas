# coding=utf-8
# Exercicio_6 - Luiz Henrique Zeferino Junior

def centenas_dezenas_unidades(valor):
    if (valor/100) != 0:
        quantidade=valor/100
        valor=valor%100
        print '%d centena(s)' %quantidade
    if (valor/10) != 0:
        quantidade=valor/10
        valor=valor%10
        print '%d dezena(s)' %quantidade
    if (valor/1) != 0:
        quantidade=valor/1
        valor=valor%1
        print '%d unidade(s)' %quantidade

valor=input('Diga um valor inteiro entre 1 e 1000: ')
centenas_dezenas_unidades(valor)