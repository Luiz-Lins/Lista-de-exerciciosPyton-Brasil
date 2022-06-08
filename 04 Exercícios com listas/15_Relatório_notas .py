'''
# 15.Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
    a. Mostre a quantidade de valores que foram lidos;
    b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    d. Calcule e mostre a soma dos valores;
    e. Calcule e mostre a média dos valores;
    f. Calcule e mostre a quantidade de valores acima da média calculada;
    g. Calcule e mostre a quantidade de valores abaixo de sete;
    h. Encerre o programa com uma mensagem;
'''

notas = []
while True:
    entrada = input('Digite uma nota: ')
    if entrada == '-1':
        break
    notas.append (float(entrada))

#  a. Mostre a quantidade de valores que foram lidos;
qnt = len(notas)
print(f' foram lidos {qnt} notas')

# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print(' '.join([str(nota) for nota in notas]))

# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
notas.reverse()
for nota in notas:
    print(nota)

# d. Calcule e mostre a soma dos valores;
soma = sum(notas)
print(f' A soma dos valores é {soma}')

# e. Calcule e mostre a média dos valores;
media = soma / qnt
print(f' A média dos valores é {media}')

# f. Calcule e mostre a quantidade de valores acima da média calculada;
print(' '.join([str(nota) for nota in notas if nota > media]))

# g. Calcule e mostre a quantidade de valores abaixo de sete;
print(' '.join([str(nota) for nota in notas if nota < 7]))

# h. Encerre o programa com uma mensagem;
print('Programa encerrado com sucesso.')
