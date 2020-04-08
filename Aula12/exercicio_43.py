peso = float(input('Digite o seu peso: '))

altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura * altura)

print ('O IMC calculado é de: {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 >= imc <= 25:
    print ('Peso ideal')
elif 25 > imc <= 30:
    print('Sobrepeso')
elif 30 < imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')
else:
    print('Não foi possível calcular o IMC com os dados fornecidos')
