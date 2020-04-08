from random import randint

num = int(input('\n\n\nDigite um número entre 0 e 5 para jogar com o computador: '))

if num > 5:
    print('Você só pode jogar com números entre 0 e 5')
else:
    print('\n\n\nO computador está sorteando um número...\n')
    sorteio = randint(0,5)
    print ('O número sorteado é: {}\n'.format(sorteio))
    if num == sorteio:
        print('Você ganhou do computador')
    else:
        print('Você perdeu')
print('Fim de jogo')
