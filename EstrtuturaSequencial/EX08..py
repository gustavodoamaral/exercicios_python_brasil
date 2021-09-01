#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hourly_earnings = float(input('How much do you earn per hour? '))
worked_hours = int(input('Number of hours worked in the month: '))

remuneration = worked_hours * hourly_earnings

print(f'The amount of your compensation this month is: {remuneration}')