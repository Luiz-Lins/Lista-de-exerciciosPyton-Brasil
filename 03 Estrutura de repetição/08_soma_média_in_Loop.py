# 8.Faça um programa que leia 5 números e informe a soma e a média dos números.

numero = float(input('Digite um número: '))

for n in range(2, 6):
    numero += float(input('Digite o um número: '))
    media = numero / n
    print(f'A soma dos números é {numero} e a média é {media}')