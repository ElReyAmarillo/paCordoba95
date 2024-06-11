import math


for i in range(2):
    print('ciclo # ' + str(i))

print('Finalizó el ciclo')

def areaCirculo(radio):
    area = math.pi * radio*radio
    print("El area es " + str(area))