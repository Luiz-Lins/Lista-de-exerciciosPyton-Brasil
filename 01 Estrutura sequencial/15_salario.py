
valor_hora = float(input('Quanto ganha por hora: '))
hr_trabalhadas = float(input('Quantas horas trabalhadas mês: '))

salario_bruto = valor_hora * hr_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

liquido = salario_bruto - ir - inss - sindicato
tt_descontos = ir + inss + sindicato

print(f'Salario bruto R${salario_bruto}')
print(f'Desconto de IR R${ir}')
print(f'Desconto de INSS R${inss}')
print(f'Desconto sindical de R${sindicato}')
print(f'Liquido a receber R${liquido}')
print(f'Total de descntos R${tt_descontos}')