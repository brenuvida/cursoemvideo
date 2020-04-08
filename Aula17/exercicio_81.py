# -*- coding: utf-8 -*-
lista = list()
nao = ['n','N','nao','Nao','não','Não','NAO','NÃO']
while True:
	valor = int(input('Digite um valor: '))
	lista.append(valor)
	sn = str(input('Deseja continuar? [S/N]: '))
	if sn in nao:
		break
print('A lista digitada é {}: '.format(lista))
print('A lista ordenada é {}: '.format(sorted(lista)))
print('A lista invertida é {}'.format(sorted(lista, reverse = True)))
