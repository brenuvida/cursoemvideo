from random import randint

comp = randint(1,10)
errou = 1
n = int(input('Digite um número entre 1 e 10 para jogar com o computador: '))

while n not in(1,2,3,4,5,6,7,8,9,10):
    print('\n Apenas números entre 1 e 10 são aceitos')
    n = int(input('Digite um número entre 1 e 10 para jogar com o computador: '))

if comp == n:
        print('Você acertou na primeira tentativa')
else:        
    while comp != n:
        print('\nVocê errou, tente novamente')
        n = int(input('\nDigite um número para tentar mais uma vez:'))
        errou += 1
if errou > 0:
        print('\nVocê precisou digitar {} vezes até acertar'.format(errou))
print('\nO computador havia escolhido o número {}.'.format(comp))



