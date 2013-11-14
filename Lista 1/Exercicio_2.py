# coding=utf-8
# Exercicio_2 - Luiz Henrique Zeferino Junior

km = input ('Quantidade de Km usados: ')
preco_km = km * 0.15

diaria = input ('Quantidade de Dias de aluguel: ')
preco_aluguel = diaria * 60

print 'Preço à pagar = R$ %.2f' %(preco_aluguel+preco_km) 