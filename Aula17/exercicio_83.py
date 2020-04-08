# Falta reescrever como exercicio 83
# -*- coding: utf-8 -*-
a = 0
expressao = str(input('Digite uma expressão: '))
for x in range(0, len(expressao)):
	if expressao[x] == '(':
		a += 1
		if a < 0:
			break
	elif expressao[x] == ')':
		a -= 1
		if a < 0:
			break
if a == 0:
	print('Sua expressão está correta!')
else:
	print('Sua expressão está incorreta')
