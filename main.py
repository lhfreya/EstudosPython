from pedido import Pedido



op1 = Pedido('Marmita c/Churrasco',12.00,0.5,500,0)
op2 = Pedido('Marmita c/ Feijoada',12.00,0.5,700,0)
op3 = Pedido('Marmita Fitness',15.00,0.25,200,0)




print('Digite 1 para marmita c/ Churrasco')
print('Digite 2 para marmita c/ Feijoada')
print('Digite 3 para marmita fitness')
print('Digite 4 para os 3 tipos de marmita')


sair = False
while not sair:

    op = input('Escolha uma opção ou sair:')




    if op == 1:
        op1.pedir(op1.valor)
        print('Marmita c/Churrasco')
        op = 5



    elif op == 2:

        print('Marmita c/ Feijoada')
        op1.pedir(op2.valor)

        op = 5

    elif op == 3:

        print('Marmita fitness')
        op1.pedir(op3.valor)

        op = 5

    elif op == 4:

        print('Marmita fitness')
        op1.pedir(op1.valor+op2.valor+op3.valor)

        op = 5

    elif op == 5:

        pagamento = float(input('Digite o valor do pagamento:'))
        op1.pagar(pagamento)
        break

    elif op == 'sair':
         sair = True
         print('Até mais!')






































