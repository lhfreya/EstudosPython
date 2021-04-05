from conta import Conta


cliente00 = Conta('Alexia',1990,'Goiânia','(62)99911-0000','001.001.001-10',0)
print('Nome:',cliente00.nome)
print('Nascimento:',cliente00.nasc)
print('Localidade:',cliente00.cidade)
print('Telefone:',cliente00.fone)
print('CPF:',cliente00.cpf)
print(cliente00)
cliente00.depositar(20)
print('Saldo:',cliente00.saldo)
cliente00.sacar(15)
print('Saldo:',cliente00.saldo)

print('                                   ')
cliente01 = Conta('Fulana',1989,'Goiânia','(62)99911-0001','021.011.021-10',0)
print('Nome:',cliente01.nome)
print('Nascimento:',cliente01.nasc)
print('Localidade:',cliente01.cidade)
print('Telefone:',cliente01.fone)
print('CPF:',cliente01.cpf)
print(cliente01)
cliente01.depositar(10000)
print('Saldo:',cliente01.saldo)
cliente01.sacar(750)
print('Saldo:',cliente01.saldo)

