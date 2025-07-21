import random
a1 = str(input('Indique o nome do(a) aluno(a): '))
a2 = str(input('Indique o nome do(a) aluno(a): '))
a3 = str(input('Indique o nome do(a) aluno(a): '))
a4 = str(input('Indique o nome do(a) aluno(a): '))

alun = random.choice([a1, a2, a3, a4])

print(f'O aluno escolhido para apagar o quadro é {alun}!')