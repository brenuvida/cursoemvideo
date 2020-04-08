
while True:
    num = int(input('\n\nDigite um número para ver sua tabuada: '))
    if num < 0:
        break
    print(30*'=')
    for c in range (1, 11):
        print('{} x {} = {}'.format(num,c, c * num))
    print(30 * '=')
print('\n\n=== FIM ===')

           
