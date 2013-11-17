# coding=utf-8
# Exercicio_8 - Luiz Henrique Zeferino Junior

def triangulo(l1,l2,l3):
    if (l1+l2>l3) or (l1+l3>l2) or (l2+l3>l1):
        if (l1 == l2 == l3):
            print 'Triangulo Equilatero' 
        elif (l1 == l2 != l3) or (l1 == l3 != l2) or (l2 == l3 != l1):
            print 'Triangulo Isosceles'
        elif (l1 != l2 != l3):
            print 'Triangulo Escaleno' 
    else: 
        print 'Não é Triangulo'

print 'Digite 3 valores: '
l1, l2, l3 = input(), input(), input()
triangulo(l1,l2,l3)
