from datetime import date
from time import sleep
ano = int(input('Digite um ano para verificar se é bissexto, digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

print ('\nAnalisando o ano {} ...\n'.format(ano))
sleep (2)

c1 = ano % 4
c2 = ano % 100
c3 = ano % 400

if (c1 == 0) and (c2 != 0):
    print('Este ano é bissexto')
else:
    if c3 == 0:
        print('Este ano é bissexto')
    else:
        print('Este ano NÃO é bissexto')
print('\n---FIM---')
