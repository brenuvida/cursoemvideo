

print('Salarios inferiores a R$ 1250,00 recebem 15% de aumento, os iguais ou superiores recebem 10%.')
sal = float(input('Digite o salário que será calculado: '))

if sal < 1250:
    sal = sal * 1.15
else:
    sal = sal * 1.10

print('O novo salário é de R$ {:.2f} reais'.format(sal))
