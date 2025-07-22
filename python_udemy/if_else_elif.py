"""
Estruturas Condicionais - If, Else, Elif
If -> Se

Else -> Senão

Elif -> Senão se
"""

idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Menor de Idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("Maior de Idade")