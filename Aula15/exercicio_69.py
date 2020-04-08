
homem = 0
pessoas = 0
mulheres = 0
homens = 0
#decisao = 'S'
while True:
    while True:
        gender = str(input('\n\nDigite H para homem ou M para mulher: ')).strip().upper()[0]
        if gender in ('H','M'):
            break
    idade = int(input('\nDigite a idade:'))
    if idade < 20 and gender == 'M':
        mulheres += 1
    if idade > 18:
        pessoas += 1
    if gender == 'H':
        homens += 1
    while True:
        decisao = str(input('\n\nVocê deseja continuar? [S/N]: ')).upper().strip()[0]
        if decisao in ('S', 'N'):
            break
    if decisao == 'N':
        break
print('\n\n{} pessoas tem mais de 18 anos, {} homens foram cadastrados, {} mulheres tem menos de 20 anos.'.format(pessoas, homens, mulheres))
print('\n\n=== FIM ===')

        
