print('Digite três números para verificar ordenar os mesmos')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 < n2:
    menor = n1
else:
    menor = n2
if n3 < menor:
    menor = n3

if n1 > n2:
    maior = n1
else:
    maior = n2

if n3 > maior:
    maior = n3

print('O menor valor digitado foi: {}\nO maior valor digitado foi: {}'.format(menor, maior))
