from cliente import Cliente

class Conta(Cliente):

    def __init__(self,nome,nasc,cidade,fone,cpf,saldo):
        Cliente.__init__(self,nome,nasc,cidade,fone,cpf,saldo)


    def depositar(self,deposito):

       print('Deposito realizado:',deposito)
       self.saldo += deposito


    def sacar(self,saque):

        print('Saque realizado:',saque)
        self.saldo -= saque




