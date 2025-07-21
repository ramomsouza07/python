num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num} \n Unidade:{u} \n Dezena:{d} \n Centena:{c} \n Milhar:{m} \n')

