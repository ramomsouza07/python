#Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

if num1 == num2:
    print("Os números são iguais")
elif num1 > num2:
    print(f"O número {num1:.2f} é maior que {num2:.2f}")
else:
    print(f"O número {num2:.2f} é maior que {num1:.2f}")