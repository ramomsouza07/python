import random
a1 = input('Indique o nome do(a) aluno(a) 1:')
a2 = input('Indique o nome do(a) aluno(a) 2:')
a3 = input('Indique o nome do(a) aluno(a) 3:')
a4 = input('Indique o nome do(a) aluno(a) 4:')
ordem = [a1, a2, a3, a4]
random.shuffle(ordem)

print(f'Para a ordem de apresentação, será a seguinte: {ordem}')