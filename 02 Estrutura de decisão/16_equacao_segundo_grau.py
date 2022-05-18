import math

valorA = float(input('1° valor de A: '))
valorB = float(input('2° valor de B: '))
valorC = float(input('3° valor de C: '))

delta = math.pow(valorB , 2) - (4 * valorA * valorC)

if valorA == 0:
    print('O valor informado para "A" é igual a "0", portanto a equação não é de segundo grau.')
elif delta < 0:
    print('A equação não possui raizes reais.')
elif delta == 0:
    print('A equação possui apenas uma raiz.')
else:
    print('A equação possui 2 raizes reais.')