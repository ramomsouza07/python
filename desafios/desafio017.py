import math
cO = int(input('Indique o valor do cateto oposto: '))
cA = int(input('Indique o valor do cateto adjacente: '))

hip = math.hypot(cA , cO)

print(f'Sendo o valor do cateto oposto de {cO} e do cateto adjacente de {cA}, a hipotenusa corresponde a {hip}!')