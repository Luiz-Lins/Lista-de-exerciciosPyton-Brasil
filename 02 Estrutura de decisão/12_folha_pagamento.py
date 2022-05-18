
hora = float(input('Qual o valor da hora: '))
horas_mes = float(input('qnts horas trabalhadas: '))

salario_bruto = hora * horas_mes

if salario_bruto <= 900:
    desc_ir = 0
elif salario_bruto <= 1500:
    desc_ir = 5
elif salario_bruto <= 2500:
    desc_ir = 10
else:
    desc_ir = 20

print(f'Salario Bruto: ({hora} * {horas_mes})  : R${salario_bruto}')
print(f'(-) IR ({desc_ir})                    : R${(salario_bruto/100) * desc_ir}')
print(f'(-) INSS (10%)                : R${salario_bruto * 0.1}')
print(f'(-) FGTS (11%)                : R${salario_bruto * 0.11}')
print(f'Total de descontos            : R${(salario_bruto/100*desc_ir) + (salario_bruto * 0.1)}')
tt_desc = (salario_bruto/100*desc_ir) + (salario_bruto * 0.1)
print(f'Salário líquido               : R${(salario_bruto - tt_desc)}')
      
