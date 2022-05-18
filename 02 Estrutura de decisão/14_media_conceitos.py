
nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))

media = (nota1 + nota2) / 2
print(media)

if media > 9:
    print('A')
    print(f'A nota 1 foi {nota1} a nota 2 foi {nota2}, a média das notas é {media}, correspondendo ao conceito "A" você foi APROVADO')
elif media > 7.5:
    print('B')
    print(f'A nota 1 foi {nota1} a nota 2 foi {nota2}, a média das notas é {media}, correspondendo ao conceito "B" você foi APROVADO')
elif media > 6:
    print('C')
    print(f'A nota 1 foi {nota1} a nota 2 foi {nota2}, a média das notas é {media}, correspondendo ao conceito "C" você foi APROVADO')
elif media > 4:
    print('D')
    print(f'A nota 1 foi {nota1} a nota 2 foi {nota2}, a média das notas é {media}, correspondendo ao conceito "D" você foi REPROVADO')
else:
    print('E')
    print(f'A nota 1 foi {nota1} a nota 2 foi {nota2}, a média das notas é {media}, correspondendo ao conceito "E" você foi REPROVADO')

