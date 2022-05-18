kg_apple = float(input('Qnts kg de maça? '))
kg_morango = float(input('Qnts kg de morango? '))

if kg_morango < 5:
    valor_da_compra_m = kg_morango * 2.50
    print(f' {valor_da_compra_m} de morangos')
else:
    valor_da_compra_m = kg_morango * 2.20
    print(f' {valor_da_compra_m} de morangos')

if kg_apple < 5:
    valor_da_compra_a = kg_apple * 1.80
    print(f' {valor_da_compra_a} de apples')
else:
    valor_da_compra_a = kg_apple *1.50
    print(f' {valor_da_compra_a} de apples')

if kg_apple + kg_morango > 8:
    print((valor_da_compra_a + valor_da_compra_m) * 0.9)
elif valor_da_compra_a + valor_da_compra_m > 25:
    print((valor_da_compra_a + valor_da_compra_m) * 0.9)
else:
    print(valor_da_compra_a + valor_da_compra_m)
