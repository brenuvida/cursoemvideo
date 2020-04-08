numeros = [int(input('Digite o primeiro número: ')), int(input('Digite o próximo número: ')), int(input('Digite o próximo número: ')), int(input('Digite o próximo número: '))]
print('Você digitou os números: {}'.format(numeros))
menor = 0
maior = 0
for a in range (0, len(numeros)):
    if a == 0:
        menor = numeros[a]
        maior = numeros[a]
        posme = [a]
        posma = [a]
    else:
        if menor == numeros[a]:
            posme.append(a)
        if maior == numeros[a]:
            posma.append(a)
        if menor > numeros[a]:
            menor = numeros[a]
            posme = a
        if maior < numeros[a]:
            maior = numeros[a]
            posma = a
print('O menor número digitado é {} e está na posição {} e o maior número digitado é {} e está na posição {}'.format(menor,posme,maior,posma))

    
