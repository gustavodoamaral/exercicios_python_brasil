primeiraNota = float(input('Informe a primeira nota: '))
segundaNota = float(input('Informe a segunda nota: '))

media = (primeiraNota + segundaNota) / 2

if media >= 7 and media < 10:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
else:
    print('Aprovado com distinção')