import random
print('Digite os nomes dos alunos que devem apresentar seus trabalhos:')
n1 = input('Digite um nome: ')
n2 = input('Digite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')

list = [n1, n2, n3, n4]
print ('')
random.shuffle(list)
print ('A ordem dos alunos para apresentar o trabalho é: {}'.format(list))
