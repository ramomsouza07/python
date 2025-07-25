"""
Loop While

Forma Geral

while expressão_booleano: (condição de existência)
    //execução do loop

while True: -> é um loop infinito, pois a condição de existência é inalterável
    print('1')

Obs.: cuidado com o while, por causa da incrementação, 
pois é necessário que em algum momento o loop tenha que parar
    
Exemplo 1

i = 0
while i < 5:
    print(i)
    i += 1

Exemplo 2

resposta = ''
while resposta != 'sim':
    resposta = input('Deseja sair (sim ou não)? ')

"""
