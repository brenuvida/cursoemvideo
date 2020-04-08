num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenovo', 'vinte')
escolha = -1
while escolha < 0 or escolha > 20:
    escolha = int(input('Digite um número entre 0 e 20:'))
print('Você escolheu imprimir o número {}.'.format(num[escolha]))

    
