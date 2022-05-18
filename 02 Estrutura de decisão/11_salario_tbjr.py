

salario = float(input('Qual o sálario: '))

amto_20_perc = 1.2
amto_20_perc2 = 0.2
amto_15_perc = 1.15
amto_15_perc2 = 0.15
amto_10_perc = 1.1
amto_10_perc2 = 0.1
amto_5_perc = 1.05
amto_5_perc2 = 0.05

if salario <= 280.00:
    print(f'O Salário informado foi R${salario}')
    print('Aumento de 20%')
    print(f'O aumento será de R${salario * amto_20_perc2}')
    print(f'O novo salário será de R${salario * amto_20_perc}')
elif salario >= 280.00 and salario <= 700.00:
    print(f'O Salário informado foi R${salario}')
    print('Aumento de 15%')
    print(f'O aumento será de R${salario * amto_15_perc2}')
    print(f'O novo salário será de R${salario * amto_15_perc}')
elif salario >= 700.00 and salario <= 1500.00:
    print(f'O Salário informado foi R${salario}')
    print('Aumento de 10%')
    print(f'O aumento será de R${salario * amto_10_perc2}')
    print(f'O novo salário será de R${salario * amto_10_perc}')
else:
    print(f'O Salário informado foi R${salario}')
    print('Aumento de 5%')
    print(f'O aumento será de R${salario * amto_5_perc2}')
    print(f'O novo salário será de R${salario * amto_5_perc}')

