import math
angulo = float(input('Digite o angulo que deseja calcular: '))
angrad = math.radians(angulo)
sen = math.sin(angrad)
cos = math.cos(angrad)
tan = math.tan(angrad)

print('Para o angulo {}: \nSeu seno é {:.2f}\nSeu coseno é {:.2f}\nSua gangente é {:.2f}'.format(angulo, sen, cos, tan))
