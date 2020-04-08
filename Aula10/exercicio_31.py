dist = float(input('Digite a distância da viagem em KM: '))
print('Viagens de até 200 Km custam R$ 0,50 por Km rodado.\nViagens acima de 200 Km custam R$ 0,45 por Km rodado.\n')

if dist <= 200:
    dist = dist * 0.50
else:
    dist = dist * 0.45

print(' O valor da corrida é de R$ {:.2f} reais. '.format(dist))
