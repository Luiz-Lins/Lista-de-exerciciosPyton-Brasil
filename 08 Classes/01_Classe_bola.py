'''1. Classe Bola: Crie uma classe que modele uma bola:

a.Atributos: Cor, circunferência, material
b.Métodos: trocaCor e mostraCor'''

class CirculoPerfeito:
    def __init__(self):
        self.cor = 'Azul'
        self.circuferencia = 4
        self.material = 'Papel'

    def mostra_cor(self):
        return self.cor

circulo_primeiro = CirculoPerfeito()
circulo_segundo = CirculoPerfeito()