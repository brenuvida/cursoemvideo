a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))

num = (a, b, c, d)
print ('Os números digitados foram {} '.format(num))

count9 = num.count(9)
countpar = (0)
if 3 in num:
    pos3 = num.index(3)
    print('O 9 aparece {} vezes, o 3 aparece na posição {} e os números pares são: '.format(count9, pos3), end = '')
    for par in num:
        if par % 2 == 0:
            print(par, end=', ')
else:
    pos3 = 0
    print('O 9 aparece {} vezes, o 3 não foi digitado e os números pares são: '.format(count9), end = '')
    for par in num:
        if par % 2 == 0:
            print(par, end=', ')


        
