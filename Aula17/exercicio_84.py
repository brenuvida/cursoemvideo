# -*- coding: utf-8 -*-
nomepeso = list()
dados = list()
nao = ('nao', 'NAO', 'Nao', 'não', 'NÃO', 'Não', 'n', 'N')
maior = menor = 0
nomemaior = list()
nomemenor = list()
while True:
	dados.append(str(input('Digite o nome: ')))
	dados.append(float(input('Digite o peso: ')))
	nomepeso.append(dados[:])
	dados.clear()
	test = str(input('Deseja continuar? S/N: '))
	if test in nao:
		break
print('A lista informada é: {}'.format(nomepeso))
for x in range(0,len(nomepeso)):
	if x == 0:
		maior = menor = nomepeso[0][1]
	elif nomepeso[x][1] > maior:
		maior = nomepeso[x][1]
	elif nomepeso[x][1] < menor:
		menor = nomepeso[x][1]
for x in range(0, len(nomepeso)):
	if menor == nomepeso[x][1]:
		nomemenor.append(nomepeso[x][0])
	if maior == nomepeso[x][1]:
		nomemaior.append(nomepeso[x][0])
print('O menor peso foi de {} kilos, peso de {}\nO maior peso foi de {} kilos, peso de {}'. format(menor,nomemenor,maior,nomemaior))
