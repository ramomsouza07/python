array = []

n = int(input("Digite a quantidade de valores no vetor: "))

for i in range(n):
    valor = int(input(print(f"Insira o valor {i+1}: ")))
    array.append(valor)

def BubbleSort(lista):
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j] , lista[j + 1] = lista[j + 1], lista[j]

BubbleSort(array)
print(f"Lista ordenada: {array}")