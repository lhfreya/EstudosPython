def main():

#declaração de variaveis

    soma = float
    cont: int = 0



    while cont < 5:
        nota = float(input("nota..:"))

        cont = cont + 1

    # processamento

    soma = soma + nota
    media = soma / cont

    print("A média das notas é: ", media)


main()
