"""
Listas são como vetores e matrizes (arrays), com a diferença de serem dinâmicos
podemos utilizar com qualquer tipo de dados

    - Dinâmico: não possui tamanho fixo, podemos ir adicionando, porém, varia de acordo com a quantidade
    de memória que temos disponível no sistema
    - Qualquer tipo de dado: podemos ter uma lista com valores em str, int, float, bool, entre outros

    As listas são representadas utilizando "[]"

type([]) -> list

#Podemos checar se um determinado valor está em uma lista

num = 1
if num in l4:
    print(f"Possui {num}")
else:
    print(f"Não encontrei {num}")

# print(type(l2[0])) -> tipo str

#Ordenar listas
print(l1)
l1.sort()
print(l1)

#Contagem de ocorrências de um determinado valor
print(l1.count(1))

#Adicionar elementos em listas
nome_da_lista.append(valor_que_será_adicionado) -> com append, é possível adicionar somente 1
elemento por vez

"""

l1 = [1, 2, 5, 7, 9, 11, 99, 1930, 454, 1]
l2 = ['R', 'a', 'm', 'o', 'm',]
l3 = []
l4 = list(range(11))
l5 = list("Ramom Souza")

l1.append([3, 5, 7]) #-> adicionando uma lista a outra

if [3, 5, 7] in l1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")

l1.extend([123, 44, 67]) # irá adicionar os valores individualmente / aceita apenas iteráveis

"""
Testes
for i in l1:
    if i in l4:
        print(f"O valor {i} está na lista 4")
    else: 
        print(f"O valor {i} não está na lista 4")


#Para valores em strings, a ordenação é em ordem alfabética

num = int(input("Insira a quantidade de valores no array: "))
array = []
i = 0
while i < num:
    var = int(input("Insira o valor: "))
    array.append(var)
    i += 1
print(array)
array.sort()
print(array)
"""