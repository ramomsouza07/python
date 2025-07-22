"""
Faça um programa que leia um número inteiro fornecido pelo usuário. 
Se esse número for positivo, calcule a raiz quadrada do número e apresente-a. 
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""

num = float(input("Digite um número: "))

if num > 0:
    raiz = num ** 0.5
    print(f"A raiz de {num:.2f} é {raiz:.2f}")
elif num == 0:
    print("O número é 0")
else:
    print("O número é inválido")
