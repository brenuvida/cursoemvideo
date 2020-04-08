preco = float(input('Digite o preço de um produto: R$ '))
condicao = int(input('Qual é a condição de pagamento escolhida? Opções: \n\n[1] A vista no dinheiro ou cheque - 10% de desconto.\n[2] A vista no cartão - 5% de desconto.\n[3] Em até 2x no cartão - Sem desconto.\n[4] 3x ou mais no cartão - 20% de acrescimo.\n\n\nDigite a sua opção: '))

print('\n\nA condição escolhida foi: {}'.format(condicao))

if condicao == 1:
    print('O valor a ser pago é: {:.2f}'.format(preco * (90/100)))
elif condicao == 2:
    print('O valor a ser pago é: {:.2f}'.format(preco * (95/100)))
elif condicao == 3:
    print('O valor a ser pago é: {:.2f}'.format(preco))
elif condicao == 4:
    print('O valor a ser pago é: {:.2f}'.format(preco * 1.20))
else:
    print('A opção deve ser 1, 2, 3 ou 4')
