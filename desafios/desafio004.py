algo = input('Escreva algo:')
print(type(algo))
print(f'É numérico?{algo.isnumeric()}')
print(f'É letra? {algo.isalpha()}')
print(f'É Alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculo? {algo.isupper()}')
print(f'Está em minúsculo? {algo.islower()}')
