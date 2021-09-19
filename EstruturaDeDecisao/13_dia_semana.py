try:
    numero_dia = int(input('Informe um número para saber o dia da semana: '))

    if numero_dia == 1:
        print('Domingo')

    elif numero_dia == 2:
        print('Segunda-Feira')

    elif numero_dia == 3:
        print('Terça-Feira')

    elif numero_dia == 4:
        print('Quarta-Feira')

    elif numero_dia == 5:
        print('Quinta-Feira')

    elif numero_dia == 6:
        print('Sexta-Feira')

    elif numero_dia == 7:
        print('Sábado')

    else:
        print('Número inválido! Dia da semana não existe.')

except ValueError:
    print('Inválido! Dia da semana não existe.')
