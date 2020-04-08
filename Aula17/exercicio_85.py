# -*- coding: utf-8 -*-
lista = list()
par = list()
impar = list()
for x in range(0,7):
	num = int(input('Digite o {}o valor: '.format(x+1)))
	if num % 2 == 0:
		par.append(num)
	if num % 2 == 1:
		impar.append(num)
lista.append(par)
lista.append(impar)
print('Os valores pares digitados foram: {}'.format(sorted(lista[0])))
print('Os valores ímpares digitados foram {}'.format(sorted(lista[1])))
