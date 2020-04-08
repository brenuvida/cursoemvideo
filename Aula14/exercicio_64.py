num = int(0)
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número qualquer para ser somado e 999 para sair: '))
    cont += 1
    if num != 999:
        soma = soma + num
print ('O número de valores calculados é de {} números e a soma de todos eles é {}'.format(cont-1, soma))
