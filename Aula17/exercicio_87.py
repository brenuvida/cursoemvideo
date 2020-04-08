# -*- coding: utf-8 -*-
#dados = list()
linha = list()
matriz = list()
maior = 0
somapar = 0
for y in range(0, 3):
	for x in range(0, 3):
		num = int(input('Digite um número: '))
		linha.append(num)
		if num % 2 == 0:
			somapar = somapar + num
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
print('A soma dos valores pares é {}'.format(somapar))
print('A soma dos valores da terceira coluna é {}'.format(matriz[0][2]+matriz[1][2]+matriz[2][2]))
for x in range(0, 3):
	if matriz[1][x] > maior:
		maior = matriz[1][x]
print('O maior valor da segunda linha é {}'.format(maior))
