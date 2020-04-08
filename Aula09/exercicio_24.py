nome = input('Digite o nome de uma cidade: ')
nome = nome.strip()
print ('O nome da cidade digitado é: {}'.format(nome))
nome = nome.lower()
print ('Verificando se existe a palavra santo no nome da cidade... \n')
print ('A palavra santo existe no mome da cidade?: {}'.format('santo' in nome))

