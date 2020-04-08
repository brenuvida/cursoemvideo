from random import randint
a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)

num = (a, b, c, d, e)
print(num)
print ('O menor número da tupla é {} e o maior é {}.'.format(sorted(num)[0], sorted(num)[4]))
