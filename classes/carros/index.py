from carro import Carro


tiggo5x = Carro('branco','2021','CaoaChery',50,10)

print(tiggo5x)
print(type(tiggo5x))
print('Tiggo 5x')
print('cor:' ,tiggo5x.cor)
print('marca:',tiggo5x.marca)
print('capacidade do tanque:',tiggo5x.tanque,'L')
print('Ano:',tiggo5x.ano)
print('abastecido:',tiggo5x.abastecido,'L')

print('                 ')


tiggo7 = Carro('Azul','2022','CaoaChery',60,10)

print(tiggo7)
print(type(tiggo7))
print('Tiggo 7')
print('cor:' ,tiggo7.cor)
print('marca:',tiggo7.marca)
print('capacidade do tanque:',tiggo7.tanque,'L')
print('Ano:',tiggo7.ano)
tiggo7.abastecer(20)
print('abastecido:',tiggo7.abastecido,'L')
tiggo7.abastecer(55)
print('abastecido:',tiggo7.abastecido,'L')

