from pedido import Pedido



op1 = Pedido('Marmita c/Churrasco',12.00,0.5,500,0)
op2 = Pedido('Marmita c/ Feijoada',12.00,0.5,700,0)
op3 = Pedido('Marmita Fitness',15.00,0.25,200,0)




print('Pedido')
op1.pedir(op1.valor+op2.valor+op3.valor)
print('Pagamento')
op1.pagar(50.00)

print('')
print('Pedido')
op1.pedir(op1.valor+op2.valor)
print('Pagamento')
op1.pagar(20.00)

print('')
print('Pedido')
op1.pedir(op1.valor+op3.valor)
print('Pagamento')
op1.pagar(250.00)






































