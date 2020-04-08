# -*- coding: utf-8 -*-
#dados = list()
linha = list()
matriz = list()
a = 0
for y in range(0, 3):
	for x in range(0, 3):
		linha.append (int(input('Digite um número: ')))
	matriz.append(linha[:])
	linha.clear()
#print(matriz)
print('\nA matriz digitada foi: \n\n')
for y in range(0,3):
	for x in range(0,3):
		print('[ {} ]'.format(matriz[y][x]), end = '')
	print('')
print('')
print('')
print('')
