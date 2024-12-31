frase = 'Sorvete de Baunilha'
print(f' {'Fatiamento':^30} \n {frase[9]} \n {frase[12:19]} \n {frase[12:20:2]} \n {frase[9::3]} \n {frase[7:]} \n {frase[:12]}\n')

print(f'{'Análise':^30} \n {len(frase)} \n {frase.count('o')} \n {frase.count('o', 0, 7)} \n {frase.find('ilha')} \n {frase.find('Chocolate')} \n {'Sorvete' in frase}')

print(f'{'Transformação':^30} \n {frase.replace('Baunilha', 'Chocolate')} \n {frase.upper()} \n {frase.lower()} \n {frase.capitalize()}\n {frase.title()} \n {frase.strip()} \n {frase.rstrip()} \n {frase.lstrip()}')
#funções com a letra r no começo, fazem a função somente na direita e l para esquerda
#split - divide a string em várias outras
print(f'{'Divisão':^30} \n {frase.split()}')

print(f'{'Junção':^30} \n {'-'.join(frase)} ')