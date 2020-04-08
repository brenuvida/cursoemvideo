print('Digite 6 números, vamos somar apenas os números pares')
n = 0
for c in range (1,7):
    x = int(input('\nDigite um númento: '))
    if x % 2 == 0:
        n = n + x
if n == 0:
    print('\n\nNenhum número par foi digitado!!')
else:
    print('\n\nA soma de todos os números pares digitados é {}'.format(n))


            
