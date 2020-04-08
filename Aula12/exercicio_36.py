pcasa = float(input('Digite ovalor da casa: '))
print ('O valor da casa é:{:.2f} '.format(pcasa))
anos = int (input('Digite em quantos anos pretende pagar o financiamento: '))
meses = anos * 12
print('{} anos é equivalente a {} em meses'.format(anos, meses))
salario = float(input('Digite o valor do seu salário: '))

porcent = salario * (30/100)

mensalidade = pcasa / meses

print ('O valor de 30% do salário é {:.2f}'.format(porcent))
print ('O valor da mensalidade é {:.2f}'.format(mensalidade))
if mensalidade > porcent:
    print ('Não é possível realizar o financiamento')
else:
    print ('É possível realizar o financiamento')
