# coding=utf-8
# Exercicio_1 - Luiz Henrique Zeferino Junior

def triangular(numero):
    x=1
    while x*(x+1)*(x+2) < numero:
        x+=1 
    if x*(x+1)*(x+2) == numero:
        print '%d é triangular' %numero
    else:
        print '%d não é triangular' %numero

numero=input('Diga um número inteiro positivo: ')
triangular(numero)