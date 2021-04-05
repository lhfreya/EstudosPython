from marmitas import Marmita



class Pedido(Marmita):

    def __init__(self,tipo,valor,peso,caloria,valorAP):
        Marmita.__init__(self,tipo,valor,peso,caloria,valorAP)
        self.valoraAP = 0

    def pedir(self,VT):

        self.valorAP += VT
        print('Valor do pedido:',self.valorAP,'R$')


    def pagar(self,PGM):

      while self.valorAP > 0:
        if PGM < self.valorAP:

          print('Valor insuficiente!')
          break

        elif PGM > self.valorAP:

            self.valorAP = PGM - self.valorAP
            print('O valor Pago é de:',PGM,'R$')
            print('O valor do troco é de:', self.valorAP,"R$")
            print('Obrigado por comprar com a gente! Volte sempre.')
            break

        else:

             self.valorAP = self.valoraAP-PGM
             print('Obrigado por comprar com a gente! Volte sempre.')
             break









