nome = input('Digite um nome completo: ')
nome = nome.strip()
print ('O nome digitado é: {}'.format(nome))
nome = nome.lower()
print('Verificando se existe a palavra Silva no nome... \n')
print('A palavra Silva existe neste nome?: {}'.format('silva' in nome))