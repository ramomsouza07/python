name = str(input('Escreva seu nome completo: ')).strip() 
print(f'Esse é o nome em maiúculo {name.upper()} \n Esse é o nome em minúsculo {name.lower()} \n A quantidade de letras desse nome é {len(name) - name.count(' ')} \n O primeiro nome tem {name.find(' ')} caracteres')
