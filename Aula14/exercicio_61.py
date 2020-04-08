cont = 10
base = int(input('Digite o número base de uma PA: '))
razao = int(input('Digite a razão da PA: '))
print('A base da PA é {} e abaixo seguem os próximos 10 termos da PA: \n\n'.format(base))
while cont > 0:
    base += 10
#    print(cont)
    print(base)
    cont = cont - 1
print('===  FIM  ===')
