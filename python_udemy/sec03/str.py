"""
Tipo String (str) - É todo dado que será categorizado como texto

Obs.: Sempre que estiver entre aspas simples, aspas duplas, aspas simples triplas, aspas duplas triplas.
aspas simples => 'Ramom', '1', 'a', '$#%'
aspas duplas => "Ramom", "1", "a", "$#%"
aspas simples triplas => '''Ramom''', '''1''', '''a''', '''$#%'''   """ 
# aspas duplas triplas => """Ramom""", """1""", """a""", """$#%""" 
"""
A string em python é criada dessa forma:
nome = palavras separadas
nome = ['p', 'a', 'l', 'a', 'v', 'r', 'a', 's', ' ', 's', 'e', 'p', 'a', 'r', 'a', 'd', 'a', 's']
         0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17

Contatenação de strings em Python
nome = ramom
print(nome + 'Souza')

Podemos fazer operações com strings
print(nome * 4) -> 'ramomramomramomramom'

https://apps.timwhitlock.info/emoji/tables/unicode
código unicode -> U+1F61C
emoji = '\U0001F61C' -> é necessário possuir a \ e o U000 antes do código

"""

nome = "Gina's Bar"
print(f"{nome}", type(nome))

nome = "Quebrando \nLinha"
print(nome, type(nome))

nome = "Ramom \" Souza"
print(f"{nome}", type(nome))

nome = "maiúsculo"
print(nome.upper() , type(nome)) #string toda em maiúscilo

nome = "minúsculo"
print(nome.lower() , type(nome))#string toda em minúsculo

nome = "palavras separadas"
print(nome.split() , type(nome))#transforma em uma lista de string, separa as palavras

print(nome[0:8]) #Slice de string -> não imprime o 8º caractere 
print(nome[9:18]) #Slice de string -> não imprime o 18º caractere

print(nome[::-1]) #Inverte a string por completo

print(nome.replace('a', 'e')) #Troca uma determinada letra por outra

nome = "Ramom Souza Vieira Barreto"
print(nome.split()[0]) #Acessa o index 0 da lista de string, que possui 4 indexes

nome = "socorram me subino onibus em marrocos" #Palíndromo -> é igual de trás para frente, assim como ana, arara.
print(nome)
print(nome[::-1]) #Inverte a string por completo
