# 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for i in range(151):
    if i % 2 != 0:
        print(i,end=', ')