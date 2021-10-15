sexo = input('Informe o sexo [M/F]: ')

if sexo == 'M':
    print('M - Masculino ')
elif sexo == 'F':
    print('F - Feminino')
elif sexo != 'M' and sexo != 'F':
    print('Sexo inválido')