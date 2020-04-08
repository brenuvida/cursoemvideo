

print('\n\n\nDigite uma sequência de números que serão somados para calcular a sua média, menor e maior número.\n')
print('Digite 0 (zero) para terminar')
soma = 0
cont = 0
maior = 0
menor = 999
num = int (-1)
while num != 0:
    if cont == -1:
        cont = 0
    num = int(input('Digite um número: '))
    soma = soma + num
    if num != 0:
        cont = cont + 1
        if num > maior:
            maior = num
        if num < menor:
            menor = num
#    print('Contador = {}.'.format(cont))
if menor != maior:
    print ('\nForam digitados {} números, o menor número é {}, o maior é {} e a média dos números digitados é {}'.format(cont, menor, maior, soma / cont))
else:
    print ('\nForam digitados {} números, todos os números são iguais e média dos números digitados é {}'.format(cont, soma / cont))
fim = input('\nPressione ENTER para perminar\n\n')
