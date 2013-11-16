# coding=utf-8
# Exercicio_5 - Luiz Henrique Zeferino Junior

def converter(horas, minutos):

    if (horas>12 and horas<25):
        horas-=12
    else:
        horas=horas

    if (horas>0 and horas<25 and minutos>=0 and minutos<=59):
        print horas,':',minutos, '\n',
    else:
        pass

horas=1
minutos=0
while (horas>0 and horas<25 and minutos>=0 and minutos<=59):
    horas=input('Diga as horas no modelo 24h -- HH --: ')
    if (horas>0 and horas<25):
        minutos=input('Diga os minutos -- MM --: ')
    converter(horas, minutos)