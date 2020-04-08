from datetime import date

ano = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    print(ano - nasc)
    if ano - nasc < 18:
        menor = menor + 1
    else:
        maior = maior + 1
print('Entre as datas digitadas {} são menores de idade e {} são maiores de idade.'.format(menor, maior))

