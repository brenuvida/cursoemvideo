print(39*'-')
print('LISTAGEM DE PREÇOS')
print(39*'-')
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print('{:.<30}R$'.format(listagem[i]),end = '')
    else:
        print('{:>7}'.format(listagem[i]))
print(39*'-')
