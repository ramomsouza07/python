print("Seja Bem-Vindo ao Marcado, Usuário")
item_car_fra = 0
item_car_boi = 0
item_fei = 0
item_arr = 0
i = 0
valido = False

while not valido:
    
    print('1 - ARROZ - 19,90')
    print('2 - FEIJÃO - 10,90')
    print('3 - CARNE DE BOI - 34,90')
    print('4 - CARNE DE FRANGO - 25,45')
    
    i = int(input("Insira o número do item que deseja comprar: "))
    
    if i in range(1,5):
        j = int(input("Insira a quantidade desse item: "))
        if i == 1:
            item_arr = j
        if i == 2:
            item_fei = j
        if i == 3:
            item_car_boi = j
        if i == 4:
            item_car_fra = j
            
        valido = int(input("Deseja sair (1 - Sim / 0 - Não): "))
    else: 
        while i not in range(1, 5):
            i = int(input("Insira um valor válido de 1 a 4: "))
 
item_arr *= 19.90   
item_fei *= 10.90        
item_car_boi *= 34.90        
item_car_fra *= 25.45      

print('Sua Nota Fiscal')
if item_arr > 0:
    print(f'O valor do arroz foi: R${item_arr:.2f}')
if item_fei > 0:
    print(f'O valor do feijão foi: R${item_fei:.2f}')
if item_car_boi > 0:
    print(f'O valor do carne de boi foi: R${item_car_boi:.2f}')
if item_car_fra > 0:
    print(f'O valor do carne de frango foi: R${item_car_fra:.2f}')