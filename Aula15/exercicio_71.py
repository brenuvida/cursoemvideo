
#valor = 0
while True:
    valor = int(input('Digite o valor que deseja sacar: '))
    if valor < 0:
        break
    else:
        notas100 = valor // 100
        valor = valor % 100
        notas50 = valor // 50
        valor = valor % 50
        notas20 = valor // 20
        valor = valor % 20
        notas10 = valor // 10
        valor = valor % 10
        notas5 = valor // 5
        valor = valor % 5
        notas1 = valor // 1
        if notas100 > 0:
            print('Você vai receber {} nota(s) de 100'.format(notas100))
        if notas50 > 0:
            print('Você vai receber {} nota(s) de 50'.format(notas50))
        if notas20 > 0:
            print('Você vai receber {} nota(s) de 20'.format(notas20))
        if notas10 > 0:
            print('Você vai receber {} nota(s) de 10'.format(notas10))
        if notas5 > 0:
            print('Você vai receber {} nota(s) de 5'.format(notas5))
        if notas1 > 0:
            print('Você vai receber {} nota(s) de 1.'.format(notas1))
print('\n === FIM ===')
