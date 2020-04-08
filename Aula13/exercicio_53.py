frase = str(input('\n\n\n\nDigite uma frase para verificar se é um palindromo: '))

frase = frase.strip()
frase = frase.split()


t = len(frase)


nfrase = ''
for c in range (0, t):
    nfrase = nfrase + frase[c]
nfrase = nfrase.lower()
print('\n\n\nA frase sem espaços e minúscula ficaria escrita desta forma: {}'.format(nfrase))
nlen = len(nfrase)
print('\n\n\nA frase possui {} caracteres'.format(nlen))
xfrase = ''



for c in range (nlen -1, -1, -1):
    xfrase = xfrase + nfrase[c]

print('\n\n\nA frase digitade de trás para frente ficaria: {}'.format(xfrase))

if nfrase == xfrase:
    print('\n\n\nEssa merda tá igual, é palindromo\n\n\n\n\n')
else:
    print('\n\n\nTá diferente, NÃO é palindromo\n\n\n\n\n')

print('======= FIM =======')

x = input('Pressione qualquer tecla para sair\n\n')


