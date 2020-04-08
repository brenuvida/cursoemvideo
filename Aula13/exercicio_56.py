print('\n\nDigite o Nome, Idade e Sexo de 4 pessoas.\n\n')

idadem = 0
velho = 0
nomevelho = ''
nummulheres = 0
for c in range (0, 4):
    print('')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite M ou F: '))
    if sexo == 'M':
        if idade > velho:
            velho = idade
            nomevelho = nome
    elif sexo == 'F':
        if idade < 20:
            nummulheres = nummulheres + 1
    idadem = idadem + idade
print('\n\nA média da idade do grupo é: {}'.format(idadem/4))
print('\n\nO homem mais velho do grupo é o {}.'.format(nomevelho))
print('\n\nO número de mulheres que tem menos de 20 anos é: {}'.format(nummulheres))


