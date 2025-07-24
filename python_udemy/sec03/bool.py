"""
Tipo Booleano - Álegebra Booleana

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro -> 1
False -> Falso -> 0

Obs.: type reconhece bool somente quando uma variável recebe True ou False
Obs.: Inicial sempre maiúscula

Operações
    - (Negação) not -> not A:
        Se A = 1, not A = 0
        Se A = 0, not A = 1

    - (E) and -> A * B:
        Operação Binária, depende de dois valores para ser calculado
            A = 1 // B = 1 -> A and B = 1
            A = 1 // B = 0 -> A and B = 0
            A = 0 // B = 1 -> A and B = 0
            A = 0 // B = 0 -> A and B = 0

    - (Ou) or -> A + B:
        Operação Binária, depende de dois valores para ser calculado
            A = 1 // B = 1 -> A or B = 1
            A = 1 // B = 0 -> A or B = 1
            A = 0 // B = 1 -> A or B = 1
            A = 0 // B = 0 -> A or B = 0

    - (Ou exclusivo) xor -> (not (A) * B) + (not (B) * A)
        Operação Binária, depende de dois valores para ser calculado
            A = 1 // B = 1 -> A xor B = 0
            A = 1 // B = 0 -> A xor B = 1
            A = 0 // B = 1 -> A xor B = 1
            A = 0 // B = 0 -> A xor B = 0

    - Implication -> (not A) + B
        Operação Binária, depende de dois valores para ser calculado
            A = 1 // B = 1 -> (not A) or B = 1
            A = 1 // B = 0 -> (not A) or B = 0
            A = 0 // B = 1 -> (not A) or B = 1
            A = 0 // B = 0 -> (not A) or B = 1

Operadores Lógicos
    - > - menor
    - < - maior
    - >= - menor ou igual
    - <= - maior ou igual
    - == - igual
    -
"""
ativo = False
print("Normal -> ", ativo)
print("Not -> ", not ativo)