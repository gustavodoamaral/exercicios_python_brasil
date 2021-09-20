data = input(str('Informe uma data no formato DD/MM/YYYY: '))

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

bissexto = False

if ano % 4 == 0:
    bissexto = True
    if ano % 100 == 0 and ano % 400 != 0:
        bissexto = False

valida = True

if mes < 12 and ano > 0:
    if mes in (1, 3, 5, 7, 8, 10, 12):
        if dia < 1 or dia > 31:
            valida = False

    elif mes in (4, 6, 9, 11):
        if dia < 1 or dia > 30:
            valida = False

    else:
        if bissexto:
            if dia < 1 or dia > 29:
                valida = False

        else:
            if dia < 1 or dia > 28:
                valida = False

else:
    valida = False

print(f'{dia}/{mes}/{ano}')

if valida:
    print('DATA VÁLIDA')

else:
    print('DATA INVALIDA')
