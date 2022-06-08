# 7.Faça um programa que leia 5 números e informe o maior número.

maior_numero = int(input('Digite um número: '))

for _ in range(5):
    maior_numero = max(maior_numero,int(input('Digite o um número: ')))
    print(f'Maior número encontrado {maior_numero}')