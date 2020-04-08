dec = int (input('Digite um número inteiro em base decimal: '))
print ('\n\n\n')
print ('O número digitado em base decimal é {}\nSua conversão para binário é: {}\nSua conversão para octal é: {}\nSua conversão para hexadecimal é: {}\n\n'.format(dec, bin(dec)[2:], oct(dec)[2:], hex(dec)[2:].upper()))
