
quant = 0
soma = 0

while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    quant += 1
    soma += num


print('A soma dos {} valores é {}.' .format(quant, soma))
