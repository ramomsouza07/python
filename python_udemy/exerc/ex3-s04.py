#Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar

num = float(input("Insira um valor: "))
if num % 2 == 0:
    print(f"O número {num:.2f} é par")
else:
    print(f"O número {num:.2f} é ímpar")