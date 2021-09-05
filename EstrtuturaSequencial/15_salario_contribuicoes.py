ganho_por_hora = float(input('Quanto você ganha por hora?: '))
horas_trab_mes = int(input('Quantas horas você trabalhou neste mês?: '))

salario_bruto = horas_trab_mes * ganho_por_hora

contribuicao_irpf = salario_bruto * (11/100)
contribuicao_inss = salario_bruto * (8/100)
contribuicao_sindicato = salario_bruto * (5/100)

salario_liquido = salario_bruto - (contribuicao_inss + contribuicao_irpf + contribuicao_sindicato)

print(f'+ Salário Bruto: R$ {salario_bruto} '
      f'\n- IR (11%): R$ {contribuicao_irpf} '
      f'\n- INSS (8%): R$ {contribuicao_inss} '
      f'\n- Sindicato (5%): R$: {contribuicao_sindicato}'
      f'\n= Salário Líquido: R$ {salario_liquido}')
