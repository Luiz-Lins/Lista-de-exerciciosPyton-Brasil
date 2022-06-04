# 5.Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:
    try:
        populacao_A = int(input('Digite a população do país A: '))
    except ValueError:
        print('Valor inválido!') 
    try:
        taxa_A = float(input('Digite a taxa de crescimento do país A:'))
    except ValueError:
        print('Valor inválido!') 
    try:
        populacao_B = int(input('Digite a população do país B: '))
    except ValueError:
        print('Valor inválido!')  
    try:
        taxa_B = float(input('Digite a taxa de crescimento do país B:'))
    except ValueError:
        print('Valor inválido!')

    anos=0
    

    populacao_A = int(populacao_A * taxa_A)
    populacao_B = int(populacao_B * taxa_B)
    anos +=1
    print(f'população de ano {anos}')
    print(f'população de A: {populacao_A}')
    print(f'população de B: {populacao_B}')
    