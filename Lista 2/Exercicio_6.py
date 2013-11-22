# coding=utf-8
# Exercicio_6 - Luiz Henrique Zeferino Junior

def centenas_dezenas_unidades(valor):
    if (valor/100) != 0:
        quantidade=valor/100
        centena=quantidade
        valor=valor%100
        if centena==1:
            cent='%d centena' %centena
        else:
            cent='%d centenas' %centena
        
    if (valor/10) != 0:
        quantidade=valor/10
        dezena=quantidade
        valor=valor%10
        if dezena==1:
            deze='%d dezena' %dezena
        else:
            deze='%d dezenas' %dezena

    if (valor/1) != 0:
        quantidade=valor/1
        unidade=quantidade
        valor=valor%1
        if unidade==1:
            uni='%d unidade' %unidade
        else:
            uni='%d unidades' %unidade

    print '%s, %s e %s' %(cent, deze, uni)

valor=input('Diga um valor inteiro entre 1 e 1000: ')
centenas_dezenas_unidades(valor)