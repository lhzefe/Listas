# coding=utf-8
# Exercicio_4 - Luiz Henrique Zeferino Junior

num = int(input('Digite um numero inteiro: '))
x=1

def funcao_de_retorno(num):
    for x in range(num+1):
        y=0
        for y in range(x):
            print x , '' ,
        print '\n'
'''
    x=1
    while x<=num:
        y=0
        while y<x:
            print '%i ' %x,
            y+=1
        x+=1
        print '\n' 
'''

funcao_de_retorno(num)