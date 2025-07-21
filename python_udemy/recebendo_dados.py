from datetime import date
ano = date.today().year

#Entrada de Dados

#print("Qual seu nome?")
#nome = input() #Input -> Entrada

nome = input("Qual seu nome: ")

"""
Sintaxe antiga
print("Seja Bem-Vindo(a) %s" %nome)

Sintaxe atual
print("Seja Bem-Vindo(a) {0}".format(nome))

Sintaxe atual
print(f"Seja Bem-Vindo(a) {nome}")
"""

#print("Qual sua idade? ")
#idade = input()

idade = int(input("Qual sua idade? "))

#Saida de Dados

#Sintaxe antiga
#print("%s tem %s anos" %(nome, idade))

"""
int(idade) => cast

conversão de um tipo de dado para outro tipo

input() => sempre recebe o dado como string
"""

print(f"{nome} tem {idade} anos")
print(f"{nome} nasceu entre {ano - 1 - idade} e {ano - idade}")