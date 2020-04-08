from random import randint
print(' === Vamos jogar par ou ímpar? === \n\n')
venceu = 0
jog = 0
while True:
    num = int(input('\n\nDigite um número para jogar: '))
    jog += 1
    escolha = str(input('\n\nDigite P ou I para Par ou Ímpar: ')).upper().strip()[0]
    compu = randint(0, 10)
    if escolha == 'P':
        if (num + compu) % 2 == 0:
            print('\n\nO computador escolheu {}. Você venceu'.format(compu))
            venceu += 1
            break
        else:
            print('\n\nO computador escolheu {}. Você perdeu, jogue novamente'.format(compu))
    if escolha == 'I':
        if (num + compu) % 2 != 0:
            print('\n\nO computador escolheu {}. Você venceu'.format(compu))
            venceu +=1
            break
        else:
            print('\n\nO computador escolheu {}. Você perdeu, jogue novamente'.format(compu))
print('\n\nVocê jogou {} veze(s) e ganhou {} partida(s)'.format(jog, venceu))

            
            
