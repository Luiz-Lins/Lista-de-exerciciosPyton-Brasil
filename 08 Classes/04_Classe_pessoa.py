'''4. Classe Pessoa: Crie uma classe que modele uma pessoa:

a. Atributos: nome, idade, peso e altura
b. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
            self.idade += 1

henrique = Pessoa('henrique', 2, 12, 80)

for _ in range(22):
    henrique.envelhecer()
    print(f'idade de {henrique.nome} é: {henrique.idade} anos. E sua altura é {henrique.altura}')
