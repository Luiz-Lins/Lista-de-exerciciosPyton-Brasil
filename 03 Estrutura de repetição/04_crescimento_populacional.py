#1. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.


populacao_A = 80_000
populacao_B = 200_000

taxa_A = 1.03
taxa_B = 1.015
anos=0

while populacao_A < populacao_B:
    populacao_A = int(populacao_A * taxa_A)
    populacao_B = int(populacao_B * taxa_B)
    anos +=1
print(f'população de ano {anos}')
print(f'população de A: {populacao_A}')
print(f'população de B: {populacao_B}')

    