#entrada dados
n1 = input('Digite o 1 numero: ')

n2 = input('Digite o 2 numero: ')

n3 = input('Digite o 3 numero: ')


def maior():

#processamento

 if n1 > n2 and n3:
        print(n1, 'e o maior numero!!')

 elif n2 > n1 and n3:

          print(n2, 'e o maior numero!!')

 elif n3 > n1 and n2:

         print(n3, 'e o maior numero!!')

 elif n1 == n2 and n1 and n2 > n3:

            print (n1, 'e', 'o maior!!')

 elif n1 == n3 and n1 and n3 > n2:

            print (n1, 'e', 'o maior!!')

 elif n2 == n3 and n2 and n3 > n1:

            print (n2, 'e', 'o maior!!')

 elif n1 == n2 and n3:

            print('todos o numeros sao iguais')


def menor():


 if n1 < n2 and n3 and n1:

           print(n1, 'e o menor numero!!')

 elif n2 < n1 and n3:

          print(n2, 'e o menor numero!!')

 elif n3 < n1 and n2:

          print(n3, 'e o menor numero!!')

 elif n1 == n2 and n1 and n2 < n3:

          print (n1, 'e', 'o menor!!')

 elif n1 == n3 and n1 and n3 < n2:

          print(n1, 'e', 'o menor!!')

 elif n2 == n3 and n2 and n3 < n1:

          print(n2, 'e', 'o menor!!')

maior()
menor()