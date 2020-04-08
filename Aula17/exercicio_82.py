# Falta reescrever como exercicio 82
# -*- coding: utf-8 -*-
lista = list()
listapar = list()
listaimpar = list()
nao = ['n','N','nao','Nao','não','Não','NAO','NÃO']
while True:
	valor = int(input('Digite um valor: '))
	lista.append(valor)
	if valor % 2 == 0:
		listapar.append(valor)
	else:
		listaimpar.append(valor)
	sn = str(input('Deseja continuar? [S/N]: '))
	if sn in nao:
		break
print(40*'+=')
print('\nA lista digitada é {}: '.format(lista))
print('\nA lista par e ordenada é  {}: '.format(sorted(listapar)))
print('\nA lista ímpar e ordenada é {}'.format(sorted(listaimpar,)))
