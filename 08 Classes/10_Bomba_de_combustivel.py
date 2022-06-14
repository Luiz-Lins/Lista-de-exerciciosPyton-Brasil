'''10. Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
     i. tipoCombustivel.
    ii. valorLitro
   iii. quantidadeCombustivel
b. Possua no mínimo esses métodos:
    i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
   ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
  iii. alterarValor( ) – altera o valor do litro do combustível.
   iv. alterarCombustivel( ) – altera o tipo do combustível.
    v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.'''

class BombaCombustivel:
    def __init__(self,tipo_combustivel:str, valor_litro: float, quantidade_combustivel: float):
        self.valor_litro = valor_litro
        self.tipo_combustivel = tipo_combustivel
        self.quantidade_combustivel = quantidade_combustivel
    def abastecer_por_valor(self, valor:float):
        litros_abastecidos = valor / self.valor_litro
        self._apresentar_abastecimento_se_possivel (litros_abastecidos, valor)

    def _apresentar_abastecimento_se_possivel(self, litros_abastecidos:float, valor:float):
        if litros_abastecidos > self.quantidade_combustivel:
            print(f'Não é Possível abastecer, faltam {litros_abastecidos - self.quantidade_combustivel:.2f} litros.')
            print('Reabasteça ou procure outra bomba.')
        else:
            self.quantidade_combustivel -= litros_abastecidos
            print(f'Foram abastecidos {litros_abastecidos:.3f} litros a um valor de R${valor:.2f}')
            print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel}')
    def abastecer_por_litros(self, litros_abastecidos:float):
        valor = litros_abastecidos * self.valor_litro
        self._apresentar_abastecimento_se_possivel (litros_abastecidos, valor)

    def adicionar_mais_combustivel(self, quantidade:float):
        if quantidade >= 0:
            self.quantidade_combustivel += quantidade
        else:
            print('não é possivel fazer operação!')

bomba = BombaCombustivel('Gasolina', 4.59, 100.0)

bomba.abastecer_por_valor(100.0)
bomba.abastecer_por_litros(50.0)

bomba.valor_litro = 5.59
bomba.abastecer_por_litros(50)
bomba.adicionar_mais_combustivel(100)
bomba.abastecer_por_litros(50)
