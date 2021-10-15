print('Descubra se o ano é bissexto ')
ano = int(input('Informe o ano: '))

if ano % 4 == 0 and ano % 100 != 0:
    bissexto = True
    print(f'o ano {ano} é bissexto')

else:
    bissexto = False

if bissexto is False:

    if ano % 400 == 0:
        print(f'o ano {ano} é bissexto')

    else:
        print(f'o ano {ano} não é bissexto')
