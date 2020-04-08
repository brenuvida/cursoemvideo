# -*- coding: utf-8 -*-
jogos = int(input('\nLoterias das caixa!!\n\nQuantos jogos você quer sortear? '))
seis = list()
from random import randint
from time import sleep
print('\n')
for x in range(1, jogos+1):
	for y in range(0, 6):
		r = randint(1, 61)
		seis.append(r)
	sleep(1)
	print('Jogo {}: {}'.format(x, seis))
	seis.clear()
print('\nNúmeros sorteados com sucesso, não esqueça de apostar na lotérica mais próxima!!!\n\n')
