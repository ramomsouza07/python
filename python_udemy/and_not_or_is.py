"""
Estruturas Lógicas - AND (E), OR (OU), NOT (NÃO), IS (É)

Operadores unários 
    - NOT

Operadores Binários 
    - AND, OR, IS

#Operador is -> é a mesma coisa que ==, ele compara 2 valores e verifica se são iguais    
"""

ativo = True
logado = True

# print(not ativo)

if ativo and logado:
    print("Bem-Vindo Usuário")
else:
    print("Você precisa ativar a conta!")


if ativo is False:
    print("Você precisa ativar a conta!")
else:
    print("Bem-Vindo Usuário")



"""
#Sistema basico e porco de cadastro e login de usuario

print("Seja Bem-Vindo Usúario")
entrada = int(input("Deseja se cadastrar (0) ou logar(1): "))

nomes_cadastrados = ["adm", "admin", "Ramom"]
senhas_cadastradas = ["123", "456", "789"]

if entrada == 0:
    nome = input("Insira seu nome da conta: ")
    senha = input("Insira a senha da conta: ")
    nomes_cadastrados.append(nome)
    senhas_cadastradas.append(senha)    
    print("Você foi cadastrado")
else:
    valido = True
    while valido:
        nome = input("Insira seu nome da conta para login: ")
        if nome not in nomes_cadastrados:
            print("Não existe usuário com esse nome")
        else:
            senha = input("Insira a senha da conta: ")
            if senha not in senhas_cadastradas:
                print("Senha incorreta")
            print("Logado com Sucesso")
            valido = int(input("Deseja sair, 1 -> sim / 0 -> Não"))
"""