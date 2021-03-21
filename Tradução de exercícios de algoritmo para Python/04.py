def main():

#declaração de variaveis

    soma: float = 0
    cont: int = 0



    while cont < 5:

        nota = float(input("nota..:"))
        soma = soma + nota
        cont = cont + 1

    # processamento


    media = soma / cont

    print("A média das notas é: ", media)


main()
