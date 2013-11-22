# coding=utf-8
# Exercicio_8 - Luiz Henrique Zeferino Junior

def conta_espaco_vogal(frase):
    vogais_espaco=[0,0,0,0,0,0]
    for x in range(len(frase)):
        if frase[x]=='a':
            vogais_espaco[0]+=1
        elif frase[x]=='e':
            vogais_espaco[1]+=1
        elif frase[x]=='i':
            vogais_espaco[2]+=1
        elif frase[x]=='o':
            vogais_espaco[3]+=1
        elif frase[x]=='u':
            vogais_espaco[4]+=1
        elif frase[x]==' ':
            vogais_espaco[5]+=1
    print 'A vogal "a" aparece: ',vogais_espaco[0], 'vez(es)' 
    print 'A vogal "e" aparece: ',vogais_espaco[1], 'vez(es)' 
    print 'A vogal "i" aparece: ',vogais_espaco[2], 'vez(es)' 
    print 'A vogal "o" aparece: ',vogais_espaco[3], 'vez(es)' 
    print 'A vogal "u" aparece: ',vogais_espaco[4], 'vez(es)' 
    print 'A quantidade de espaços é: ',vogais_espaco[5], 

frase=raw_input('Digite uma frase: ')
conta_espaco_vogal(frase)