'''1.0 Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.'''

s1 = input('Digite uma string: ')
s2 = input('Digite uma string: ')

print(f'String 1: {s1}')
print(f'String 1: {s2}')

tamanho1 = len(s1)
tamanho2 = len(s2)

print(f'Tamanho de "{s1}": {tamanho1} caracteres')
print(f'Tamanho de "{s2}": {tamanho2} caracteres')

if tamanho1 == tamanho2:
    print('As duas strings são do mesmo tamanho.')
else:
    print('As duas strings são de tamanhos diferentes.')

if s1 == s2:
    print('As duas strings possuem o mesmo conteúdo')
else:
    print('As duas strings possuem conteúdo diferente.')




