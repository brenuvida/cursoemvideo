

print ('Calculo de triângulos.... \n\n\n')

lado1 = float(input('Digite o seguimento 1 do triângulo: '))
lado2 = float(input('Digite o seguimento 2 do triângulo: '))
lado3 = float(input('Digite o seguimento 3 do triângulo: '))

if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print('\n\nEstes três seguimentos não formam um triângulo')
else:
    if lado1 == lado2 == lado3:
        print('\nTriângulo equilatero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('\nTriângulo isoceles')
    else:
        print('\nTriângulo escaleno')
print ('\n\n\n== FIM ==')
