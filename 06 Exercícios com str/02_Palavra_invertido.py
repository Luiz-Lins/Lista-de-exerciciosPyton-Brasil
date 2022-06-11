#2. Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = input('digite seu nome: ').upper()
letras_invertido = ''.join(reversed(nome))
palavra_invertido = ' '.join(reversed(nome.split()))

print(nome)
print(letras_invertido)
print(palavra_invertido)