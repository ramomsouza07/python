"""
Break - utilizado para sair de um loop ou em condicionais

Ele quebra o código, "pula"
Quando o loop começa a executar o bloco de código, assim que identifica o break, ele ignora tudo
e sai do loop.

Exemplo

i = 0
while i < 5:
    i += 1
    print(i)
    if i == 3:
        break
"""


i = 0
while i < 5:
    i += 1
    print(i)
    if i == 3:
        break