palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futudo','velejar','dingue','ancora','vento','represa','alheta','fiel')


for pal in palavras:
    print('\nNa palavra {} temos as vogáis: '.format(pal),end='')
#    print(pal)
    for i in pal:
#        print(i)
        if i == 'a':
            print('a',end='')
        if i == 'e':
            print('e',end='')
        if i == 'i':
            print('i',end='')
        if i == 'o':
            print('o',end='')
        if i == 'u':
            print('u',end='')
print('\n\n===  FIM  ===')
