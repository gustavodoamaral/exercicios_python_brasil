letra = input('Informe uma letra: ')

if 'AEIOU'.find(letra.upper()) >= 0:
    print(f'Vogal')
else:
    print(f'Consoante')