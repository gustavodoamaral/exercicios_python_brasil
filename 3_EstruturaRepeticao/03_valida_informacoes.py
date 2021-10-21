nome = '' 
while len(nome) < 3: 
    nome = str(input('Informe o nome: '))
    if len(nome) < 3: 
        print('Nome inválido')
    else: 
        break

idade = -1
while idade < 0 or idade > 150: 
    idade = int(input('Informe a idade: '))
    if idade < 0 or idade > 150: 
        print('Idade inválida')
    else: 
        break

salario = -1
while salario < 0: 
    salario = float(input('Informe o salário: '))
    if salario < 0: 
        print('Salário inválido')
    else: 
        break

sexo = ''
while sexo != 'M' or sexo != 'F': 
    sexo = str(input('Informe o sexo [M]/[F]: ')).upper()
    if sexo != 'M' or sexo != 'F': 
        print('Sexo inválido')
    else: 
        break

estadoCivil = ''
while not estadoCivil.find('S','C','V','D'):
    estadoCivil = str(input('Informe o estado civil [S],[C],[V] ou [D]: ')).upper()
    if not estadoCivil.find('S','C','V','D'):
        print('Extado Civil inválido')
    else: 
        break

print('Informações validadas')