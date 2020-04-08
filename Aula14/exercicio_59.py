print('Este programa vai realizar uma operação de acordo com a sua escolha.\nPara começar digite dois números.\n')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

print('\nNo menu abaixo escolha uma opção.\n\nSuas opções são:\n\n[1] - Somar\n[2] - Multiplicar\n[3] - Mostrar o maior\n[4] - Digitar novos números\n[5] - Sair do programa\n')
op = int(input('Digite sua opção:'))
if op == 4:
    num1 = float(input('Digite novamente o primeiro número: '))
    num2 = float(input('Digite novamente o segundo número: '))
    op = int(input('Digite novamente sua opção:'))
while op not in (1,2,3,4,5):
    op = int(input('\nApenas números entre 1 a 5 são aceitos\nDigite sua opção:'))
if op == 1:
    print('A soma entre os dois números é: {}'.format(num1 + num2))
elif op == 2:
    print('A multiplicação entre os dois números é {}'.format(num1 * num2))
elif op == 3:
    if num1 == num2:
        print('Os números são iguais')
    elif num1 > num2:
        print('O primeiro número é maior')
    elif num2 > num1:
        print('O segundo número é maior')
elif op == 4:
    print('Você tem dificuldade para decidir')
elif op == 5:
    print('== FIM ==')

print('\n O jogo acabou')


            
