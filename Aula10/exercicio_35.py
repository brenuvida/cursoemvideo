print('\nVamos verificar se três retas podem formar um triangulo\n')

a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))


print('\nO triangulo não é possível\n' if a > (b + c) or b > (a + c) or c > (a + b) else '\nO triângulo é possível\n')




"""
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
media = 0   
if a != maior and a != menor:
    media = a
if b != maior and b != menor:
    media = b
if c != maior and c != menor:
    media = c

if a == b and b == c:
    print ('O triangulo é possível e tem 3 lados iguais')
if (media + menor) > maior:
    print('O triangulo é possível')
else:
    print ('O triangulo NÃO é possível')

"""
