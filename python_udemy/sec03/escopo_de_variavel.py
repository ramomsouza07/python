"""
Escopo de Variáveis

Dois casos de escopos
1 - Variáveis Globais - são reconhecidas, seu escopo compreende todo o programa
2 - Variáveis Locais - são reconhecidas apenas no bloco em que foram declaradas

Obs.: Python é uma linguagem de tipagem dinâmica, não é indicado o tipo da variável em sua declaração, o tipo é inferido ao atribuirmos o valor da mesma

Para declarar uma variável em Python:

nome_da_variavel = valor_da_variavel
"""

num = 42 #Variável Global
print(num)

if num > 10:
    novo = num + 10 #Variável Local
    print(novo)

print(novo)