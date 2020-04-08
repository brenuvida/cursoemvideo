p = int(input('Digite um número para saber se é um número primo: '))

n = 0
for c in range(2, p):
    print(c)
    if p % c == 0:
        n = n + 1
if n == 0:
    print('É um número primo')
else:
    print('Não é um número primo')
print('=== FIM ===')
