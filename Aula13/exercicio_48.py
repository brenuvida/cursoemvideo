print('Imprimir a soma de todos os números impares que são multiplos de 3 entre 1 e 500')

n = 0

for c in range(1,501,2):
    if c % 3 == 0:
        print(c)
        n = n + c
print (' A soma de todos os números ímpares divisíveis por 3 é: {}'.format(n))


