import math

ang = float(input('Indique um ângulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O ângulo {ang}° possui o seno de {sen:.2f}, o cosseno de {cos:.2f} e a tangente de {tan:.2f}!')