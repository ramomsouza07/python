"""
ranges -> Função auxiliar que podemos utilizar na função for

Ranges são utilizados para gerar sequências númericas definidas por um valor_inicial e um valor_final(que não é incluido no range)

#Formas Gerais

Forma 1
    range(valor_de_parada) -> valor de parada não incluso
    Obs.: valor_inicial padrão é 0 e passo de 1 em 1

Exemplo
    for n in range(4):
        print(n)

Forma 2
    range(valor_inicial, valor_de_parada)
    Obs.: passo de 1 em 1

Exemplo
    for n in range(1, 4):
        print(n)

Forma 3
    range(valor_inicial, valor_de_parada, passo)
    passo -> incrementar um valor

Exemplo
    for i in range(0, 51, 5):
        print(i)

Forma 4 (Inverso)
    range(valor_inicial, valor_de_parada, passo)
    passo -> dencrementa um valor 

Exemplo
    for i in range(10, 0, -1):
        print(i)

#Lista com os valores do range
lista = list(range(10)) -> list converte para uma lista
"""
