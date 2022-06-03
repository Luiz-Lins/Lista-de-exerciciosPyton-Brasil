'''
03 Faça um programa que leia e valide as seguintes informações:
    a.Nome: maior que 3 caracteres;
    b.Idade: entre 0 e 150;
    c.Salário: maior que zero;
    d.Sexo: 'f' ou 'm';
    e.Estado Civil: 's', 'c', 'v', 'd';
'''
# Validar Nome
while True:
    nome = input('Digite seu nome: ')
    
    if (len(nome) <=3 ): 
        print('Nome inválido')
    else:
        print('nome válido')
        break

print()

#Validar Idade
while True:
    idade = int(input('Qual sua idade: '))
    
    if idade >= 0 and idade <= 150:
        print('Idade válida')
        break
    else:
        print('idade inválida')
print()

#validar salário 
while True:
    salario = int(input('Qual seu sálario: '))
    
    if salario >= 0:
        print('Salario válido')
        break
    else:
        print('salario inválido')
print()

#validar sexo

while True:
    sexo = str.lower(input('Sexo M ou F para sexo:'))
    if sexo == "m" or sexo == 'f':
        print('informação de sexo válida.')
        break
    else:
        print('informação inválida')
print()
    
#estado civil

while True:
    ec = str.lower(input('Digite s, c, v, d para estado civil:'))
    if ec == "s" or ec == 'c' or ec == 'v' or ec == 'd':
        print('informação de estado civil válida.')
        break
    else:
        print('informação inválida')