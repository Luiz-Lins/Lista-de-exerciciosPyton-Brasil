
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))

if num1 > num2 and num1 > num3:
    print(f'O maior número digitado foi o 1° {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número digitado foi o 2° {num2}')
elif num3 > num1 and num3 > num2:
    print(f'O maior número digitado foi o 3° {num3}')
    