nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and media < 10: 
    print(f'\nAPROVADO \nMédia: {media}')

elif media < 7: 
    print(f'\nREPROVADO \nMédia: {media}')

else: 
    print(f'\nAPROVADO COM DISTINÇÃO \nMédia: {media}')