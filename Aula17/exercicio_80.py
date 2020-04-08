# -*- coding: utf-8 -*-
lista = []
for y in range (0,5):
	num = int(input('Digite um número: '))
	if y == 0:
		lista.append(num)
	elif num > lista[(len(lista)-1)]:
		lista.append(num)
	else:
		for x in range (0,len(lista)):
			if num <= lista[x]:
				lista.insert(x,num)
				break
print('A lista digitada de forma ordenada é {}'.format(lista))
