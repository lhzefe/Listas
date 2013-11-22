# coding=utf-8
# Exercicio_7 - Luiz Henrique Zeferino Junior

import random
from os import system

def ler_arquivo(lista):
    x = 0
    lista_de_palavras = [''] * len(lista)
    while x < len(lista):
        palavra = lista[x]
        lista_de_palavras[x] += palavra[:-1]
        x+=1
    return lista_de_palavras

def verificar_letra(letra, palavra_teste):
    if letra in palavra_teste:
        return 1
    else:
        return 0        

def trocar_letra(letra, palavra_teste, lista):
    x = 0
    while x < len(palavra_teste):
        if letra == palavra_teste[x]:
            lista[x] = letra
        x += 1

x=' '
while x!='s':
    system ('clear')
    palavras = open('Exercicio_7.txt', 'r')
    lista = ler_arquivo(palavras.readlines())
    palavra = lista[random.randint(0,len(lista)-1)]    
    palavra_escolhida = ['_'] * len(palavra)

    y = 1
    while y == 1:
        
        print 'Jogo da Forca'
        print 'Você tem 6 chances...'
        print 'A palavra tem: ', len(palavra), 'letras.\n'

        vida = 6
        while vida > 0:
            if verificar_letra('_', palavra_escolhida):
                print 'Você tem %d vida.' %vida
                print palavra_escolhida
                letra = raw_input('Diga uma letra: ').lower()
                if verificar_letra(letra, palavra):
                    trocar_letra(letra, palavra, palavra_escolhida)
                    print 'Certo!!! a palavra tem: %s.' %letra
                else:
                    print 'Errado!!! a palavra não tem : %s.' %letra
                    vida -= 1
                                    
            else:
                print 'Você acertou!!! A palavra é:', palavra
                y = 0
                break

        if vida <= 0:       
            print 'Você já era!!! A palavra certa era: ', palavra
            y = 0
    x=raw_input('Digite "s" para sair, ou enter para continuar a jogar: ')