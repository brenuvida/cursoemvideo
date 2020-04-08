from time import sleep
dist = float(input('Digite a distância da viagem em KM: '))
print ('Calculando a sua viagem .')
sleep(1)
print ('Calculando a sua viagem ..')
sleep(1)
print ('Calculando a sua viagem ...')
sleep(1)
print('Viagens de até 200 Km custam R$ 0,50 por Km rodado.\nViagens acima de 200 Km custam R$ 0,45 por Km rodado.\n')
print (' O valor da corrida é de R$ {:.2f} reais. '.format(dist * 0.50) if dist <= 200 else ' O valor da corrida é de R$ {:.2f} reais. '.format(dist * 0.45))

