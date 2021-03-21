#Estrutura condicional composta

def main():

    peso1 = float(input("Digite o peso do 1º livro:"))
    peso2 = float(input("Digite o peso do 2º livro:"))
    peso3 = float(input("Digite o peso do 3º livro:"))

    soma1 = float(peso1+peso2)
    soma2 = float(peso1+peso3)
    soma3 = float(peso2+peso3)

    if soma1>soma2 and soma1>soma3:
        print("A soma dos mais pesados é de:",soma1,"kg")
    elif soma2>soma3:
        print("A soma dos mais pesada é de:",soma2,"kg")
    else:
        print("A soma dos mais pesada é de:",soma3,"kg")

    

main()