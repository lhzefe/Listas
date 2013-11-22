# coding=utf-8
# Exercicio_4 - Luiz Henrique Zeferino Junior

from math import sqrt
def equacao_segundo_grau(a,b,c):
    print 'Digite os valores de A, B e C, onde Ax²+Bx+C=0: '
    a = input()
    if a==0:
        print 'Não é equação de segundo grau'
    else:
        b,c = input(), input()
        delta= (b)**2 -(4*a*c)
        if delta < 0:
            print 'Não possui raizes reais'
        elif delta==0:
            x1= -b/2*a
            print 'A raiz da equação é: ',x1,
        elif delta>0:
            x1= (-b + sqrt(delta))/2*a
            x2= (-b - sqrt(delta))/2*a
            print 'As raizes da equação são: ',x1, 'e' ,x2,

equacao_segundo_grau(a=0,b=0,c=0)