'''2. Classe Quadrado: Crie uma classe que modele um quadrado:

a.Atributos: Tamanho do lado
b.Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado:
    def __init__(self, lado = 1):
        self.lado = lado
        
    def calcular_area(self):
        return self.lado ** 2

quadrado = Quadrado(4)
print(quadrado.lado, quadrado.calcular_area())