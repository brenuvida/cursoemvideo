print('Digite o peso de 5 pessoas\n\n\n')

menor = float(1000)
maior = float(0)
for c in range (0, 5):
    peso = float(input('Digite o peso: '))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso
print('O menor peso digitado é {} e o maior peso digitado é {}.'.format(menor, maior))



