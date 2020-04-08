num = []
menor = 0
maior = 0
#z = 0
#posmenor = []
#posmaior = []
print('Digite 5 números inteiros:\n')
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
print('\n\nO menor número é {} e aparece na posição '.format(menor), end = '')
for y in range (0,5):
	if num[y] == menor:
		print('{}... '.format(y+1), end = '')
print('\nO maior número é {} e parece na posição '.format(maior), end = '')
for y in range (0,5):
	if num[y] == maior:
		print('{}... '.format(y+1), end = '')
print('\n')
