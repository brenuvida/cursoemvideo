numero = int(input('Digite um número com quatro dígitos: '))
milhar = numero // 1000
numero = numero % 1000
centena = numero // 100
numero = numero % 100
dezena = numero // 10
unidade = numero % 10

print ('Unidade: {}'.format(unidade))
print ('Dezena: {}'.format(dezena))
print ('Centena: {}'.format(centena))
print ('Milhar: {}'.format(milhar))

