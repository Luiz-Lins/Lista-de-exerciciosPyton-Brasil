
nota1 = float(input('1° nota: '))
nota2 = float(input('2° nota: '))

media = (nota1 + nota2)/ 2
print(media)

if media < 7:
    print('reprovado!')
elif media <= 9.9:
    print('aprovado!')
elif media == 10.0:
    print('Aprovado com distinção')