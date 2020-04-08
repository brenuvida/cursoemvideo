

### FIBONACCI ###

a = 1
b = 1
c = 0
cont = int(input('Quantos termos de uma sequência de Fibonacci você quer ver?: '))
print (a)
print (b)
while (cont - 2) > 0:
    cont = cont - 1
    c = a + b
    a = b
    b = c
    print (c)
