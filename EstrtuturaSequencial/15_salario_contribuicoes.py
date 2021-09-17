ganhoHora = float(input('Quanto você ganha por hora?: '))
horasTrabalhadas = int(input('Quantas horas você trabalhou?: '))

salarioBruto = horasTrabalhadas * ganhoHora

contribuicaoIRPF = salarioBruto * (11/100)
contribuicaoINSS = salarioBruto * (8/100)
contribuicaoSindicato = salarioBruto * (5/100)

salarioLiquido = salarioBruto - (contribuicaoINSS + contribuicaoIRPF + contribuicaoSindicato)

print(f'+ Salário Bruto: R$ {salarioBruto} '
      f'\n- IR (11%): R$ {contribuicaoIRPF} '
      f'\n- INSS (8%): R$ {contribuicaoINSS} '
      f'\n- Sindicato (5%): R$: {contribuicaoSindicato}'
      f'\n= Salário Líquido: R$ {salarioLiquido}')
