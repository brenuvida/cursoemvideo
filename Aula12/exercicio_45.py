
from random import randint

print ('\n\n\nVamos jogar JOKENPÔ!!!\n\n\n')

escolha = int(input('Escolha PEDRA, PAPEL ou TESOURA:\n\n[1] PEDRA\n\n[2] PAPEL\n\n[3] TESOURA\n\nFaça a sua escolha: '))

if escolha != 1 and escolha != 2 and escolha != 3:
    print('\n\nVocê escolheu: {}\nApenas números entre 1 e 3 são aceitos, tente novamente'.format(escolha))
else:
    lista = ['','PEDRA','PAPEL','TESOURA']
    print('Você escolheu: {}\n\n'.format(lista[escolha]))

    computador = randint(1,3)
    print('O computador escolheu: {}\n\n'.format(lista[computador]))
    if escolha == 1 and computador == 1:
        print('Emppate')
    elif escolha == 1 and computador == 2:
        print('O computador ganhou')
    elif escolha == 1 and computador == 3:
        print('Você ganhou')
    elif escolha == 2 and computador == 2:
        print('Emppate')
    elif escolha == 2 and computador == 1:
        print('Você ganhou')
    elif escolha == 2 and computador == 3:
        print('O computador ganhou')
    elif escolha == 3 and computador == 3:
        print('Emppate')
    elif escolha == 3 and computador == 1:
        print('O computador ganhou')
    elif escolha == 3 and computador == 2:
        print('Você ganhou')
print ('\n\n === FIM ===\n\n\n\n')

        
        
        
