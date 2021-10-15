salarioBruto = float(input('Informe o salário bruto: '))

if salarioBruto <= 900:
    porcentagem = 0
    contribuicaoIRPF = 0

elif salarioBruto <= 1500:
    porcentagem = 5
    contribuicaoIRPF = salarioBruto * 0.05

elif salarioBruto <= 2500:
    porcentagem = 10
    contribuicaoIRPF = salarioBruto * 0.1

else:
    porcentagem = 20
    contribuicaoIRPF = salarioBruto * 0.2

contribuicaoINSS = salarioBruto * 0.1
contribuiçãoFGTS = salarioBruto * 0.11

salarioLiquido = (salarioBruto - contribuicaoIRPF) - contribuicaoINSS

print(f'Salário Bruto: R$ {salarioBruto}\n'
      f'(-) IR - {porcentagem}%: R$ {contribuicaoIRPF}\n'
      f'(-) INSS - 10%: {contribuicaoINSS}\n'
      f'FGTS - 10%: R$ {contribuiçãoFGTS}\n'
      f'Total de descontos: R$ {contribuicaoINSS+contribuicaoIRPF}\n'
      f'Salário Líquido: {salarioLiquido}')
