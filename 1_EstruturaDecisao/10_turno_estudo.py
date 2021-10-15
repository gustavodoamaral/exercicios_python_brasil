turno = str(input('Em que turno você estuda? \n'
                  '[M] Matutino\n'
                  '[V] Vespetino\n'
                  '[N] Noturno\n'
                  'Informe o turno: ')).upper()
if turno == 'M':
    print('Bom dia! ;)')

elif turno == 'V':
    print('Boa tarde! ;)')

elif turno == 'N':
    print('Boa noite! ;)')

else:
    print('Turno inválido')