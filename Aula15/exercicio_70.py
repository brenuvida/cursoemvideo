total = 0
totalmil = 0
baratonome = ''
barato = 0
while True:
    nome = str(input('\nDigite o nome do produto: '))
    valor = float(input('Digite o valor do produto em R$: '))
    if barato == 0:
        barato = valor
    elif valor < barato:
        baratonome = nome
    total += valor
    if valor > 1000:
        totalmil += 1
    while True:
        decisao = str(input('\nVocê deseja continuar? [S/N]: ')).upper().strip()[0]
        if decisao in ('N', 'S'):
            break
    if decisao == 'N':
        break
print('\n\nO total gasto na compra é {}, {} produto(s) custa(m) mais que mil reais e o nome do produto mais barato é {}.'.format(total, totalmil, baratonome))
print('\n\n ===  FIM  ===')

    
