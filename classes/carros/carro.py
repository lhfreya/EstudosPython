from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self,cor,ano,marca,tanque,abastecido):
        Veiculo.__init__(self,cor,ano,marca,tanque,abastecido)

    def abastecer(self,litros):

        if self.abastecido + litros > self.tanque:

           print('Error: Litragem maior que a capacidade máxima de combustível ')

        else:
            self.abastecido += litros




