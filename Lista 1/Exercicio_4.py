# coding=utf-8
# Exercicio_4 - Luiz Henrique Zeferino Junior

def funcao_de_retorno(num):
    for x in range(1, num+1):
        y=0
        for y in range(x):
            print x,
        print

    '''x=1
                 while x<=num:
                     y=0
                     while y<x:
                         print '%i' %x,
                         y+=1
                     x+=1
                     print''' 
                     
num = int(input('Digite um numero inteiro: '))
funcao_de_retorno(num)