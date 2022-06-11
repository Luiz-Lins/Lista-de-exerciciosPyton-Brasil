'''11. Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!'''

palavra = 'Devpro'.upper()

print('Jogo da forca: ')
print('Descubra a palavra: ')

print('A palavra é: ', end='')
for letra in palavra:
    print(f'_ ',end='')

conj_palavra = set(palavra)
conj_letra_digitada = set()
erros = 0


while (not conj_palavra.issubset(conj_letra_digitada)) and erros < 7:
    print()
    print()
    letra_digitada = input('Digite uma letra: ').upper()
    conj_letra_digitada.add(letra_digitada)
    if letra_digitada in conj_palavra:
        print('A palavra é: ', end='')
        for letra in palavra:
            if letra in conj_letra_digitada:
                print(f'{letra} ',end='')
            else:
                print(f'_ ',end='')
    else:    
        erros += 1
        print(f'Erro {erros} de 6. Tente novamente')
    
    
    
    print()
    print('letras já digitadas:', conj_letra_digitada)

if erros < 7:
    print('Parabéns você ganhou!!')
else:
    print('você perdeu!')
        



