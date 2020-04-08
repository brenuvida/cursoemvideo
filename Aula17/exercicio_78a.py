num = []
menor = 0
maior = 0
#z = 0
posmenor = []
posmaior = []
print('Digite 5 números inteiros:')
for x in range (0,5):
	a = int(input('Digite um número: '))
	num.append(a)
	if x == 0:
		menor = a
		maior = a
	else:
		if a < menor:
			menor = a
		elif a > maior:
			maior = a

print("\n\nA lista de números digitados é {}".format(num))
print('\n\nO menor número digitado é {} e o maior número digitado é {}'.format(menor,maior))
for y in range (0,5):
	if num[y] == menor:
		posmenor.append(y)
	if num[y] == maior:
		posmaior.append(y)
#	z = z + 1
print('\n\nOs menor número é {} e aparece na posição {}, o maior número é {} e aparece nas posição{}'.format(menor, posmenor, maior, posmaior))
