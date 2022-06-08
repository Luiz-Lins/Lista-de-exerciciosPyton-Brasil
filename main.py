'''
16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.'''

salarios = [200, 250, 320, 389, 480, 623, 697, 656, 789, 820,992,920,2000,3000,1000, 509, 538]
contagem_fx_salarial = [0] * 9
for salario in salarios:
    indice = salario  // 100 -2
    indice_max = len(contagem_fx_salarial) -1
    indice = min(indice, indice_max)
    contagem_fx_salarial[indice] += 1
print(contagem_fx_salarial)