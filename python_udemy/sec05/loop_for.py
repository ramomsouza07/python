"""
Laço de Repetição - For

Loop é uma estrutura de repetição 

for item in interavel:
    execução

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.    
Iteravel - todo objeto que possui indices que podem ser percorridos.

Exemplos de Iterváreis
    - Strings -> nome = 'Texto de exemplo'
    - Lista -> lista = [1, 2, 3, 4]
    - Range -> numeros = range(1, 10)
"""

#Exemplos de For
""""""
nome = "Ramom"
lista = [1, 3, 5, 7, 9]
numeros = range(1,5)

#Exemplo 1 (Iterando em uma string)
for letra in nome:
    print(letra)

#Exemplo 2 (Iterando em uma lista)
for num in lista:
    print(num)

#Exemplo 3 (Iterando em um range)
#range(valor_inicial, valor_final)
#Obs.: O valor final não é incluído, se valor_final é 10, o range alcança até o 9

for num in range(1, 10):
    print(num)

teste = "Lorem Ipsum"

for i, v in enumerate(teste): #enumerate -> ele cria tuplas com um index e o valor definido do objeto
    print(f"No índice {i} : {v}")

for tupla in teste:
    print(tupla)