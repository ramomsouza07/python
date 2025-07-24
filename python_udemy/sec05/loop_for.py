"""
Laço de Repetição - For

Loop é uma estrutura de repetição 

for item in interavel:
    execução

for _ in range(3): -> o '_' ignora o valor
    executa 3 vezes

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.    
Iteravel - todo objeto que possui indices que podem ser percorridos.

Exemplos de Iterváreis
    - Strings -> nome = 'Texto de exemplo'
    - Lista -> lista = [1, 2, 3, 4]
    - Range -> numeros = range(1, 10)
"""


#Exemplos de For
#Exemplo 1 (Iterando em uma string)
"""
nome = "Ramom"
for letra in nome:
    print(letra)
"""


#Exemplo 2 (Iterando em uma lista)
"""
lista = [1, 3, 5, 7, 9]
for num in lista:
    print(num)
"""
    
#Exemplo 3 (Iterando em um range)
#range(valor_inicial, valor_final)
#Obs.: O valor final não é incluído, se valor_final é 10, o range alcança até o 9
"""
numeros = range(1,5)
for num in range(1, 10):
    print(num)
"""

"""
# Exemplo 4
teste = "Lorem Ipsum"
for i, v in enumerate(teste): #enumerate -> ele cria tuplas com um index e o valor definido do objeto
    print(f"No índice {i} : {v}")
"""

"""
# Exemplo 5
for letra in teste:
    print(letra, end = '') #o parâmetro end, por padrão, vem atribuído com \n
"""

"""
# Exemplo 6
for tupla in teste:
    print(tupla) #se adicionar um index na variavel (tupla[0]) irá mostrar somente o primeiro valor de cada tupla
    #Tupla -> ((0, L), (1, o), (2, r), (3, e), (4, m), (5, ), (6, I), (7, p), (8, s), (9, u), (10, m))
    #print(tupla) -> 0\n 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n
"""

# Exemplo 7
"""
quan = int(input("Quantas vezes você quer que repita: "))
resul = 0
for i in range(1, quan + 1): #se deixar apenas a variável, ele vai até o valor_da_variável - 1
    if i % 2 == 0:
        resul *=i
    else:
        resul += i
print(resul)
"""

# Exemplo 8
emoji = '\U0001F61C'
for num in range(1, 11):
    print(emoji * num)
