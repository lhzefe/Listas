# coding=utf-8
# Exercicio_3 - Luiz Henrique Zeferino Junior

cigarros_fumados = input('Quantidade de cigarros fumados por dia: ')
tempo_de_vida_perdido = cigarros_fumados * (10/60.0)
anos = input('Tempo que fuma em anos: ')
total_de_dias_de_vida_perdidos = ((tempo_de_vida_perdido/24) *  (anos * 365))

print 'O tempo de vida perdido em dias foi: %.0f' %total_de_dias_de_vida_perdidos