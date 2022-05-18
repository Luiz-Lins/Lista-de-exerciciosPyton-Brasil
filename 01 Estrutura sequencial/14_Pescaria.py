

peso_pesca = float(input('Quantos kg foram pescados no total: '))

multa = ((peso_pesca - 50) * 4 )

if peso_pesca >= 50:
    print(f'Devido o valor total da pesca ter ultrapassado 50kg vc será multado em R${multa}')
else:
    print('Ok, Seu valor total pescado está dentro da lei. Continue assim!')