from time import sleep
num = int(input('Digite um número inteiro: '))
num = num % 2

print('Analisando o número digitado')
sleep(3)

print('O número digitado é PAR'if num == 0 else 'O número digitado é IMPAR')


