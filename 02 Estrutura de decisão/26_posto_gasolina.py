abastecer1 = input('Alcool ou Gasolina: ')
abastecer2 = float(input('litros a abastecer: '))

A = 1.90
G = 2.50

desconto1 = 0.97
desconto2 = 0.95
desconto3 = 0.96
desconto4 = 0.94

if abastecer1 == 'A' and abastecer2 <= 20:
    valorfinal = abastecer2 * A * desconto1
    print(
        f'Cliente abasteceu {abastecer2} litros, valor total {A * abastecer2}, obteve 3% de desconto, valor final R${valorfinal}.'
    )

if abastecer1 == 'A' and abastecer2 > 20:
    valorfinal = abastecer2 * A * desconto2
    print(
        f'Cliente abasteceu {abastecer2} litros, valor total {A * abastecer2}, obteve 5% de desconto, valor final R${valorfinal}.'
    )

if abastecer1 == 'G' and abastecer2 <= 20:
    valorfinal = abastecer2 * G * desconto3
    print(
        f'Cliente abasteceu {abastecer2} litros, valor total {G * abastecer2}, obteve 4% de desconto, valor final R${valorfinal}.'
    )

if abastecer1 == 'G' and abastecer2 > 20:
    valorfinal = abastecer2 * G * desconto4
    print(
        f'Cliente abasteceu {abastecer2} litros, valor total {G * abastecer2}, obteve 6% de desconto, valor final R${valorfinal}.'
    )
