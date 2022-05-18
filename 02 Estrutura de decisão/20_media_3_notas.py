
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))

media = (nota1 + nota2 +nota3)/3

if media >= 10:
    print(f'Aprovado com distinção, media{media}')
elif media <= 6.99:
    print(f'Reprovado, média de {media}.')
else:
    print(f'Aprovado, média {media}')