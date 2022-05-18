print('Responda as seguintes perguntas com Sim ou Não:')

perg1=input('Telefonou para a vitima? ')
perg2=input('Esteve no local do crime? ')
perg3=input('Mora perto da vítima? ')
perg4=input('Devia para vítima? ')
perg5=input('já trabalhou com a vítima? ')

if perg1 == 'sim':
    r1 = 1
else:
    r1 = 0
    
if perg2 == 'sim':
    r2 = 1
else:
    r2 = 0
if perg3 == 'sim':
    r3 = 1
else:
    r3 = 0
if perg4== 'sim':
    r4 = 1
else:
    r4 = 0
if perg5 == 'sim':
    r5 = 1
else:
    r5 = 0

resultado = r1 + r2 + r3 + r4 + r5

if resultado <= 1:
    print('Inocente')
elif resultado == 2:
    print('suspeito')
elif resultado <= 4:
    print('cumplice')
else:
    print('assassino')
