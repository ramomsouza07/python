import math
import random

#from math import sqrt, floor
num = int(input('Indique um valor: '))
raiz = math.sqrt(num)

num2 = random.randint(1, 20)
fat = math.factorial(num2)

print(f'A raiz quadrada desse número é igual a {raiz:.2f}!\n O fatorial do valor {num2} é igual a {fat}')
