# coding=utf-8
# Exercicio_3 - Luiz Henrique Zeferino Junior

import random
def embaralhar_palavra(palavra):
    palavra=list(palavra)
    random.shuffle(palavra)
    palavra=''.join(palavra)
    palavra=palavra.upper()
    print palavra
'''
def embaralhar_palavra(palavra):
    palavra=''.join(random.sample(palavra, len(palavra))).upper()
    print palavra
'''
palavra=raw_input('Diga uma palavra para embaralhar: ')
embaralhar_palavra(palavra)