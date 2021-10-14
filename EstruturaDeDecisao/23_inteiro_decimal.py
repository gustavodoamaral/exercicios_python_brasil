numero = float(input('Informe um número e descubra se é inteiro ou decimal: '))

if round(numero) == numero: 
    print(f'O número {round(numero)} é inteiro')
else: 
    print(f'O número {numero} é decimal')