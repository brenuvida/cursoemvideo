from time import sleep
num1 = int(input('Digiteum número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))



print ('Comparando os números... ')
if num1 == num2:
    print ('Os dois númerostem o mesmo valor ')
elif num1 > num2:
    print('O primeiro número digitado é maior')
elif num2 > num1:
    print('O segundo número digitado é maior')
else:
    print('Não foi possível realizar o cálculo com as informações fornecidas')
