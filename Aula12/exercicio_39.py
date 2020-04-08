from datetime import date

hoje = date.today().year
nascido = int(input('Digite a data de nascimento com 4 dígitos: '))
print ('A data digitada é: {}'.format(nascido))

dif = hoje - nascido
if dif == 18:
    print('É hora de se alistar')
elif dif < 18:
    print ('Ainda faltam {} anos para se alistar'.format(18-dif))
elif dif > 18:
    print ('O tempo de alistamento já passou há {} anos.'.format(dif - 18))
else:
    print('Não foi possível calcular a data com os dados informados')
    
