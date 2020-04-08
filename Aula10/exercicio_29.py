
num = int(input('Qual a velocidade do carro em Km/h? '))

if num > 80:
    print('O carro foi multado em {} reais'.format((num - 80) * 7))
else:
    print('Dentro da velocidade permitida')
