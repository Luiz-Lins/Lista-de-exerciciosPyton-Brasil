
turno = input('Qual turno você estuda? Digite M para Matutino, V para vespertino, N para Noturno: ').lower()

if turno == 'm':
    print('Bom dia!')
elif turno == 'v':
    print('Boa tarde')
elif turno == 'n':
    print('Boa noite')
else:
    print('valor inválido')
    