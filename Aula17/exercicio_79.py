lista = []
while True:
	test = int(input('Digite um valor: '))
	if test in lista:
		print('Valor duplicado	, digite outro valor!')
	else:
		lista.append(test)
		print('Valor adicionado com sucesso')
		c = input('Quer continuar? [S/N]: ')
		if c in ['Nao', 'Não', 'N', 'n', 'não', 'nao']:
			break
print(30*'-=')
print('Você digitou os valores {}'.format(sorted(lista)))


#n = ['Não', 'não', 'Nao', 'nao', 'N', 'n']
#while True:
#	t.append(int(input('Digite um valor:'))
#	test = input('Você deseja continuar? Sim ou Não')
#	if c == n:
#		break
#print('Você digitou os valores: {}'.format(t.sorted()))
