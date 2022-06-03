# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


while True:
    try:
        nota = int(input('Digite uma nota entre 0 e 10: '))
    except ValueError:
        print('Valor digitado é inválido.')
    else:
        if 0 <= nota <= 10:
            print(f'Nota informada é {nota}')
            break
        else:
            print('a nota deve ser entre 0 e 10.')
        



