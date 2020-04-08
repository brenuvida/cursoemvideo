from datetime import date

nasc = int(input('Digite o ano do nascimento: '))

hoje = date.today().year

idade = hoje - nasc

print('\n\nA idade do atleta é {}'.format(idade))

if idade <= 9:
    print('Atleta MIRIM')
elif 10 < idade <= 14:
    print('Atleta INFANTIL')
elif 15 < idade <= 19:
    print('Atleta JUNIOR')
elif 20 < idade <= 25:
    print('Atleta SÊNIOR')
elif idade > 25:
    print('Atleta MASTER')
else:
    print('Não foi possível calcular a idade com as informações fornecidas')

