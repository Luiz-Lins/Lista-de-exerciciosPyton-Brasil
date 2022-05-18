ano = int(input('digite o ano: '))

bissexto = False
if ano % 4 == 0:
    bissexto = True
    if ano % 100 == 0:
        if ano % 400 != 0:
            bissexto = False
if bissexto:
    print(f'{ano}, ano digitado é Bissexto!')
else:
    print(f'{ano}, ano digitado não é Bissexto!')