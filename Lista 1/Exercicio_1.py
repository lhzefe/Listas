# coding=utf-8
# Exercicio_1 - Luiz Henrique Zeferino Junior

dias = input ('Quantidade de dias: ')
if dias>=0:
	horas=dias*24

horas = horas+input ('Quantidade de horas: ')
if horas>=0:
	minutos=horas*60

minutos = minutos+input ('Quantidade de minutos: ')
if minutos>=0:
	segundos=minutos*60

segundos = segundos + input ('Quantidade de segundos: ')

print '%d segundos' %segundos