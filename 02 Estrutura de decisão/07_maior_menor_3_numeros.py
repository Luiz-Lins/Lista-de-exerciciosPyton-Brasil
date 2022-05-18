

num1 = input('Digite o 1° número: ')
num2 = input('Digite o 2° número: ')
num3 = input('Digite o 3° número: ')

resposta1 = num1 > num2, num1 > num3
resposta2 = num2 > num1, num2 > num3
resposta3 = num3 > num1, num3 > num2

if num1 > num2 and  num1 > num3:
    print(f'O 1° número digitado ({num1}) é o maior.')
elif num2 > num1 and  num2 > num3:
    print(f'O 2° número digitado ({num2}) é o maior.')
elif num3 > num1 and  num3 > num2:
    print(f'O 3° número digitado ({num3}) é o maior.')

if num1 < num2 and  num1 < num3:
    print(f'O 1° número digitado ({num1}) é o menor.')
elif num2 < num1 and  num2 < num3:
    print(f'O 2° número digitado ({num2}) é o menor.')
elif num3 < num1 and  num3 < num2:
    print(f'O 3° número digitado ({num3}) é o menor.')