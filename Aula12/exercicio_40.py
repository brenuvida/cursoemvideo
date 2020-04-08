se1 = float(input('Digite a nota do primeiro semestre: '))
se2 = float(input('Digite a nota do segundo semestre: '))

media = (se1 + se2)/2

print('A média calculada é: {}'.format(media))

if media < 7:
    print('Aluno reprovado')
else:
    print('Aluno aprovado')
